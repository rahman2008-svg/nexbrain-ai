def best_answer(results, query):
    query = query.lower()

    best = None
    best_score = 0

    for item in results:
        score = 0

        text = (item["title"] + " " + item["content"]).lower()

        for word in query.split():
            if word in text:
                score += 1

        if score > best_score:
            best_score = score
            best = item

    return best, best_score
