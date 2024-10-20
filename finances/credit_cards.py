"""
    Transform Data: Credits Cards
        Plots:
            Cut-off
            Payment
            Credit Score
"""
import pandas as pd
import plotly.express as px
from finances import finances_codes as fc

raw = pd.read_excel("data\\CreditCards.xlsx", sheet_name=None)

# General Info of Credit Cards.
raw_g = raw['General']
raw_g = raw_g.set_index("Name", drop=True)
### print(raw_g)

# Total amount of the Limit Credit
TOTAL_CREDIT = raw_g['Credit Limit'].sum()


# CREDIT CARDS
def list_cc():
    """
        Get a list of Credit Cards written in Finance App
    """
    H = "History "
    raw_sheets = list(raw.keys())
    credit_cards = []
    for k in raw_sheets:
        if k.startswith(H):
            credit_cards.append(k)
    return credit_cards
