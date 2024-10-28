from dash import html, dcc

# Portfoly


portfoly = html.Div(
    children=[
        html.H1("Portafolio de Inversiones"),
    ]
)

# Summary

sum_ary = html.Div(children=[
    html.H1("Resumen general"),
])





# Expenses

expenses = html.Div(children=[
    html.H1("Gastos Personales"),
    html.Div(children=[
        html.Div(children=[
            html.H1("Consumo Mensual")
        ], style= {"width": "50%"}),  
        html.Div(children=[
            html.H1("Distribución por Tarjeta")
        ], style= {"width": "50%"})
    ], style={
        
    })
])
