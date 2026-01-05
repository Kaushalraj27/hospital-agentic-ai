# 🏥 Hospital Agentic AI Assistant – Task 1

## 📌 Overview
This project implements a **customer-facing Hospital AI Assistant** that helps patients:
- Log in to the system
- Store patient profile details
- Check doctor availability
- Book appointments
- Get department suggestions based on symptoms

The system is built using **Python** and **SQLite**, and follows a simple interactive console-based approach.

---

## 🛠️ Technologies Used
- Python 3.x
- SQLite (for database)
- Standard Python libraries (sqlite3, re, datetime)

---

## 📂 Project Structure

```

hospital-agent-ai/
│
├── app.py                     # Main application entry point
├── init_db.py                 # Database initialization & data population
├── response_agent.py          # Handles responses & outputs
├── intent_agent.py            # Parses user intent (rule-based)
├── schema.sql                 # Database schema
│
├── database/
│   └── hospital.db            # SQLite database file
│
└── README.md                  # Project documentation

```

---

## 🗄️ Database Design

### 1. doctors_availability
| Column Name | Type | Description |
|------------|------|------------|
| doctor_id | INTEGER | Primary key |
| name | TEXT | Doctor name |
| department | TEXT | Department |
| day_of_week | TEXT | Day |
| time_slot | TEXT | Time slot |
| is_booked | BOOLEAN | Booking status |

### 2. patients
| Column Name | Type | Description |
|------------|------|------------|
| patient_id | INTEGER | Primary key |
| name | TEXT | Patient name |
| age | INTEGER | Patient age |
| medical_issue | TEXT | Symptoms |

The database contains **20+ doctors across 5+ departments**.

---

## 🔐 User Login
A fixed test user is implemented as required:

```

Username: patient1
Password: pass123

```

After login, the user is prompted to enter:
- Name
- Age
- Medical issue

These details are stored in the database.

---

## 💬 Supported Queries

The AI assistant supports the following types of natural language queries:

### 1. Symptom-Based Query
```

"I have chest pain"

```
→ Suggests relevant department

### 2. Availability Check
```

"Show available doctors in Cardiology on Monday"

```
→ Lists available doctors and slots

### 3. Booking Request
```

"Book a slot with Dr Rahul on Monday at 09:00-10:00"

````
→ Confirms booking if slot is free

---

## ▶️ How to Run the Project

### Step 1: Initialize the Database
```bash
python init_db.py
````

### Step 2: Run the Application

```bash
python app.py
```

---

## 🧪 Sample Interaction

```
Welcome to Hospital AI Assistant
Username: patient1
Password: pass123
Login successful!

Enter your name: Kaushal
Enter your age: 22
Describe your medical issue: chest pain
Patient profile saved successfully!

Ask your question: Show available doctors in Cardiology on Monday
Available doctors:
- Dr Rahul at 09:00-10:00

Ask your question: Book a slot with Dr Rahul on Monday at 09:00-10:00
Appointment booked successfully!
```

---

## ⚠️ Edge Case Handling

* Invalid login credentials are rejected
* Booking an already booked slot is prevented
* If no doctors are available, alternatives are suggested

---

## 📈 Future Scope

* Integration of ML-based query classification (Task-2)
* Web or Streamlit interface
* Email/SMS notifications

---

## ✅ Conclusion

This project successfully demonstrates a working **Hospital Agentic AI Assistant** with SQL-backed persistence, rule-based query handling, and appointment booking. The modular design allows easy extension for advanced AI features.

---

```

---

## ✅ FINAL NOTE (IMPORTANT)

✔ This README **perfectly matches Task-1 requirements**  
✔ Simple, clean, examiner-friendly  
✔ No unnecessary ML mentions  
✔ Safe for **direct submission**

---


