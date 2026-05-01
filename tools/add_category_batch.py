import json
import os

FILE = "data/db.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_categories(categories):
    data = load()

    seen = set(d["title"].lower() for d in data)

    new_id = len(data) + 1
    added = 0

    for cat, items in categories.items():
        for item in items:

            title = f"{item} কী?"

            if title.lower() in seen:
                continue

            data.append({
                "id": new_id,
                "title": title,
                "content": f"{item} হলো {cat} সম্পর্কিত একটি গুরুত্বপূর্ণ বিষয়।",
                "tags": [cat, item.lower(), "knowledge"]
            })

            seen.add(title.lower())
            new_id += 1
            added += 1

    save(data)

    print(f"✅ Added {added} items | Total: {len(data)}")


# =========================
# FINAL CATEGORY SET (ONLY ONE)
# =========================
if __name__ == "__main__":

    categories = {
"daily_life": [
    "Time", "Weather", "Calendar", "Day", "Night",
    "Morning", "Evening", "Sleep", "Food", "Water",
    "Health Tips", "Exercise", "Study", "Work", "Routine"
],

"education_skills": [
    "Reading", "Writing", "Listening", "Speaking",
    "Memory", "Concentration", "Learning", "Teaching",
    "Problem Solving", "Critical Thinking"
],

"transport": [
    "Car", "Bus", "Train", "Bicycle", "Airplane",
    "Ship", "Traffic", "Road", "Highway", "Airport"
],

"science_in_daily_life": [
    "Electricity", "Magnet", "Gravity", "Light",
    "Sound", "Heat", "Energy", "Force", "Motion"
],

"digital_world": [
    "Mobile Phone", "Laptop", "App", "Website",
    "WiFi", "Bluetooth", "Software", "Hardware",
    "Operating System", "File System"
]
    }

    add_categories(categories)
