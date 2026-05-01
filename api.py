import sys
import os
from flask import Flask, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from tools.ask import ask

app = Flask(__name__)

# =========================
# HOME UI (ChatGPT STYLE)
# =========================
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>NexBrain AI</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
            }

            #chat {
                width: 80%;
                margin: auto;
                margin-top: 20px;
                text-align: left;
            }

            .msg {
                padding: 10px;
                margin: 10px;
                border-radius: 10px;
            }

            .user { background: #1e293b; }
            .bot { background: #334155; }

            input {
                width: 60%;
                padding: 10px;
                margin-top: 20px;
            }

            button {
                padding: 10px;
                margin-left: 5px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>

        <h1>🤖 NexBrain AI</h1>

        <input id="msg" placeholder="Ask something..." />
        <button onclick="send()">Send</button>
        <button onclick="startVoice()">🎤</button>

        <div id="chat"></div>

        <script>

        let history = [];

        function typeText(element, text, i = 0) {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                setTimeout(() => typeText(element, text, i + 1), 15);
            }
        }

        function speak(text) {
            let speech = new SpeechSynthesisUtterance(text);
            speech.lang = "en-US";
            speech.rate = 1;
            window.speechSynthesis.speak(speech);
        }

        function updateUI() {
            let chat = document.getElementById("chat");
            chat.innerHTML = "";

            history.forEach(m => {
                chat.innerHTML += `
                    <div class="msg ${m.role}">
                        ${m.role === "user" ? "You" : "AI"}: ${m.text}
                    </div>
                `;
            });
        }

        async function send() {
            let msg = document.getElementById("msg").value;
            if (!msg) return;

            history.push({role: "user", text: msg});
            updateUI();

            let res = await fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: msg})
            });

            let data = await res.json();

            let botDiv = document.createElement("div");
            botDiv.className = "msg bot";
            botDiv.innerHTML = "AI: ";
            document.getElementById("chat").appendChild(botDiv);

            typeText(botDiv, data.answer);

            speak(data.answer);

            history.push({role: "bot", text: data.answer});

            document.getElementById("msg").value = "";
        }

        function startVoice() {
            let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = "en-US";

            recognition.onresult = function(event) {
                document.getElementById("msg").value =
                event.results[0][0].transcript;
            };

            recognition.start();
        }

        </script>

    </body>
    </html>
    """

# =========================
# CHAT API
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    result = ask(message)

    if isinstance(result, dict):
        answer = f"{result['title']}\n\n{result['content']}"
    else:
        answer = result

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
