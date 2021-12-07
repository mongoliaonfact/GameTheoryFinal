# @author: bbaasan
# Facilitated Game Theory
# Nov 25, 2021
# bbaasan@gmu.edu
import pandas as pd
import random
from Agent2 import Agent
from Firm2 import Firm
from Client import Client


class Market:

    def __init__(self):
        pass

    def make_players(self, cls, num_players):
        players_dict = {}
        for player_id in range(num_players):
            an_agent = cls(player_id)
            players_dict[player_id] = an_agent
        return players_dict

    def match_firm_agent(self, rounds=10, firm_dict=None,
                         agent_dict=None):

        # matching agents and firms
        for a_round in range(rounds):
            for each_firm_id in firm_dict:
                try:
                    nth_firm = firm_dict[each_firm_id]
                    rnd_agent_key = random.choice(list(agent_dict.keys()))
                    # agent attributes
                    agent_wage = agent_dict[rnd_agent_key].wage
                    agent_skill = agent_dict[rnd_agent_key].skill_rate
                    # firm attritbure
                    firm_wage = nth_firm.wage
                    firm_ability = nth_firm.ability
                    # print(firm_wage, agent_wage, firm_ability, agent_skill)

                    # conditions that each firm and agent to meet are:
                    if agent_wage < firm_wage and agent_skill >= firm_ability:
                        nth_firm.employees.append(agent_dict[rnd_agent_key])
                        agent_dict.pop(rnd_agent_key)

                except KeyError:
                    pass
        return firm_dict

    def firm_print(self, dict1):
        # firm attributes
        id = []
        wage = []
        ability = []
        clients = []
        employees = []

        # agent attributes
        emp_id = []
        emp_wage = []
        emp_ability = []
        emp_skill_rate = []
        emp_client = []
        emp_workdays = []

        for i in dict1:
            firm = dict1[i]
            for j in firm.employees:
                id.append(firm.id)
                wage.append(firm.wage)
                ability.append(firm.ability)
                clients.append(None)
                employees.append(j.id)
                emp_id.append(j.id)
                emp_wage.append(j.wage)
                emp_ability.append(j.ability)
                emp_skill_rate.append(j.skill_rate)
                emp_client.append(None)
                emp_workdays.append(j.work_days)

        frame = {
            'firm_id': id,
            'firm_wage': wage,
            'firm_ability': ability,
            'firm_clients': clients,
            'employees': employees,
            'emp_id': emp_id,
            'emp_wage': emp_wage,
            'emp_ability': emp_ability,
            'emp_skill_rate': emp_skill_rate,
            'emp_client': emp_client,
            'emp_workdays': emp_workdays
        }
        return pd.DataFrame(frame)


    def agent_print(self, dict1):
        id = []
        wage = []
        ability = []
        skill = []
        clients = []
        workdays = []

        for i in dict1:
            agent = dict1[i]
            id.append(agent.id)
            wage.append(agent.wage)
            ability.append(agent.ability)
            skill.append(agent.skill_rate)
            clients.append(agent.clients)
            workdays.append(agent.work_days)

        frame = {
            'id': id,
            'wage': wage,
            'ability': ability,
            'skill_rate': skill,
            'clients': clients,
            'work_days': workdays
        }
        return pd.DataFrame(frame)

    def market_agent_perspective(self, num_week = 3,
                                 market_dict=None, client_dict=None):
        ''''
        Method param:
        1. num_week: number of weeks. Default = 3
        2. market_dict: dictionary of market Agent and Firm
        3. client_dict:  dictionary of Client
        '''
        # loop over num of week
        for nth_week in range(num_week):
            # 7 days for a week
            for nth_day in range(7):
                # print(nth_week, nth_day)
                    for firm_key in market_dict:
                        a_firm = market_dict[firm_key]
                        # print(a_firm)
                        for emp in a_firm.employees:

                            if nth_day in emp.work_days:
                                firm_id = market_dict[firm_key]
                                # if nth_week == num_week and nth_day
                                try:
                                    client_list = random.sample(client_dict.keys(), k=5)
                                    client1_id, client2_id, client3_id, client4_id, client5_id = client_list
                                    # print(nth_week, nth_day, firm_id, emp)
                                    client1 = client_dict[client1_id]
                                    # print('client1: ', client1)
                                    client2 = client_dict[client2_id]
                                    # print('client2: ', client2)
                                    client3 = client_dict[client3_id]
                                    # print('client3: ', client3)
                                    client4 = client_dict[client4_id]
                                    # print('client4: ', client4)
                                    client5 = client_dict[client5_id]
                                    # print('client5: ', client5)
                                    # client 1
                                    if emp.skill_rate >= client1.preference:
                                        emp.clients.append(client1_id)
                                        client_dict.pop(client1_id, None)
                                    # client 2
                                    if emp.skill_rate >= client2.preference:
                                        emp.clients.append(client2_id)
                                        client_dict.pop(client2_id, None)
                                    # client 3
                                    if emp.skill_rate >= client3.preference:
                                        emp.clients.append(client3_id)
                                        client_dict.pop(client3_id, None)
                                    # client 4
                                    if emp.skill_rate >= client4.preference:
                                        emp.clients.append(client4_id)
                                        client_dict.pop(client4_id, None)
                                    # client 5
                                    if emp.skill_rate >= client5.preference:
                                        emp.clients.append(client5_id)
                                        client_dict.pop(client5_id, None)
                                except ValueError:
                                    pass
                            else:
                                pass

        return market_dict

    def market_print(self, market_dict_to_print = None):
        # firm attributes
        firm_id = []
        firm_wage = []
        firm_skill = []
        firm_clients = []
        firm_employees = []

        # agent attributes
        emp_id = []
        emp_wage = []
        emp_ability = []
        emp_skill_rate = []
        emp_client = []
        emp_workdays = []

        for each_firm in market_dict_to_print:
            a_firm = market_dict_to_print[each_firm]
            for  each_worker in a_firm.employees:
                firm_id.append(a_firm.id)
                firm_wage.append(a_firm.wage)
                firm_skill.append(a_firm.ability)
                firm_clients.append(a_firm.clients)
                firm_employees.append(each_worker.id)
                emp_id.append(each_worker.id)
                emp_wage.append(each_worker.wage)
                emp_ability.append(each_worker.ability)
                emp_skill_rate.append(each_worker.skill_rate)
                emp_client.append(each_worker.clients)
                emp_workdays.append(each_worker.work_days)
        frame = {
            'firm_id': firm_id,
            'firm_wage':firm_wage,
            'firm_ability':firm_skill,
            'firm_clients': firm_clients,
            'firm_employees':firm_employees,
            'emp_id':emp_id,
            'emp_wage':emp_wage,
            'emp_ability':emp_ability,
            'emp_skill_rate':emp_skill_rate,
            'emp_clients':emp_client,
            'emp_workdays':emp_workdays
        }

        return pd.DataFrame(frame)
    """
    def agents_days(self, agents_dict=None, num_work_days = 30):
        days_ = []
        agent_id_ = []
        agent_wage_ = []
        agent_ability_ = []
        agent_skill_rate_ = []
        agent_clients_ = []
        agent_workdays_ = []
        agent_daily_ = []

        for day in range(num_work_days):
            for agent_key in agents_dict:
                an_agent = agents_dict[agent_key]
                # print(day, an_agent.work_days)
                days_.append(day)
                agent_id_.append(an_agent.id)
                agent_wage_.append(an_agent.wage)
                agent_ability_.append(an_agent.ability)
                agent_skill_rate_.append(an_agent.skill_rate)
                agent_clients_.append(an_agent.clients)
                agent_workdays_.append(an_agent.work_days)
                agent_daily_.append(an_agent.daily_clients)
        frame = {
            'days':days_,
            'agent_id':agent_id_,
            'agent_wage':agent_wage_,
            'agent_ability':agent_ability_,
            'agent_skill_rate':agent_skill_rate_,
            'agent_clients':agent_clients_,
            'agent_workdays':agent_workdays_,
            'agent_daily':agent_daily_
        }
        return pd.DataFrame(frame)
    """

    def days_to_dict(self, x):
        dict1 = {}

        for day in x:
            dict1[day] = []
        return dict1

    def from_client_perspective(self, weeks=None, days=7, dict1 = None, dict2=None):
        # weeks = 2
        # days = 7
        # print(market_df.columns)
        ref = {}
        for week in range(weeks):
            for day in range(days):
                for client_key in dict1:
                    a_client = dict1[client_key]
                    compatible_emp_list = []
                    try:
                        if day in a_client.weekdays:
                            firm_key = random.choice(list(dict2.keys()))
                            a_firm = dict2[firm_key]
                            for emp in a_firm.employees:
                                try:
                                    # compatible_emp_list = {}
                                    if a_client.ability == emp.ability and \
                                            a_client.preference >= emp.skill_rate:
                                        compatible_emp_list.append((a_client.id, a_firm.id, emp.id))

                                except ValueError:
                                    print(ValueError)
                    except ValueError:
                        pass
                    if len(compatible_emp_list) == 0:
                        pass
                    else:
                        # print('outer', compatible_emp_list)
                        # print('rnd choice', random.choice(compatible_emp_list))
                        rnd_choice = random.choice(compatible_emp_list)
                        a_client.request.append((rnd_choice[1], rnd_choice[2]))
                        ref[a_client.id] = a_client # .id, a_client.request)# , compatible_emp_list)
                        # ref[week] = {day: a_client}
        return ref

    def client_perspective_frame(self, dict = None):
        id=[]
        pay=[]
        preference=[]
        ability=[]
        weekdays=[]
        agents=[]
        for i in dict:
            client = dict[i]
            id.append(client.id)
            pay.append(client.pay)
            preference.append(client.preference)
            ability.append(client.ability)
            weekdays.append(client.weekdays)
            agents.append(client.request)

        frame = pd.DataFrame({
            'client_id':id,
            'client_pay':pay,
            'client_preference': preference,
            'client_ability':ability,
            'client_weekdays':weekdays,
            'client_request': agents
        })
        return frame