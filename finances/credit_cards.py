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
    cols = ["Cut","Payment","I-FM", "Credit Limit"]
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
    print(sel_cols)
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

def plot_cards(y, year, color = "Card"):
    """
        Plot by value type (Payment, Cut, I-FM)
    """

    plot_names = {
        "I-FM":"Interest Free Months",
        "Cut": "Balance Cut",
        "Payment": "Payment (avoid interests)"
    }

    df = all_cc_df(y)
    plot = df_to_plotly_df(df, color, y)
    plot = plot[plot['Date'].str.endswith(year)]
    print(plot)
    fig = px.line(plot, x = "Date", y = y,
                    color = color, title = plot_names[y])
    return fig
# fig_cut.show()

# Plot by Credit Card
CREDIT_CARD = "ORO"
oro = raw[f"History {CREDIT_CARD}"]
plot_oro = df_to_plotly_df(oro, "Amount","Cash", cols = ["Cut","Payment","I-FM", "Credit Limit"])
fig_card = px.line(plot_oro, x= "Date", y= "Cash", color= "Amount")







# fig_card.show()

# Credit Score by Card
PLOT_T = "Credit Limit"
CARD = "Card"
df_cl = all_cc_df(PLOT_T)
plot_cl = df_to_plotly_df(df_cl, CARD, PLOT_T)

PLOT_T = "Cut"
CARD = "Card"
df_cut = all_cc_df(PLOT_T)
plot_cut = df_to_plotly_df(df_cut, CARD, PLOT_T)

plot_score = plot_cut.copy()
plot_score['Credit Use'] = plot_score['Cut'] / plot_cl['Credit Limit'] * 100
plot_score['Credit Use'] = plot_score['Credit Use'].transform(lambda x: round(x,2))

fig_cu = px.line(plot_score, x = "Date", y = "Credit Use", color = "Card")
# fig_cu.show()

# Credit Use Genral
g_cl = pd.DataFrame(plot_cl.groupby('Date', sort=False)['Credit Limit'].sum())
g_cut = pd.DataFrame(plot_cut.groupby('Date', sort=False)['Cut'].sum())


def cu_op(x,y):
    """
        Operator to calculate the credit use. 
    """
    u = 0
    if y != 0:
        u = x / y
    return u

g_cu = g_cut.copy()
for gi in g_cu.index:
    credit_use = cu_op(g_cu.loc[gi, 'Cut'], g_cl.loc[gi, 'Credit Limit'])
    g_cu.loc[gi, 'Credit Use'] =  round(credit_use * 100, 2)

plot_gcu = px.line(g_cu, x = g_cu.index, y = "Credit Use")
print(g_cu)
