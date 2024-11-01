"""
    Transform Data: Expenses
        - 

"""

import pandas as pd
import plotly.express as px


raw = pd.read_excel("data\\Expenses.xlsx", sheet_name=None)
expenses = raw['E1']
# print(expenses)
YEARS = list(expenses['Year'].unique())
MONTHS = list(expenses['Month'].unique())
CATS = list(expenses['Category'].unique())
SCATS = list(expenses['SubCategory'].unique())
CARDS = list(expenses['Credit Card'].unique())
SECTOR = list(expenses['Sector'].unique())
LEVEL = list(expenses['Level'].unique())


def fyear(year):
    """
        Filter df by year
    """
    exp_y = expenses[expenses['Year'] == year]
    return exp_y


def fyearmonth(year, month):
    """
        Filter df for year and month
    """
    exp_y = fyear(year)
    exp_s = exp_y[exp_y['Month'] == month]
    return exp_s

tyear = YEARS[0]
tmonth = MONTHS[0]
exp_ym = fyearmonth(tyear, tmonth)
# print(exp_ym)


PLOT_N = ['Category', 'SubCategory', 'Concept','Credit Card', 'Sector', 'Level']
PLOT_V =  'Amount'

# Plots
for name in PLOT_N:
    fig = px.pie(exp_ym, names = name, values=PLOT_V, title= name)
    fig.show()
