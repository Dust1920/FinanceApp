"""
    Expenses Block
"""

from dash import html, dcc
from dash import Input, Output, callback
from finances import credit_cards as cc



MULTI_COLUMN = {"padding": "5px",
                "display": "flex"}


EXPENSES = html.Div(children=[
    html.H1("Gastos Personales", style = {"text-align": "center"}),
    html.H2("Seleccione un año"),
    html.Div(children=[
        dcc.Dropdown(id = "year-visualize",
                     options = [2023, 2024, 2025],
                     value = 2024,
                     placeholder="Year to Visualize",
                     clearable=False,
                     style={"font-size":"30px","height":"50px"})
            ],style={"width":"80%", "margin":"auto", "font-size":"30px"}),
    html.H1("Gastos Mensuales", style = {"text-align": "center"}),
    html.H2("Seleccione un mes"),
    html.Div(children = [

    ], style={"width":"80%", "margin":"auto", "font-size":"30px"}),
    html.Div(children=[
        html.Div(children=[
            # Grafica de Consumo Total por Mes
            html.H1("Consumo Mensual"),
            html.Div(children=[
                dcc.Graph()
            ],style={"width":"98%", "margin":"auto"}),
        ], style= {"width": "50%"}),
        html.Div(children=[
            # Grafica por Consumo Total por Mes
            html.H1("Distribución por Tarjeta"),
            dcc.Graph()
        ], style= {"width": "50%"})
    ], style=MULTI_COLUMN),
    html.H1("Meses sin Intereses"),
    html.Div(children=[
        html.Div(children=[
            # Grafica de Consumo Total por Mes
            html.H1("Distribución por Tarjeta"),
            html.Div(children=[
                dcc.Graph(id = "ifm-dist"),
            ],style={"width":"95%","margin":"auto"})
        ], style= {"width": "50%"}),
    html.Div(children=[
        # Grafica por Consumo Total por Mes
        html.H1("Progreso"),
        html.Div(children=[
        dcc.Graph(),
        ],style={"width":"95%","margin":"auto"})
    ], style= {"width": "50%"})
    ], style=MULTI_COLUMN)
])





@callback(
    Output("ifm-dist", "figure"), Input("year-visualize","value")
)

def ifm_plot(year):
    """
        Plot IFM by Cards and Year
    """
    fig = cc.plot_cards("I-FM",str(year)[2:])
    return fig
