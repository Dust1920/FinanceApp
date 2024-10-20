"""
    Finance Codes 
"""
import pandas as pd


def get_cutoff(card, df):
    """
    Given Credit Card get
    the cut off date. 
    """
    return df.loc[card, 'Cut-off']


def adjust_na(df):
    """
        Check and delete excedent rows
    """
    df['Check'] = [1 if not pd.isna(x) else 0 for x in df['I-FM']]
    df_check = df[df['Check'] == 1]
    df_check = df_check.drop(columns=['Check'])
    return df_check


def creditcard(df) -> dict:
    """
    Get keys of a credit card
    """
    cc = {
        "YEARS":list(df['Year'].unique()),
        "MONTH":list(df['Month'].unique()),
    }
    return cc


def create_ccplot(df):
    """
        Transform Credit Card Dataframe to plot in plotly.
    """
    df = adjust_na(df)
    df['Date'] = df['Month'].transform(lambda x: x[:3]) + df['Year'].transform(lambda x: str(x)[2:])
    return df
