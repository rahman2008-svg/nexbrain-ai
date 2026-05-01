context = {
    "history": [],
    "last_query": None,
    "last_answer": None,
    "topic_stack": []
}


def save_context(query, answer):
    context["last_query"] = query
    context["last_answer"] = answer

    # topic tracking (simple intent memory)
    context["topic_stack"].append(query)

    context["history"].append({
        "q": query,
        "a": answer
    })

    if len(context["history"]) > 30:
        context["history"].pop(0)

    if len(context["topic_stack"]) > 10:
        context["topic_stack"].pop(0)


def get_context():
    return context
