from tools.search import search
from tools.best import best_answer

def ask(query):
    results = search(query)

    if not results:
        return "No data found"

    best, score = best_answer(results, query)

    return {
        "title": best["title"],
        "content": best["content"],
        "score": score
    }
