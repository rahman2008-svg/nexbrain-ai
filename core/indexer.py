# core/indexer.py

from core.utils import tokenize

def build_index(db):
    index = {}

    for i, item in enumerate(db):
        text = item["title"] + " " + item["content"] + " " + " ".join(item["tags"])
        tokens = tokenize(text)

        for t in tokens:
            if t not in index:
                index[t] = set()
            index[t].add(i)

    return index


def search_index(query, db, index):
    q_tokens = tokenize(query)
    candidates = set()

    for t in q_tokens:
        if t in index:
            candidates.update(index[t])

    # fallback: যদি কিছু না মিলে
    if not candidates:
        return list(range(len(db)))

    return list(candidates)
