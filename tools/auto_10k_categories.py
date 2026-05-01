import json
import os

FILE = "data/db.json"

categories = {
    "countries": ["Bangladesh", "India", "USA", "China", "Japan", "UK"],
    "space": ["Solar System", "Mars", "Moon", "Sun", "Black Hole", "Galaxy"],
    "science": ["Physics", "Chemistry", "Biology", "AI", "Robotics", "Computer"],
    "tech": ["Internet", "Programming", "Database", "Cybersecurity"],
    "people": ["Einstein", "Newton", "Tesla", "Curie"],
    "religion": ["Islam", "Christianity", "Buddhism"],
    "education": ["Math", "History", "Geography"]
}

def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

data = load()

seen = set([d["title"].lower() for d in data])
new_id = len(data) + 1

batch_size = 10000
added = 0

while added < batch_size:

    for cat, items in categories.items():
        for item in items:

            title = f"{item} কী?"

            if title.lower() in seen:
                continue

            data.append({
                "id": new_id,
                "title": title,
                "content": f"{item} হলো {cat} সম্পর্কিত একটি গুরুত্বপূর্ণ বিষয়। এটি জ্ঞানভিত্তিক তথ্যের অংশ।",
                "tags": [cat, item.lower(), "knowledge"]
            })

            seen.add(title.lower())
            new_id += 1
            added += 1

            if added >= batch_size:
                break

        if added >= batch_size:
            break

save(data)

print(f"✅ 10K multi-category dataset done | Total: {len(data)}")
