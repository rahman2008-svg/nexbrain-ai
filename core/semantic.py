from core.utils import tokenize

def semantic_score(q_tokens, text_tokens):
    score = 0

    for q in q_tokens:
        for t in text_tokens:
            if q in t or t in q:
                score += 0.5

    return score
