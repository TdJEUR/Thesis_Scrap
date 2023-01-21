def practice(no_arms, eps, no_turns):
    for turn in range(no_turns):
        turn_rewards = []
        for arm in range(no_arms):
            turn_rewards.append(random.normal(distribution_centers[arm],
                                              distribution_sds[arm]))