import pandas as pd
import matplotlib.pyplot as plt
import plotnine
from Main4 import main
from plotnine import *
from collections import Counter

#pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
market_market = main()


# print(market_market.columns)
def relationship_len_of_wordays_responds_num_of_clients(df=None):
    # following will produce a graph that contains x=employee workdays and
    # resposne y=number of clients for that employee and
    # colored by employee wage

    # notice: increasing number of firms decreases the number of clients
    # that each employee can have, which is expected that the code is
    # suppose to do

    gg_by_wage = (
            ggplot(market_market, aes(x='emp_workdays_length', y='emp_clients_length',
                                      color='emp_wage'))
            + geom_point(alpha=1)
            + ggtitle('Relationship between Emp Num of Days to Work vs. Number of Clients')
    )

    return gg_by_wage


# relationship_len_of_wordays_responds_num_of_clients(market_market)

# print(market_market.plot())
# plt.show()

client_perspective = main()


def get_xy(df=None):
    x = []
    y = []
    for ind, row in enumerate(df.client_request):
        for each in row:
            firm = each[0]
            agent = each[1]
            x.append(firm)
            y.append(agent)
    x_df = pd.DataFrame.from_dict(Counter(x), orient='index')
    y_df = pd.DataFrame.from_dict(Counter(y), orient='index')
    return x_df, y_df

client_firm_df = get_xy(client_perspective)[0]
client_agent_df = get_xy(client_perspective)[1]
print(client_firm_df.plot())
print(client_agent_df.plot())
plt.show()
