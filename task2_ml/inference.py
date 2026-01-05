import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_DIR = "task2_ml/trained_model_final/trained_model"


def load_label_map():
    label_map = {}
    with open(f"{MODEL_DIR}/label_map.txt", "r") as f:
        for line in f:
            idx, label = line.strip().split(":")
            label_map[int(idx)] = label
    return label_map


def predict_department(text):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    model.eval()

    label_map = load_label_map()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=64
    )

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()

    return label_map[predicted_class]


def main():
    print("🏥 Hospital Department Prediction (Task-2)")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Enter patient symptom query: ")

        if query.lower() == "exit":
            print("Exiting interface.")
            break

        department = predict_department(query)
        print(f"Predicted Department: {department}\n")


if __name__ == "__main__":
    main()
