memory = {
    "bad": set(),
    "good": set()
}


def mark_good(item_id):
    memory["good"].add(item_id)


def mark_bad(item_id):
    memory["bad"].add(item_id)


def is_bad(item_id):
    return item_id in memory["bad"]
