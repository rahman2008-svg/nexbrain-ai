from core.utils import tokenize
from core.indexer import search_index
from core.semantic import semantic_score
from core.vector import vectorize, cosine_like
from core.cache import get_cache, set_cache
from core.memory import is_bad
from core.context import get_context
from core.fallback import fallback_response
from core.intent import is_followup


def title_boost(q_tokens, title_tokens):
    score = 0
    for q in q_tokens:
        if q in title_tokens:
            score += 5
    return score


def tag_score(q_tokens, tags):
    score = 0
    for q in q_tokens:
        for t in tags:
            if q in t:
                score += 3
    return score


def rank(query, db, index):

    # ⚡ CACHE
    cached = get_cache(query)
    if cached:
        return cached

    ctx = get_context()

    # 🧠 FOLLOW-UP HANDLING
    if is_followup(query):
        if ctx["last_answer"]:
            return ({"title": "Context Reply", "content": ctx["last_answer"], "tags": []}, 20)

    q_tokens = tokenize(query)
    q_vec = vectorize(query)

    candidates = search_index(query, db, index)

    best_item = None
    best_score = 0

    for i in candidates:
        item = db[i]

        if is_bad(item["id"]):
            continue

        full_text = item["title"] + " " + item["content"] + " " + " ".join(item["tags"])
        tokens = tokenize(full_text)
        vec = vectorize(full_text)

        score = 0

        for w in q_tokens:
            if w in tokens:
                score += 2

        score += semantic_score(q_tokens, tokens)
        score += cosine_like(q_vec, vec) * 5
        score += tag_score(q_tokens, item["tags"])
        score += title_boost(q_tokens, tokenize(item["title"]))

        if score > best_score:
            best_score = score
            best_item = item

    if best_item is None:
        return fallback_response(query), 1

    result = (best_item, best_score)

    set_cache(query, result)

    return result
