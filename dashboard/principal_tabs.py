from dash import html, dcc
from dash import dash_table


MULTI_COLUMN = {"padding": "5px",
                "display": "flex",
                "background-color":"red"}

# Portfoly
portfoly = html.Div(
    children=[
        html.H1("Portafolio de Inversiones"),
        html.Div(children=[
            # Distribución de Portafolio
            dcc.Graph()
        ]),
        html.Div(children=[
            # Distribución de Activos.
            html.H1("Registro", style={"text-align":"center"}),
            dash_table.DataTable()
        ])
        ])

# Summary
sum_ary = html.Div(children=[
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


# Expenses
expenses = html.Div(children=[
    html.H1("Gastos Personales", style = {"text-align": "center"}),
    html.Div(children=[
        html.Div(children=[
            # Grafica de Consumo Total por Mes
            html.H1("Consumo Mensual"),
            dcc.Graph()
        ], style= {"width": "50%"}),
        html.Div(children=[
            # Grafica por Consumo Total por Mes
            html.H1("Distribución por Tarjeta"),
            dcc.Graph()
        ], style= {"width": "50%"})
    ], style=MULTI_COLUMN)
])
