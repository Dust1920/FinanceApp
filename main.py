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
    finances_folder = {
        "CreditCards":"1Pqu-yUZ3VmWWnED6u6NjztRtWaNyy6Y-Ys1s2obDp-0",
        "Expenses":"1RjBA6vRcA8PaqLEV2WR1weNpBCBxtW9tZLFX3K33Puw",
        "I-FM":"1O-Ha-6n9THleh7bDlv4hoIQL5O0Y48Ho6cjR0Z7TvQY",
        "Income":"1VQOT2rkwS-CC7dI6X2BTNI3l9q2dcEW_XV8vRSx9sow",
        "Plans":"1e4UFj50CBnmFRN7MskgthuiLArYEpXMe2RmbY4ghcyM",
        "Portfoly": "1XfsUEtWTI_4EUeKqntFaHmb1KmaD4V9As2Xpqs5_Bpg"
    }

    # Folder Name to save the Finance Data.

    download.charge_finance_data(FOLDER_NAME,
                                finances_folder)

TEST = 1

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
