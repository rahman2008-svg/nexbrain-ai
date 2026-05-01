from core.engine import rank
from app.ui import print_box
from core.context import save_context


def chat(db, index):
    print("🤖 NexBrain AI Assistant (FINAL EVOLUTION)\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        item, score = rank(user, db, index)

        answer = f"{item['title']}\n\n{item['content']}\n\nConfidence Score: {score}"

        save_context(user, answer)

        print_box(answer)
