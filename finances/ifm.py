"""
    Transform Data: Interest Free Monthly
        
"""
import pandas as pd
import plotly.express as px
pd.options.mode.copy_on_write = True

i_fm = pd.read_excel("data\\I-FM.xlsx")


YEARS = list(i_fm['Year'].unique())
MONTHS = list(i_fm['Month'].unique())
CATEGORY = list(i_fm['Category'].unique())
SUBCATEGORY = list(i_fm['Subcategory'].unique())


def msi_format(**kwargs):
    """
    Create IFM database
    """
    year = kwargs.get("y",None)
    month = kwargs.get("m", None)
    i_fmy = i_fm.copy()
    if not pd.isnull(year):
        i_fmy = i_fm[i_fm['Year'] == year]
    if not pd.isnull(month):
        i_fmy = i_fmy[i_fmy['Month'] == month]
    i_fmy.dropna(how = "all", axis = 1, inplace = True)
    return i_fmy

# print(i_fmy)

def msi_plots(df):
    """
    Create IFM Plots. 
    """
    sifm = df[['Day', 'Month', 'Year', 'Category', 'Subcategory',
                'Concept', 'Total', 'Level', 'Credit Card']]

    ifcounter = df[[x + 1 for x in range(len(df.columns) - len(sifm.columns))]]
    # print(ifcounter)

    sifm['Meses Cubiertos'] = ifcounter.sum(axis = 1)
    sifm['Meses Totales'] = len(ifcounter.columns) - ifcounter.isna().sum(axis = 1)
    sifm['Progreso'] = sifm['Meses Cubiertos'] / sifm['Meses Totales'] * 100

    for x in sifm.index:
        total = sifm.loc[x, 'Total']
        progress = sifm.loc[x, 'Progreso']
        sifm.loc[x, 'Monto Cubierto'] = total if progress == 100 else progress * total / 100

    df_o = pd.DataFrame(index = ['Cubierto','Restante'], columns=['Monto'])
    df_o['Monto'] = 0
    df_o.loc['Cubierto'] = sifm['Monto Cubierto'].sum()
    df_o.loc['Restante'] = sifm['Total'].sum() - sifm['Monto Cubierto'].sum()
    return df_o

y0 = YEARS[0]
m0 = MONTHS[0]

ifm_f = msi_format()

df_pgs = msi_plots(ifm_f)
fig_msi = px.pie(df_pgs, names= df_pgs.index, values= 'Monto',
                title = f"IFM {m0},{y0}", hole = 0.7)
fig_msi.show()
