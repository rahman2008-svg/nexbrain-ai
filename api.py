from flask import Flask, request, jsonify

from core.engine import rank
from core.indexer import build_index   # ✅ FIXED import
import json

app = Flask(__name__)

with open("data/db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

index = build_index(db)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data["message"]

    result, score = rank(query, db, index)

    return jsonify({
        "answer": result["content"],
        "title": result["title"],
        "score": score
    })


@app.route("/")
def home():
    return "NexBrain AI is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
