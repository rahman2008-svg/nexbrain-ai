def refine(item, score):
    text = item["content"]

    if score > 15:
        return f"📘 বিস্তারিতভাবে:\n{text}\n\n✅ এটা খুব নির্ভরযোগ্য তথ্য"
    elif score > 8:
        return f"📗 সহজভাবে:\n{text}"
    else:
        return f"📙 সংক্ষেপে:\n{text}"
