import numpy as np

class MultiArmedBandit:

    def __init__(self, no_plays, no_arms):
        self.no_plays = no_plays
        self.no_arms = no_arms
        self.total_reward = 0

