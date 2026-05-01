# core/generator.py

import random

def generate_answer(item, score, context=None):
    base = item["content"]

    styles = [
        f"{item['title']} সম্পর্কে বললে: {base}",
        f"সহজভাবে বললে, {base}",
        f"তুমি যে বিষয়টা জানতে চেয়েছো, সেটা হলো: {base}",
    ]

    answer = random.choice(styles)

    # confidence tone
    if score > 8:
        answer += "\n✅ এটা খুব নির্ভরযোগ্য তথ্য"
    elif score > 4:
        answer += "\nℹ️ এই তথ্যটি সম্ভাব্যভাবে সঠিক"
    else:
        answer += "\n⚠️ পুরোপুরি নিশ্চিত না"

    # context add
    if context and context == item["title"]:
        answer += "\n🔁 তুমি আগেও এই বিষয় নিয়ে প্রশ্ন করেছিলে"

    return answer
