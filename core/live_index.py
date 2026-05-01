# core/live_index.py

from core.utils import tokenize

def update_index_with_item(index, item, item_id):
    text = item["title"] + " " + item["content"] + " " + " ".join(item["tags"])
    tokens = tokenize(text)

    for t in tokens:
        if t not in index:
            index[t] = set()
        index[t].add(item_id)

    return index
