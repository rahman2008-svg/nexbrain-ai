import json

FILE = "data/db.json"

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

seen = set()
clean = []

for item in data:
    key = item["title"].strip().lower()

    if key in seen:
        continue

    seen.add(key)
    clean.append(item)

# re-id
for i, item in enumerate(clean):
    item["id"] = i + 1

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(clean, f, indent=2, ensure_ascii=False)

print(f"✅ cleaned dataset | total: {len(clean)}")
