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
            dcc.Graph(figure= portfoly.distribution())
        ]),

        html.Div(children=[
            html.Div(children=[
                html.H1("Nueva Inversión"),
                dcc.Input(id = "new-portfoly",
                          value=1_000,
                          type = "number",
                          style={"font-size":"30px"})
            ], style={"width":"50%"}),
            html.Div(children=[
                html.H1(id = "portfoly-value"),
            ], style={"width":"50%"}),
        ], style=MULTI_COLUMN),
        html.Div(children=[
            # Distribución de Activos.
            html.H1("Registro", style={"text-align":"center"}),
            dash_table.DataTable(id = "portfoly-table",
                                 style_data={"font-size": "30px"},
                                 style_header={"font-size": "30px"})],
                                 style={"width":"80%", "margin":"auto"})
        ])


@callback(
    Output("portfoly-table", "data"), Input("new-portfoly","value")
)

def add_new_inversion(amount):
    """
        Add new inversion and calculate the missing amount in 
        all the portfoly categories.  
    """
    if not portfoly.pd.isnull(amount):
        port_df = portfoly.portfoly_df(amount)
    else:
        port_df = portfoly.res_table
    return port_df.to_dict("records")

@callback(
    Output("portfoly-value","children"),Input("new-portfoly","value")
)

def portfoly_v(amount):
    """
        Calculate Portfoly Value
    """
    text = ""
    if amount:
        text = f"Valor del Portafolio: {portfoly.TOTAL_PORTFOLY + amount}"
    else:
        text = f"Valor del Portafolio: {portfoly.TOTAL_PORTFOLY}"
    return text
