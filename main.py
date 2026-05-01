import json
from app.chat import chat
from core.indexer import build_index
from core.preprocess import preprocess_db   # 🔥 ADD

def load_db():
    with open("data/db.json", "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    print("⏳ Loading DB...")

    db = load_db()

    print("⚡ Preprocessing DB...")
    db = preprocess_db(db)   # 🔥 ADD

    print("⚡ Building Index...")
    index = build_index(db)

    chat(db, index)
