import numpy as np

class MultiArmedBandit:

    def __init__(self, no_plays, no_arms):
        self.no_plays = no_plays
        self.no_arms = no_arms
        self.total_reward = 0
        actual_arm_scores = []
        for arm in range(self.no_arms):
            arm_score = np.random.randint(5, 10)
            actual_arm_scores.append(arm_score)

    def play(self):
        for round in range(self.no_plays):






