bad_answers = set()

def mark_bad(item_id):
    bad_answers.add(item_id)

def is_bad(item_id):
    return item_id in bad_answers
