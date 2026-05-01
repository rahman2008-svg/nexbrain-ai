from core.utils import tokenize

def vectorize(text):
    """
    Simple character + word hybrid vector (no numpy)
    """
    tokens = tokenize(text)

    vec = {}

    for t in tokens:
        for ch in t:
            vec[ch] = vec.get(ch, 0) + 1

    return vec


def cosine_like(v1, v2):
    """
    simplified similarity score (no math lib)
    """
    common = 0
    total = 0

    for k in v1:
        total += v1[k]
        if k in v2:
            common += min(v1[k], v2[k])

    if total == 0:
        return 0

    return common / total
