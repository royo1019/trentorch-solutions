def simulate_self_play(
    agent_a_moves: list[str], agent_b_moves: list[str], max_turns: int
) -> list[tuple[str, str]]:
    """Simulate two agents, "A" and "B", alternating turns starting with A.
    `agent_a_moves` and `agent_b_moves` are each agent's pre-scripted moves,
    used in order as that agent gets its turns. Build a transcript of
    (agent_name, move) pairs, one per turn, for up to `max_turns` turns --
    but stop early the moment the agent whose turn it is has no more moves
    left to use.
    """
    # TODO: implement
    pass
    result=[]
    for turn in range(max_turns):
        agent_a = turn % 2 == 0
        moves = agent_a_moves if agent_a else agent_b_moves
        move_index = turn // 2
        if move_index >=len(moves):
            break
        agent_name = "A" if agent_a else "B"
        result.append((agent_name,moves[move_index]))

    return result
