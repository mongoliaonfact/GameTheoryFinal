# @author: bbaasan
# Game Theory
# date: Dec, 18, 2021

import random
from collections import defaultdict


class Agent:

    def __init__(self, aid):
        self.aid = 'A'+str(aid)
        self.awage = random.randint(7,9)
        self.askill = self.make_choice
        self.askill_rate = round(random.random(), 2)
        self.aworkday = self.get_workday
        self.aclients = list()

    @property
    def make_choice(self):
        return random.randint(1, 4)

    @property
    def get_workday(self):
        ref = defaultdict(list)
        month = range(1, 29)
        n = random.choice(month)
        workdays = sorted(random.sample(month, n))
        for day in [str(w) for w in workdays]:
            ref[day] = []
        return ref

    def __str__(self):
        return f'{self.aid}, {self.awage}, {self.askill}, ' \
               f'{self.askill_rate}, {self.aworkday}, ' \
               f'{self.aclients}'.format(self=self)
