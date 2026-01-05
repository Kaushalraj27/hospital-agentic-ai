# 🏥 Hospital Agentic AI Assistant

**Task-1: Agentic AI System | Task-2: ML-based Department Prediction**

---

## 📌 Project Overview

This project implements a **Hospital Agentic AI Assistant** using a **multi-agent architecture**.
The system supports:

* Patient login & profile management
* Natural language symptom queries
* Doctor availability lookup
* Appointment booking with SQL persistence
* ML-based department prediction from patient symptoms

The project is divided into **two well-defined tasks**:

* **Task-1:** Rule-based Agentic AI Assistant (core system)
* **Task-2:** Machine Learning model for symptom → department prediction

---

## 🧠 Task-1: Hospital Agentic AI Assistant

### 🎯 Objective

To design and implement a **customer-facing agentic AI system** that interacts with patients, manages doctor availability, and handles appointment booking using SQL.

---

### 🧩 Architecture (Multi-Agent System)

The system is built using **specialized agents**, each responsible for a specific task:

| Agent                 | Responsibility                                           |
| --------------------- | -------------------------------------------------------- |
| Authentication Agent  | Handles user login (test user based)                     |
| Patient Profile Agent | Stores patient details (name, age, issue)                |
| Intent Agent          | Identifies user intent (symptoms, availability, booking) |
| DB Agent              | Queries SQLite database                                  |
| Booking Agent         | Performs atomic booking transactions                     |
| Response Agent        | Generates final user responses                           |

---

### 🗂 Database Design (SQLite)

#### `doctors_availability`

| Column      | Description      |
| ----------- | ---------------- |
| doctor_id   | Primary key      |
| name        | Doctor name      |
| department  | Department       |
| day_of_week | Availability day |
| time_slot   | Time range       |
| is_booked   | Booking status   |

#### `patients`

| Column        | Description      |
| ------------- | ---------------- |
| patient_id    | Primary key      |
| name          | Patient name     |
| age           | Patient age      |
| medical_issue | Patient symptoms |

---

### 🖥 Interfaces Supported

* Console-based interaction (`app.py`)
* Streamlit UI (`streamlit_app.py`)

---

### ▶️ How to Run Task-1

```bash
pip install -r requirements.txt
python app.py
```

OR (Streamlit UI)

```bash
streamlit run streamlit_app.py
```

---

### ✅ Example Interactions

* “I have chest pain”
* “Show available doctors in Cardiology on Monday”
* “Book a slot with Dr Rahul on Monday at 09:00-10:00”

---

## 🤖 Task-2: ML-Based Department Prediction

### 🎯 Objective

To build a **machine learning model** that predicts the **relevant hospital department** based on patient symptoms.

---

### 📊 Dataset

* Source: Kaggle Healthcare Dataset
* Total samples: **23,000+**
* Final departments used (10 classes):

```
Cardiology
Dermatology
ENT
Endocrinology
Gastroenterology
General Medicine
Neurology
Orthopedics
Psychiatry
Pulmonology
```

---

### 🛠 Data Pipeline

* Raw dataset stored in: `task2_ml/data/Healthcare.csv`
* Cleaned dataset: `symptom_department.csv`
* Preprocessing logic: `prepare_dataset.py`

This ensures **reproducibility and transparency**.

---

### 🧠 Model Details

| Item          | Value                      |
| ------------- | -------------------------- |
| Model         | DistilBERT                 |
| Task          | Multi-class classification |
| Framework     | HuggingFace Transformers   |
| Training      | Google Colab (GPU)         |
| Loss Function | Cross-Entropy              |
| Epochs        | 3                          |

---

### 📈 Evaluation Metrics

**Classification Report (summary):**

* Accuracy: **~47%**
* Macro F1-Score: **~0.30**
* Weighted F1-Score: **~0.36**

**Confusion Matrix** was generated to analyze misclassification trends and class imbalance.

> Note: Some departments show lower precision due to overlapping symptom patterns and dataset imbalance, which is expected in real medical data.

---

### ▶️ How to Run Task-2 Locally

#### Inference

```bash
python task2_ml/inference.py
```

#### Evaluation

```bash
python task2_ml/evaluate.py
```

---

### 📁 Why Trained Model Is Not Uploaded?

The `trained_model/` directory is **intentionally excluded** via `.gitignore`:

* Model size is large
* HuggingFace models are reproducible
* Training script is provided
* Industry-standard best practice

---

## 📂 Repository Structure

```
hospital-agentic-ai/
│
├── agents/          # Task-1 agents
├── auth/
├── database/
├── reports/
│
├── task2_ml/
│   ├── data/
│   ├── train.py
│   ├── inference.py
│   ├── evaluate.py
│   ├── model_info.txt
│
├── app.py
├── streamlit_app.py
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Key Highlights

* Clean multi-agent architecture
* SQL-based persistence
* Atomic booking transactions
* Scalable ML pipeline
* Clear task separation
* Industry-ready repo structure

---

## 🧾 Conclusion

This project demonstrates a **complete end-to-end AI system** combining:

* Rule-based agentic AI (Task-1)
* ML-based intelligence (Task-2)

The solution is **modular, explainable, and extensible**, making it suitable for real-world healthcare automation scenarios.


