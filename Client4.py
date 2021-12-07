# @author: bbaasan
# Date: Nov 5, 2021
# Facilitated Game Theory
# bbaasan@gmu.edu

import random
import numpy as np


class Client:

    def __init__(self, cid):
        self.id = 'C'+str(cid)
        self.pay = random.randint(20, 25)
        self.preference = round(np.random.uniform(), 2)
        self.ability = self.make_choice
        self.weekdays = self.get_service_days
        self.request = []

    @property
    def get_service_days(self):
        work_day = random.randint(1, 2)
        weekdays = sorted(random.sample(range(7), k=work_day))
        return weekdays

    def check_ability(self, emp=None):
        # first check the client ability
        if self.preference <= emp.skill_rate:
            self.request.append(emp.id)

    @property
    def make_choice(self):
        choice = random.choice(['1', '2', '3', '4'])
        return choice

    def __str__(self):
        return f'{self.id}, {self.pay}, {self.preference}, {self.ability},' \
               f' {self.request}, {self.weekdays}'.format(self=self)
