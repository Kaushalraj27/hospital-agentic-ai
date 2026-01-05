import torch
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 🔥 DIRECT CLASSES (NO AUTO)
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

MODEL_DIR = "task2_ml/trained_model/trained_model"
DATA_PATH = "task2_ml/data/symptom_department.csv"

# Load tokenizer & model (LOCAL ONLY)
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_DIR)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

# Load dataset
df = pd.read_csv(DATA_PATH)

label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["department"])

texts = df["query_text"].tolist()
true_labels = df["label"].tolist()

pred_labels = []

# Prediction loop
for text in texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    pred_labels.append(pred)

print("\n=== CLASSIFICATION REPORT ===\n")
print(classification_report(
    true_labels,
    pred_labels,
    target_names=label_encoder.classes_
))

print("\n=== CONFUSION MATRIX ===\n")
print(confusion_matrix(true_labels, pred_labels))
