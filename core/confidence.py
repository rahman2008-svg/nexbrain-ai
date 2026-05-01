def confidence(score):
    if score >= 15:
        return "High"
    elif score >= 8:
        return "Medium"
    else:
        return "Low"
