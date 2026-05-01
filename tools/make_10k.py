import json
import random

topics = [
    "Python", "AI", "Machine Learning", "Math", "Physics",
    "Chemistry", "History", "Geography", "Biology", "Bangladesh",
    "Computer", "Internet", "Technology", "Science", "Education"
]

templates = [
    "এর অর্থ হলো {topic} সম্পর্কে একটি মৌলিক ধারণা।",
    "{topic} হলো আধুনিক বিশ্বের একটি গুরুত্বপূর্ণ বিষয়।",
    "{topic} সম্পর্কে জানা শিক্ষার জন্য গুরুত্বপূর্ণ।",
    "{topic} ব্যবহার করে অনেক সমস্যা সমাধান করা যায়।",
    "{topic} আজকের যুগে খুবই প্রয়োজনীয় একটি বিষয়।"
]

data = []
id_counter = 1

for i in range(700):  # 15 topics × 700 ≈ 10,500 data
    for topic in topics:
        text = random.choice(templates).format(topic=topic)

        data.append({
            "id": id_counter,
            "title": f"{topic} তথ্য {i}",
            "content": text,
            "tags": [topic.lower(), "education", "knowledge"]
        })

        id_counter += 1

with open("data/db.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ 10K dataset তৈরি হয়ে গেছে!")
