"""
    Transform Data: Credits Cards
        Plots:
            Cut-off
            Payment
            Credit Score
"""
import pandas as pd
import plotly.express as px

# Read Data (Credit Cards)
raw = pd.read_excel("data\\CreditCards.xlsx", sheet_name=None)

# General Info of Credit Cards.
raw_g = raw['General']
raw_g = raw_g.set_index("Name", drop=True)

# Total amount of the Limit Credit
TOTAL_CREDIT = raw_g['Credit Limit'].sum()

# Auxiliar Functions
def list_cc():
    """
        Get a list of Credit Cards written in Finance App
    """
    hist = "History "
    raw_sheets = list(raw.keys())
    credit_cards = []
    for k in raw_sheets:
        if k.startswith(hist):
            credit_cards.append(k)
    return credit_cards

def all_cc_df(col, **kwargs):
    """
    Generate a Cut Off Line Plot
    """
    cards = kwargs.get("cards","*")
    if cards == "*":
        cards = list_cc()
    name_cards = [x.split(" ")[1] for x in cards]
    cols = ["Cut","Payment","I-FM"]
    if not col in cols:
        return -1
    col_df = pd.DataFrame()
    for nc, cc in enumerate(cards):
        df = raw[cc]
        df['Date'] = df['Month'].transform(lambda x: str(x)[:3])
        df['Date'] += df['Year'].transform(lambda x: str(x)[2:])
        df.set_index('Date', inplace=True, drop=True)
        if nc == 0:
            col_df = pd.DataFrame(index = df.index, columns=name_cards)
        col_df.loc[:, name_cards[nc]] = df.loc[:,col]
    return col_df

def df_to_plotly_df(df: pd.DataFrame, col_tname, col_data, **kwargs):
    """
    Convert a Pandas DataFrame a DataFrame to Plot with Plotly. 
    """
    nx = len(df.index)
    sel_cols = kwargs.get("cols", df.columns)
    ny = len(sel_cols)
    result = pd.DataFrame(index = list(range(nx * ny)), columns=["Date", col_tname, col_data])
    i = 0
    for x in df.index:
        for y in sel_cols:
            result.loc[i, ["Date", col_tname, col_data]] = [x,y,df.loc[x,y]]
            i = i + 1
    return result

# Plot by value type. (Payment, Cut, I-FM)
PLOT_T = "I-FM"
CARD = "Card"
df_cut = all_cc_df(PLOT_T)
plot_cut = df_to_plotly_df(df_cut, CARD, PLOT_T)
fig_cut = px.line(plot_cut, x = "Date", y = PLOT_T,
                  color = CARD, title = PLOT_T)
fig_cut.show()

# Plot by Credit Card
CREDIT_CARD = "ORO"
oro = raw[f"History {CREDIT_CARD}"]
plot_oro = df_to_plotly_df(oro, "Amount","C", cols = ["Cut","Payment","I-FM"])
fig_card = px.line(plot_oro, x = "Date", y = "Cash", color="Amount")
fig_card.show()
print(plot_oro)
