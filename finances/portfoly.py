"""
    Transform Data: Portfoly
"""
import pandas as pd
import plotly.express as px

# Read Portfoly Data
raw = pd.read_excel("data\\Portfoly.xlsx", sheet_name=None)
res = raw['Resumen']  # Percentages
reg = raw['Registro']  # Actives

res = res.set_index('Sección', drop=True)
reg = reg.set_index('Simbolo', drop=True)

TOTAL_PORTFOLY = reg['Precio Actual'].sum()
## Portfoly Distribution
def distribution(dr = res, ds = reg):
    """
        Plot the Portfoly Distribution.
    """
    # Total Portfoly Value
    total = ds['Precio Actual'].sum()
    port_dist = px.pie(dr, names=dr.index, values="Actual (%)", hole=0.7)
    port_dist.update_layout(margin = {"t":50, "l":20, "r":0, "b":0},
                            annotations=[{
                            "text":f"Valor Portafolio<br>${round(total, 2):,} MXN",
                            "x":0.5, "y":0.5, "font_size":20, "showarrow":False}])
    return port_dist

res['Diferencia'] = (res['Objetivo (%)'] - res['Actual (%)']) * TOTAL_PORTFOLY
print(res)



def difference_goal_actual(new_inversion, d_b = res):
    """
    Calculate the money difference between the actual inversion and 
    """
    for s_i in d_b.index:
        actives_w_s = reg[reg['Parte en Portafolio'] == s_i]
        if len(actives_w_s) > 0:
            active_t = actives_w_s['Precio Actual'].sum()
            obj_amo = (TOTAL_PORTFOLY + new_inversion) * d_b.loc[s_i, 'Objetivo (%)']
            print(new_inversion)
            d_b.loc[s_i,'Diferencia'] = obj_amo - active_t
        else:
            d_b.loc[s_i,'Diferencia'] = 0
    return d_b




def portfoly_df(amount, d_b = res):
    """
        Create a Portfoly Table
    """
    d_b = difference_goal_actual(amount, d_b)
    db_table = d_b.copy()
    db_table['Actual (%)'] = db_table['Actual (%)'].transform(lambda x: f"{round(x,2) * 100}%")
    db_table['Objetivo (%)'] = db_table['Objetivo (%)'].transform(lambda x: f"{round(x,2) * 100}%")
    db_table['Diferencia'] = db_table['Diferencia'].transform(lambda x: f"{round(x,2)}")    
    return db_table


s = pd.DataFrame()
## Portfoly Table
res_table = res.copy()
res_table['Actual (%)'] = res_table['Actual (%)'].transform(lambda x: f"{round(x,2) * 100}%")
res_table['Objetivo (%)'] = res_table['Objetivo (%)'].transform(lambda x: f"{round(x,2) * 100}%")
res_table['Diferencia'] = res_table['Diferencia'].transform(lambda x: f"{round(x,2)}")












"""
NEW_INVERSION = 500

#print(reg.columns)

# Calculate the Difference Amount between Actual* Inversion and Goal Inversion.
for s in res.index:
    actives_w_s = reg[reg['Parte en Portafolio'] == s]
    if len(actives_w_s) > 0:
        active_t = actives_w_s['Precio Actual'].sum()
        obj_amo = (TOTAL_PORTFOLY + NEW_INVERSION) * res.loc[s, 'Objetivo (%)']
        res.loc[s,'Diferencia'] = obj_amo - active_t
    else:
        res.loc[s,'Diferencia'] = 0

# Calculate the New Inversion.
for s in res.index:
    if NEW_INVERSION >= 0:
        if res.loc[s, 'Diferencia'] > 0:
            diff_pos = res[res['Diferencia'] > 0]
            diff_pos = diff_pos['Diferencia'].sum()
            u = res.loc[s, 'Diferencia'] / diff_pos * NEW_INVERSION
            res.loc[s, 'Nueva Inversión'] = u
        else:
            res.loc[s, 'Nueva Inversión'] = 0
    else:
        if res.loc[s, 'Diferencia'] <= 0:
            diff_neg = res[res['Diferencia'] <= 0]
            diff_neg = diff_neg['Diferencia'].sum()
            u = res.loc[s, 'Diferencia'] / diff_neg * NEW_INVERSION
            res.loc[s, 'Nueva Inversión'] = u
        else:
            res.loc[s, 'Nueva Inversión'] = 0

# Calculate the New Percentage

for s in res.index:
    actives_w_s = reg[reg['Parte en Portafolio'] == s]
    if len(actives_w_s) > 0:
        active_t = actives_w_s['Precio Actual'].sum()
        NEW_PORTFOLY = TOTAL_PORTFOLY + NEW_INVERSION
        res.loc[s,'Nuevo Porcentaje'] = (active_t +  res.loc[s, 'Nueva Inversión']) / (NEW_PORTFOLY)
    else:
        res.loc[s,'Nuevo Porcentaje'] = 0

"""


# Pie Objective
if __name__ == "__main__":
    pie_obj = px.pie(res, names = res.index, values="Objetivo (%)",
                    hole = 0.7, title="Portfoly Objective")
    # pie_obj.show()

    # Pie Actual
    pie_act = px.pie(res, names = res.index, values="Nuevo Porcentaje",
                    hole = 0.7, title="Portfoly New")
    pie_act.show()

    # Pie Inversion
    pie_nv = px.pie(res, names = res.index, values="Nueva Inversión",
                    hole = 0.7, title="New Inversion")
    pie_nv.show()
