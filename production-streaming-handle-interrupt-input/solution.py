def handle_interrupt_input(current_task: str | None, new_input: str, interrupt_keywords: list[str]) -> str:
    """`current_task` is the description of whatever the agent is currently
    doing, or None if it's idle. Decide what to do with `new_input` (a
    message the user just sent):

    - If `new_input` contains any of `interrupt_keywords` (case-insensitive,
      as substrings), return "INTERRUPT_AND_SWITCH" -- the user wants to
      stop the current task and act on this instead, regardless of whether
      a task is running.
    - Otherwise, if there's no current task, return "START_NEW_TASK".
    - Otherwise, return "QUEUE_AFTER_CURRENT".
    """
    # TODO: implement
    pass
    keywords=[]
    for s in interrupt_keywords:
        keywords.append(s.lower())

    lowered=new_input.lower()
    for keyword in keywords:
        if keyword in lowered:
            return "INTERRUPT_AND_SWITCH"
    if current_task is None:
        return "START_NEW_TASK"
    
    return "QUEUE_AFTER_CURRENT"
