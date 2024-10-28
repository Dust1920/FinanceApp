from dash import html, dcc


MULTI_COLUMN = {"padding": "5px",
                "display": "flex"}


EXPENSES = html.Div(children=[
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
