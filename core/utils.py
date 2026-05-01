# core/utils.py

def clean_text(text):
    return text.lower().strip()

def tokenize(text):
    return clean_text(text).split()

# --- NEW: Levenshtein distance (pure python) ---
def levenshtein(a, b):
    la, lb = len(a), len(b)
    if la == 0: return lb
    if lb == 0: return la

    dp = list(range(lb + 1))
    for i in range(1, la + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, lb + 1):
            cur = dp[j]
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[j] = min(
                dp[j] + 1,      # deletion
                dp[j-1] + 1,    # insertion
                prev + cost     # substitution
            )
            prev = cur
    return dp[lb]

def similarity(a, b):
    # 0..1 (1 মানে একদম মিল)
    dist = levenshtein(a, b)
    m = max(len(a), len(b))
    if m == 0:
        return 1.0
    return 1.0 - (dist / m)
