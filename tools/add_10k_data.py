import json
import os

FILE = "data/db.json"

topics = [
    "Python", "AI", "Machine Learning", "Deep Learning",
    "Bangladesh", "Computer", "Internet", "Physics",
    "Chemistry", "Biology", "Math", "History",
    "Geography", "Technology", "Robotics", "Science",
    "Programming", "Database", "Networking", "Cybersecurity"
]

def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

data = load()

start_id = len(data) + 1
new_data = []

# 1000 new items per run
for i in range(50):  # 50 × 20 = 1000
    for t in topics:
        new_data.append({
            "id": start_id,
            "title": f"{t} কী?",
            "content": f"{t} হলো একটি গুরুত্বপূর্ণ শিক্ষার বিষয় যা বাস্তব জীবনে ব্যবহার হয়।",
            "tags": [t.lower(), "knowledge"]
        })
        start_id += 1

data.extend(new_data)

# limit 10000
data = data[:10000]

save(data)

print(f"✅ Added batch | Total now: {len(data)}")
