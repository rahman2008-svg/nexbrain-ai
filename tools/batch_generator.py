import json
import os

FILE = "data/db.json"

# 10 different topic groups (rotation system)
topic_groups = [
    ["Python", "AI", "ML", "Deep Learning", "Data Science"],
    ["Bangladesh", "India", "USA", "China", "Japan"],
    ["Physics", "Chemistry", "Biology", "Math", "Science"],
    ["Internet", "Computer", "Technology", "Programming", "Software"],
    ["Robotics", "Blockchain", "Cybersecurity", "Cloud", "Database"],
    ["History", "Geography", "Culture", "Politics", "Economics"],
    ["Space", "NASA", "Mars", "Solar System", "Universe"],
    ["Human Body", "Medicine", "Disease", "Nutrition", "Genetics"],
    ["Environment", "Climate", "Earth", "Nature", "Disaster"],
    ["Education", "Knowledge", "Learning", "Research", "Innovation"]
]

# load old data
if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = []

start_id = len(data) + 1
new_data = []

# generate 1000 items per batch run
for i in range(200):  # 200 × 5 topics = 1000
    group = topic_groups[i % len(topic_groups)]

    for topic in group:
        new_data.append({
            "id": start_id,
            "title": f"{topic} কী?",
            "content": f"{topic} হলো একটি গুরুত্বপূর্ণ বিষয় যা শিক্ষা ও বাস্তব জীবনে ব্যবহার হয়।",
            "tags": [topic.lower(), "knowledge"]
        })
        start_id += 1

# merge
data.extend(new_data)

# limit 10K
data = data[:10000]

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Batch done | Total data: {len(data)}")
