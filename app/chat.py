import sys
import os

# =========================
# FIX: project root path
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from tools.ask import ask

# =========================
# SIMPLE MEMORY SYSTEM
# =========================
context = {
    "last_question": None,
    "last_answer": None
}

def print_box(text):
    print("\n" + "=" * 40)
    print(text)
    print("=" * 40 + "\n")


def chat():
    print("🤖 NexBrain AI Chat System (Offline Mode)")
    print("Type 'exit' to quit\n")

    while True:
        user = input("You: ").strip()

        if user.lower() == "exit":
            print("Bye 👋")
            break

        # =========================
        # FOLLOW-UP HANDLING
        # =========================
        if user.lower() in ["আর বলো", "more", "details", "explain"]:
            if context["last_answer"]:
                print_box(context["last_answer"])
                continue

        # =========================
        # MAIN AI RESPONSE
        # =========================
        result = ask(user)

        if isinstance(result, dict):
            answer = f"{result['title']}\n\n{result['content']}\n\nScore: {result['score']}"
        else:
            answer = result

        # save memory
        context["last_question"] = user
        context["last_answer"] = answer

        print_box(answer)


if __name__ == "__main__":
    chat()
