import json

# load database
with open("data/db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# load index
with open("data/index.json", "r", encoding="utf-8") as f:
    index = json.load(f)


def search(query):
    words = query.lower().split()

    candidate_ids = set()

    for w in words:
        if w in index:
            candidate_ids.update(index[w])

    results = []

    for item in db:
        if item["id"] in candidate_ids:
            results.append(item)

    return results
