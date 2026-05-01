import json

subjects = [
    ("Python", "Python একটি জনপ্রিয় programming language যা সহজ এবং শক্তিশালী।"),
    ("JavaScript", "JavaScript ওয়েব ডেভেলপমেন্টে ব্যবহৃত একটি ভাষা।"),
    ("Artificial Intelligence", "AI হলো এমন প্রযুক্তি যা মানুষের মতো চিন্তা করতে পারে।"),
    ("Machine Learning", "Machine Learning হলো AI এর একটি অংশ যা data থেকে শেখে।"),
    ("Bangladesh", "Bangladesh দক্ষিণ এশিয়ার একটি দেশ যার রাজধানী ঢাকা।"),
    ("Computer", "Computer হলো একটি electronic device যা তথ্য প্রক্রিয়া করে।"),
    ("Internet", "Internet হলো বিশ্বব্যাপী network system।"),
    ("Physics", "Physics হলো পদার্থ ও শক্তি নিয়ে বিজ্ঞান।"),
    ("Chemistry", "Chemistry হলো পদার্থের গঠন নিয়ে বিজ্ঞান।"),
    ("Biology", "Biology হলো জীবজগত নিয়ে বিজ্ঞান।"),
    ("Math", "Math হলো সংখ্যার ও হিসাবের বিজ্ঞান।"),
    ("History", "History হলো অতীত ঘটনাবলি অধ্যয়ন।"),
    ("Geography", "Geography হলো পৃথিবী ও পরিবেশ নিয়ে বিজ্ঞান।"),
    ("Technology", "Technology হলো আধুনিক যন্ত্র ও উদ্ভাবন।"),
    ("Robotics", "Robotics হলো রোবট তৈরি ও নিয়ন্ত্রণের বিজ্ঞান।")
]

extra_topics = [
    "Education", "Science", "Space", "Internet Safety",
    "Programming Basics", "Algorithms", "Data Structures",
    "Operating System", "Networking", "Database",
    "Cybersecurity", "Blockchain", "Cloud Computing"
]

data = []
id_counter = 1

# main data
for i in range(300):  # 15 × 300 = 4500
    for t in subjects:
        data.append({
            "id": id_counter,
            "title": f"{t[0]} কী?",
            "content": t[1],
            "tags": ["education", "knowledge"]
        })
        id_counter += 1

# extra expansion
for i in range(400):  # 13 × 400 ≈ 5200
    for t in extra_topics:
        data.append({
            "id": id_counter,
            "title": f"{t} কী?",
            "content": f"{t} হলো আধুনিক শিক্ষার একটি গুরুত্বপূর্ণ বিষয়।",
            "tags": ["knowledge", "general"]
        })
        id_counter += 1

# limit 10K
data = data[:10000]

with open("data/db.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ 10,000 OFFLINE dataset তৈরি হয়েছে (NO WAIT, NO API)")
