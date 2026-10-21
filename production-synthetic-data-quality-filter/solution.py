def filter_quality(examples: list[str], min_length: int, banned_phrases: list[str]) -> list[str]:
    """Keep only examples that are at least `min_length` characters long AND
    contain none of `banned_phrases` (case-insensitive substring match).
    Return the kept examples in their original order.
    """
    # TODO: implement
    pass
    kept=[]
    for i in range(len(examples)):
        if len(examples[i]) < min_length or any(banned.lower() in examples[i].lower() for banned in banned_phrases):
            continue
        kept.append(examples[i])

    return kept
