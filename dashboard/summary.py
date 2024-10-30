from dash import html, dcc


MULTI_COLUMN = {"padding": "5px",
                "display": "flex"}


SUMMARY = html.Div(children=[
    html.H1("Resumen general"),
    html.Div(children=[
        html.Div(children=[
            # Dias para la fecha de corte.
            html.H1("Dias para pagar la tarjeta"),
            dcc.Graph()
        ], style={"width":"50%"}),
        html.Div(children=[
            # Fecha Actual
            html.H1("Fecha de Hoy"),
            html.H2("")
        ],style = {"width":"50%"}),
    ], style=MULTI_COLUMN),
    html.Div(children=[
        html.Div(children=[
            # Uso de Crédito Historico por Año
            html.H1("Crédito Histórico"),
            dcc.Dropdown(options = [2023,2024,2025],
                         value = 2024,
                         clearable = False,
                         style={"font-size":"30px"}),
            dcc.Graph()
        ], style={"width":"50%"}),
        html.Div(children=[
            # Uso de Crédito Mensual
            html.H1("Uso de Crédito:", style={"margin-left":"10px"}),
            html.H1("", style={"margin":"5px"}),
            html.H1("Crédito Total: ", style={"margin-left":"10px"})
        ], style={"width":"50%"})
    ], style=MULTI_COLUMN)
])