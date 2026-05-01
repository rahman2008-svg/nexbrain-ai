def rewrite_answer(item, score):
    text = item["content"]

    if score > 15:
        return f"📘 বিস্তারিতভাবে বললে:\n{text}\n\n✅ এটা খুব নির্ভরযোগ্য তথ্য"
    elif score > 8:
        return f"📗 সহজভাবে:\n{text}\n\nℹ️ এটা ভালো ম্যাচ পাওয়া তথ্য"
    else:
        return f"📙 সংক্ষেপে:\n{text}\n\n⚠️ নিশ্চিততা কম"
