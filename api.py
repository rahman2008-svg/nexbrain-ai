from flask import Flask, request, jsonify

from core.engine import rank
from core.indexer import build_index
import json

app = Flask(__name__)

# load database
with open("data/db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

index = build_index(db)


# 🤖 CHAT API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data["message"]

    result, score = rank(query, db, index)

    return jsonify({
        "title": result["title"],
        "answer": result["content"],
        "score": score
    })


# 🌐 ROOT = UI (MAIN FIX)
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>NexBrain AI</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 50px;
                background: #f5f5f5;
            }
            input {
                padding: 10px;
                width: 250px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px;
                margin-left: 5px;
                border-radius: 5px;
                border: none;
                background: #333;
                color: white;
                cursor: pointer;
            }
            #out {
                margin-top: 20px;
                font-size: 18px;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>

        <h1>🤖 NexBrain AI</h1>

        <input id="msg" placeholder="Ask something..." />
        <button onclick="send()">Send</button>

        <p id="out"></p>

        <script>
        async function send(){
            let msg = document.getElementById('msg').value;

            let res = await fetch('/chat', {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body: JSON.stringify({message: msg})
            });

            let data = await res.json();
            document.getElementById('out').innerText = data.answer;
        }
        </script>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
