import numpy as np
import random

class eps_greedy:

    def __init__(self, no_arms, eps, no_turns):
        self.no_arms = no_arms
        self.eps = eps
        self.no_turns = no_turns
        self.distribution_centers = []
        self.distribution_sds = []
        self.total_reward = 0
        self.max_total_reward = 0
        for i in range(no_arms):
            self.distribution_centers.append(random.randint(10, 100))
            self.distribution_sds.append(random.randint(10, 20))

    def play(self):
        for turn in range(self.no_turns):
            turn_rewards = []
            for arm in range(self.no_arms):
                turn_rewards.append(random.normal(self.distribution_centers[arm],
                                                  self.distribution_sds[arm]))
