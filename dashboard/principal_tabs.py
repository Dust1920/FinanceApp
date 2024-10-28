from dash import html, dcc

MULTI_COLUMN = {"padding": "5px",
                "display": "flex",
                "background-color":"red"}

# Portfoly
portfoly = html.Div(
    children=[
        html.H1("Portafolio de Inversiones"),
        html.Div(children=[
            # Distribución de Portafolio
        ]),
        html.Div(children=[
            # Distribución de Activos.
            html.H1("Registro", style={"text-align":"center"})
        ])
        ])

# Summary
sum_ary = html.Div(children=[
    html.H1("Resumen general"),
    html.Div(children=[
        html.Div(children=[
            # Dias para la fecha de corte.
            html.H1("Dias para pagar la tarjeta")
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
            html.H1("Crédito Histórico")
        ], style={"width":"50%"}),
        html.Div(children=[
            # Uso de Crédito Mensual
            html.H1("Uso de Crédito: "),
            html.H1(""),
            html.H1("Crédito Total: ")
        ], style={"width":"50%"})
    ], style=MULTI_COLUMN)
])


# Expenses
expenses = html.Div(children=[
    html.H1("Gastos Personales", style = {"text-align": "center"}),
    html.Div(children=[
        html.Div(children=[
            html.H1("Consumo Mensual"),
            # Grafica de Consumo Total por Mes
        ], style= {"width": "50%"}),
        html.Div(children=[
            html.H1("Distribución por Tarjeta")
            # Grafica por Consumo Total por Mes
        ], style= {"width": "50%"})
    ], style=MULTI_COLUMN)
])
