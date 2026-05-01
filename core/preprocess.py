from core.utils import tokenize

def preprocess_db(db):
    for item in db:
        item["_tokens"] = tokenize(
            item["title"] + " " +
            item["content"] + " " +
            " ".join(item["tags"])
        )
    return db
