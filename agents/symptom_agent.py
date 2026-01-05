def suggest_department(symptom_text):
    text = symptom_text.lower()

    if "chest pain" in text or "heart" in text:
        return "Cardiology"
    elif "headache" in text or "dizziness" in text:
        return "Neurology"
    elif "bone" in text or "joint" in text:
        return "Orthopedics"
    elif "child" in text or "fever" in text:
        return "Pediatrics"
    elif "skin" in text or "rash" in text:
        return "Dermatology"
    else:
        return "General Medicine"

