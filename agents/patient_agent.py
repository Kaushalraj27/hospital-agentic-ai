import sqlite3

DB_PATH = "database/hospital.db"

def save_patient(name, age, medical_issue):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients (name, age, medical_issue)
        VALUES (?, ?, ?)
    """, (name, age, medical_issue))

    conn.commit()
    conn.close()
