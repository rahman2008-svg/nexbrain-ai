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

def add_batch(items):
    data = load()

    seen = set([x["title"].lower() for x in data])

    for item in items:
        if item["title"].lower() in seen:
            continue

        data.append(item)
        seen.add(item["title"].lower())

    save(data)

    print(f"✅ Total dataset: {len(data)}")
