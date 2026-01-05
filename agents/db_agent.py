import sqlite3

DB_PATH = "database/hospital.db"

def get_available_doctors(department, day):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, time_slot FROM doctors_availability
    WHERE department=? AND day_of_week=? AND is_booked=0
    """, (department, day))

    data = cursor.fetchall()
    conn.close()
    return data
