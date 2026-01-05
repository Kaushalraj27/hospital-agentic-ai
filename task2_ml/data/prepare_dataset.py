import pandas as pd
import re

# ===============================
# 1. LOAD RAW KAGGLE DATASET
# ===============================
# Rename your downloaded CSV to this name
RAW_DATA_PATH = "task2_ml/data/Healthcare.csv"
OUTPUT_PATH = "task2_ml/data/symptom_department.csv"

df = pd.read_csv(RAW_DATA_PATH)

# Keep only required columns
df = df[["Symptoms", "Disease"]]


# ===============================
# 2. DISEASE → DEPARTMENT MAPPING
# ===============================
DISEASE_TO_DEPARTMENT = {

    # Cardiology
    "Heart Disease": "Cardiology",
    "Hypertension": "Cardiology",

    # Neurology
    "Stroke": "Neurology",
    "Migraine": "Neurology",
    "Epilepsy": "Neurology",

    # Pulmonology
    "Bronchitis": "Pulmonology",
    "COVID-19": "Pulmonology",
    "Pneumonia": "Pulmonology",

    # Gastroenterology
    "Food Poisoning": "Gastroenterology",
    "Gastritis": "Gastroenterology",
    "Diarrhea": "Gastroenterology",

    # Endocrinology
    "Thyroid Disorder": "Endocrinology",
    "Diabetes": "Endocrinology",

    # Psychiatry
    "Depression": "Psychiatry",
    "Anxiety": "Psychiatry",
    "Insomnia": "Psychiatry",

    # Dermatology
    "Skin Infection": "Dermatology",
    "Rash": "Dermatology",

    # General Medicine
    "Influenza": "General Medicine",
    "Allergy": "General Medicine",
    "Fever": "General Medicine"
}


# ===============================
# 3. KEYWORD-BASED FALLBACK ROUTING
# ===============================
def keyword_department(symptoms):
    text = symptoms.lower()

    if re.search(r"tooth|gum|jaw|dental", text):
        return "Dentistry"

    if re.search(r"sexual|erection|libido|impotence", text):
        return "Sexology"

    if re.search(r"ear|hearing|nose|throat", text):
        return "ENT"

    if re.search(r"joint|bone|knee|back pain|fracture", text):
        return "Orthopedics"

    if re.search(r"menstrual|pregnant|pregnancy|uterus", text):
        return "Gynecology"

    if re.search(r"child|infant|baby", text):
        return "Pediatrics"

    if re.search(r"skin|itch|rash", text):
        return "Dermatology"

    if re.search(r"cough|breath|lungs", text):
        return "Pulmonology"

    if re.search(r"vomiting|nausea|diarrhea|stomach", text):
        return "Gastroenterology"

    return None


# ===============================
# 4. APPLY MAPPING LOGIC
# ===============================
# First: disease → department
df["department"] = df["Disease"].map(DISEASE_TO_DEPARTMENT)

# Second: symptom keyword fallback
df["department"] = df.apply(
    lambda row: row["department"]
    if pd.notna(row["department"])
    else keyword_department(row["Symptoms"]),
    axis=1
)

# Drop rows still unmapped
df = df.dropna(subset=["department"])

# Rename column for training compatibility
df = df.rename(columns={"Symptoms": "query_text"})


# ===============================
# 5. SAVE FINAL DATASET
# ===============================
df[["query_text", "department"]].to_csv(
    OUTPUT_PATH,
    index=False
)

print("\n✅ Dataset preparation completed successfully!")
print("Total samples:", len(df))
print("\nDepartment distribution:")
print(df["department"].value_counts())
