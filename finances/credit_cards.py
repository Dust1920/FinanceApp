"""
    Transform Data: Credits Cards
        Plots:
            Cut-off
            Payment
            Credit Score
"""
import pandas as pd
import plotly.express as px


raw = pd.read_excel("data\\CreditCards.xlsx", sheet_name=None)

# General Info of Credit Cards.
raw_g = raw['General']
raw_g = raw_g.set_index("Name", drop=True)

# Total amount of the Limit Credit
TOTAL_CREDIT = raw_g['Credit Limit'].sum()

# Auxiliar Functions
def list_cc(df):
    """
        Get a list of Credit Cards written in Finance App
    """
    hist = "History "
    raw_sheets = list(df.keys())
    credit_cards = []
    for k in raw_sheets:
        if k.startswith(hist):
            credit_cards.append(k)
    return credit_cards
