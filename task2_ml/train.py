import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
)

from datasets import Dataset


# ---------------- CONFIG ----------------
MODEL_NAME = "distilbert-base-uncased"   # small & CPU-friendly
DATA_PATH = "task2_ml/data/symptom_department.csv"
OUTPUT_DIR = "task2_ml/trained_model"
EPOCHS = 3
BATCH_SIZE = 8
LEARNING_RATE = 2e-5


def main():
    print("Loading dataset...")

    # ---------------- LOAD DATA ----------------
    df = pd.read_csv(DATA_PATH)

    # Encode department labels
    label_encoder = LabelEncoder()
    df["label"] = label_encoder.fit_transform(df["department"])

    num_labels = len(label_encoder.classes_)
    print("Departments:", list(label_encoder.classes_))

    # ---------------- SPLIT DATA ----------------
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df["label"]
    )

    # Convert to HuggingFace Dataset
    train_dataset = Dataset.from_pandas(
        train_df[["query_text", "label"]]
    )
    test_dataset = Dataset.from_pandas(
        test_df[["query_text", "label"]]
    )

    # ---------------- TOKENIZER ----------------
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    def tokenize(batch):
        return tokenizer(
            batch["query_text"],
            padding="max_length",
            truncation=True,
            max_length=64
        )

    train_dataset = train_dataset.map(tokenize, batched=True)
    test_dataset = test_dataset.map(tokenize, batched=True)

    train_dataset.set_format(
        type="torch",
        columns=["input_ids", "attention_mask", "label"]
    )
    test_dataset.set_format(
        type="torch",
        columns=["input_ids", "attention_mask", "label"]
    )

    # ---------------- MODEL ----------------
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=num_labels
    )

    # ---------------- TRAINING ARGS ----------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=LEARNING_RATE,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        num_train_epochs=EPOCHS,
        weight_decay=0.01,
        logging_dir=f"{OUTPUT_DIR}/logs",
        logging_steps=10,
        load_best_model_at_end=True,
        metric_for_best_model="loss",
        report_to="none"   # disables wandb
    )

    # ---------------- TRAINER ----------------
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        tokenizer=tokenizer
    )

    # ---------------- TRAIN ----------------
    print("Starting training...")
    trainer.train()

    # ---------------- SAVE MODEL ----------------
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    # Save label mapping
    label_map = {
        idx: label
        for idx, label in enumerate(label_encoder.classes_)
    }

    with open(f"{OUTPUT_DIR}/label_map.txt", "w") as f:
        for k, v in label_map.items():
            f.write(f"{k}:{v}\n")

    print("Training completed successfully!")
    print("Model saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()


