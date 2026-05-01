import json

with open("data/db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

index = {}

for item in db:
    words = (item["title"] + " " + item["content"]).lower().split()

    for w in words:
        if w not in index:
            index[w] = []
        index[w].append(item["id"])

with open("data/index.json", "w") as f:
    json.dump(index, f)

print("✅ Index built")
