def classify_intent(query):
    q = query.lower()
    if "book" in q:
        return "BOOK"
    elif "available" in q or "show" in q:
        return "AVAILABILITY"
    else:
        return "SYMPTOM"
