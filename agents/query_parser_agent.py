import re

DEPARTMENTS = [
    "cardiology", "neurology", "orthopedics",
    "pediatrics", "dermatology", "general medicine"
]

DAYS = [
    "monday", "tuesday", "wednesday",
    "thursday", "friday", "saturday", "sunday"
]

def extract_department_and_day(query):
    q = query.lower()

    department = None
    day = None

    for d in DEPARTMENTS:
        if d in q:
            department = d.title()
            break

    for d in DAYS:
        if d in q:
            day = d.title()
            break

    return department, day
