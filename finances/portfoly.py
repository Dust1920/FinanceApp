"""
    Transform Data: Portfoly
        - 
"""
import pandas as pd


raw = pd.read_excel("data\\Portfoly.xlsx", sheet_name=None)
res = raw['Resumen']
reg = raw['Registro']

res = res.set_index('Sección', drop=True)
reg = reg.set_index('Simbolo', drop=True)

TOTAL_PORTFOLY = reg['Precio Actual'].sum()

NEW_INVERSION = 500

print(reg.columns)

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
        res.loc[s,'Nuevo Porcentaje'] = (active_t +  res.loc[s, 'Nueva Inversión']) / (TOTAL_PORTFOLY + NEW_INVERSION)
    else:
        res.loc[s,'Nuevo Porcentaje'] = 0

print(res)
