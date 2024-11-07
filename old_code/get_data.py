"""
    Dashboard
"""

import os

# Load Data
FOLDER_NAME = "data"
REFRESH = 1

if REFRESH or not os.path.exists(FOLDER_NAME):
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)
    from GD import download

    # Google Sheets of FinanceApp
    from data import x
    finances_folder = x.finances_folder

    # Folder Name to save the Finance Data.
    download.charge_finance_data(FOLDER_NAME, finances_folder)
