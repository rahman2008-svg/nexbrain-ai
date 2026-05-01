def is_followup(query):
    followups = [
        "আর বলো", "more", "details",
        "explain", "what about it",
        "এটা কি", "বল আবার", "continue"
    ]
    return query.lower() in followups
