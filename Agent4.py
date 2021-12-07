# @author" bbaasan
# date: Nov 5, 2021
# Facilitated Game Theory
# bbaasan@gmu.edu

import random
import string
import numpy as np


class Agent:

    def __init__(self, aid):
        self.id = 'A'+str(aid)
        self.wage = self.create_wage
        self.ability = self.make_choice
        self.skill_rate = round(np.random.uniform(), 2)
        self.clients = []
        self.work_days = self.make_work_days

    @property
    def make_work_days(self):
        week = range(7)
        work_day = random.randint(1, 7)
        workdays = sorted(random.sample(week, k=work_day))
        return workdays

    @property
    def make_choice(self):
        choice = random.choice(['1', '2', '3', '4'])
        return choice

    def make_dict(self, x):
        dict1 = {}
        for day in x:
            dict1[day] = []
        return dict1

    @property
    def create_wage(self):
        wage = random.randint(7, 9)
        return wage

    def __str__(self):
        return f'{self.id}, {self.wage}, {self.ability}, {self.skill_rate}, ' \
               f' {self.clients}, {self.work_days}'.format(self=self)
