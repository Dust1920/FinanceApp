"""
    Finance App
"""
import os

# DashBoard
from dash import Dash
from dash import html, dcc, Input, Output


# Load Data
FOLDER_NAME = "data"
if not os.path.exists(FOLDER_NAME):
    os.mkdir(FOLDER_NAME)
    from GD import download

    # Google Sheets of FinanceApp
    from data import x
    finances_folder = x.finances_folder
    # Folder Name to save the Finance Data.

    download.charge_finance_data(FOLDER_NAME,
                                finances_folder)

TEST = 0

if TEST:
    from finances import credit_cards as cc
    print(cc.TOTAL_CREDIT)




# Create DashBoard

DASHBOARD = 0
if DASHBOARD:

    app = Dash(__name__)
    app.title = "Finanzas Personales"

    app.layout = html.Div()


    if __name__ == "__main__":
        app.run(debug=True)
