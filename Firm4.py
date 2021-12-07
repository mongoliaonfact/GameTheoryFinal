# @author" bbaasan
# date: Nov 5, 2021
# Facilitated Game Theory
# bbaasan@gmu.edu

import random
import numpy as np


class Firm:

    def __init__(self, fid):
        self.id = 'F'+ str(fid)
        self.wage = random.randint(10, 15)
        self.ability = 0.2 # round(np.random.uniform(), 2)
        self.clients = []
        self.employees = []

    def __str__(self):
        return f'{self.id}, {self.wage},' \
               f'{self.ability}, {self.clients}, {self.employees}'.format(self=self)

