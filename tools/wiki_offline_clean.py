import json
import requests

FILE = "data/db.json"

topics = [
    "Python_(programming_language)",
    "Artificial_intelligence",
    "Machine_learning",
    "Deep_learning",
    "Computer_science",
    "Bangladesh",
    "Physics",
    "Chemistry",
    "Biology",
    "Mathematics",
    "Internet",
    "Robotics",
    "Technology",
    "Science",
    "History"
]

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fetch(topic):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + topic
    try:
        r = requests.get(url, timeout=10).json()
        return r.get("title"), r.get("extract")
    except:
        return None, None

data = load()
seen_titles = set([d["title"].lower() for d in data])

new_data = []
id_counter = len(data) + 1

for topic in topics:
    title, content = fetch(topic)

    if not title or not content:
        continue

    clean_title = title.strip().lower()

    # 🧠 duplicate filter
    if clean_title in seen_titles:
        continue

    seen_titles.add(clean_title)

    new_data.append({
        "id": id_counter,
        "title": f"{title} কী?",
        "content": content,
        "tags": ["wiki", "knowledge"]
    })

    id_counter += 1

data.extend(new_data)
save(data)

print("✅ Clean Wikipedia dataset added (duplicate-free)")
