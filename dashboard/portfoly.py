"""
    Finance App Tab: Portfoly
"""

from dash import html, dcc
from dash import callback, Input, Output
from dash import dash_table

from finances import portfoly


MULTI_COLUMN = {"padding": "5px",
                "display": "flex"}



# Portfoly
PORTFOLY = html.Div(
    children=[
        html.H1("Portafolio de Inversiones"),
        html.Div(children=[
            # Distribución de Portafolio
            dcc.Graph()
        ]),

        html.Div(children=[
            html.Div(children=[
                html.H1("Nueva Inversión"),
                dcc.Input(id = "new-portfoly", value=0, style={"font-size":"30px"})
            ], style={"width":"50%"}),
            html.Div(children=[
                html.H1("Valor de Portafolio: "),
            ], style={"width":"50%"}),
        ], style=MULTI_COLUMN),
        html.Div(children=[
            # Distribución de Activos.
            html.H1("Registro", style={"text-align":"center"}),
            dash_table.DataTable(id = "portfoly-table")
        ])
        ])


@callback(
    Output("portfoly-table", "dash-table"), Input("new-portfoly","value")
)

def add_new_inversion(amount):
    """
        Add new inversion and calculate the missing amount in 
        all the portfoly categories.  
    """
    if amount:
        return portfoly.res.to_dict("records")
