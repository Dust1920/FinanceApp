"""
    Transform Data: Credits Cards
"""
import pandas as pd
import plotly.express as px

raw = pd.read_excel("data\\CreditCards.xlsx", sheet_name=None)

# General Info of Credit Cards.
raw_g = raw['General']
raw_g = raw_g.set_index("Name", drop=True)
print(raw_g)

def get_cutoff(card):
    """
    Given Credit Card get
    the cut off date. 
    """
    return raw_g.loc[card, 'Cut-off']

# Total amount of the Limit Credit
TOTAL_CREDIT = raw_g['Credit Limit'].sum()
