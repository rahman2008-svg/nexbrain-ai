# core/feedback.py

feedback_score = {}

def update_feedback(item_id, value):
    if item_id not in feedback_score:
        feedback_score[item_id] = 0

    feedback_score[item_id] += value


def get_feedback(item_id):
    return feedback_score.get(item_id, 0)
