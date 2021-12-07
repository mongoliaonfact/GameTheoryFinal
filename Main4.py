from Agent4 import Agent
from Market4 import Market
from Firm4 import Firm
from Client4 import Client
import random
import pandas as pd
import os
from collections import Counter
import matplotlib.pyplot as plt


def main():
    random.seed(1, version=100)
    num_agents = 1200
    num_firms = 15
    num_clients = 500

    market = Market()
    agents = market.make_players(Agent, num_agents)
    # print(market.agent_print(agents))
    firms = market.make_players(Firm, num_firms)
    clients = market.make_players(Client, num_clients)
    firm_agent = market.match_firm_agent(rounds=20, firm_dict=firms,
                                         agent_dict=agents)
    # pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    #firm_agent_df = market.market_print(firm_agent)
    """
    firm_agent_client = market.market_agent_perspective(num_week=3,
                                                        market_dict=firm_agent,
                                                        client_dict=clients)

    market_df = market.market_print(firm_agent_client)
    # print(market_df)
    # market_df.to_csv('market_df.csv', index=False)

    market_df.loc[:, 'emp_workdays'] = market_df.loc[:,
                                       'emp_workdays'].apply(lambda x: market.days_to_dict(x))

    emp_clients_len = market_df.loc[:, 'emp_clients'].apply(lambda x: len(x))
    market_df.insert(10, 'emp_clients_length', emp_clients_len)

    market_df.loc[:, 'emp_workdays_length'] = market_df.loc[:,
                                              'emp_workdays'].apply(lambda x: len(x.keys()))
    """
    def from_client_perspective(weeks=None, days=7, dict1 = None, dict2=None):
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

    client_perspective  = market.from_client_perspective(weeks=3, dict1=clients, dict2=firm_agent)

    client_perspective_frame = market.client_perspective_frame(client_perspective)


    return client_perspective_frame

if __name__ == '__main__':
    main()
