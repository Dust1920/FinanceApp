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





def difference_goal_actual(n_i, d_b = res):
    """
    Calculate the money difference between the actual inversion and 
    """
    for s_i in d_b.index:
        actives_w_s = reg[reg['Parte en Portafolio'] == s_i]
        if len(actives_w_s) > 0:
            active_t = actives_w_s['Precio Actual'].sum()
            obj_amo = (TOTAL_PORTFOLY + n_i) * d_b.loc[s_i, 'Objetivo (%)']
            d_b.loc[s_i,'Diferencia'] = obj_amo - active_t
        else:
            d_b.loc[s_i,'Diferencia'] = 0
    return d_b


def new_inversion(nv_inv, d_b = res):
    """
        Calculate the new inversions
    """
    for s_ii in d_b.index:
        if nv_inv >= 0:
            if d_b.loc[s_ii, 'Diferencia'] > 0:
                diff_pos = d_b[d_b['Diferencia'] > 0]
                diff_pos = diff_pos['Diferencia'].sum()
                u = d_b.loc[s_ii, 'Diferencia'] / diff_pos * nv_inv
                d_b.loc[s_ii, 'Nueva Inversión'] = u
            else:
                d_b.loc[s_ii, 'Nueva Inversión'] = 0
        else:
            if d_b.loc[s_ii, 'Diferencia'] <= 0:
                diff_neg = d_b[d_b['Diferencia'] <= 0]
                diff_neg = diff_neg['Diferencia'].sum()
                u = d_b.loc[s_ii, 'Diferencia'] / diff_neg * nv_inv
                d_b.loc[s_ii, 'Nueva Inversión'] = u
            else:
                d_b.loc[s_ii, 'Nueva Inversión'] = 0
    return d_b

def new_percentage(nv_i, d1 = res, d2 = reg):
    """
        Calculate the new percentage after the new inversion. 
    """
    for s_k in d1.index:
        actives_w_s = d2[d2['Parte en Portafolio'] == s_k]
        if len(actives_w_s) > 0:
            active_t = actives_w_s['Precio Actual'].sum()
            n_p = TOTAL_PORTFOLY + nv_i
            d1.loc[s_k,'Nuevo Porcentaje'] = (active_t + d1.loc[s_k, 'Nueva Inversión']) / n_p
        else:
            d1.loc[s_k,'Nuevo Porcentaje'] = 0
    return d1



def portfoly_df(amount, d_b = res):
    """
        Create a Portfoly Table
    """
    d_b = difference_goal_actual(amount, d_b)
    d_b = new_inversion(amount)
    d_b = new_percentage(amount, d_b)
    db_table = d_b.copy()
    db_table['Actual (%)'] = db_table['Actual (%)'].transform(lambda x: f"{round(x * 100,2)}%")
    db_table['Objetivo (%)'] = db_table['Objetivo (%)'].transform(lambda x: f"{round(x * 100,2)}%")
    db_table['Diferencia'] = db_table['Diferencia'].transform(lambda x: f"{round(x,2)}")
    db_table['Nueva Inversión'] = db_table['Nueva Inversión'].transform(lambda x: f"{round(x,2)}")
    db_table['Nuevo Porcentaje'] = db_table['Nuevo Porcentaje'].transform(lambda x: f"{round(x * 100,2)}%")
    return db_table


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
