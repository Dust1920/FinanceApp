"""
    Download Data in Google Drive
"""

import sys
import os
import requests


def get_google_sheet(spreadsheet_id, outdir, outfile):
    """
        Download Google Sheets Files 
    """
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=xlsx'
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        filepath = os.path.join(outdir, outfile)
        with open(filepath, 'wb') as fs:
            fs.write(response.content)
            print(f'CSV file saved to: {filepath}')
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')
        sys.exit(1)


##############################################


def charge_finance_data(folder_name, finances_sheets):
    """
      Load Finance Data by Finance App
    """
    for f in finances_sheets.items():
        get_google_sheet(f[1], folder_name, f"{f[0]}.xlsx")
    sys.exit(0) ## success
