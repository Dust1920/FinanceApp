"""
    Finance App: Central Dashboard
"""


from dash import Dash
from dash import html, dcc
from dash import callback, Input, Output

from dashboard import general as g
from dashboard import intro





app = Dash(__name__)
app.title = "Finanzas Personales"

app.layout = html.Div(children=[
    html.Header(children=[
        html.H1("Finanzas Personales", className="title-text"),
        html.H1("Fecha de Hoy: "),
        html.Div(children=[
            html.Div(children=[
                html.H2("Año"),
                dcc.Dropdown(options = [2023,2024,2025], value = g.YEAR_NOW),
            ], style={"width":"50%", "margin":"5px"}),
            html.Div(children=[
                html.H2("Mes"),
                dcc.Dropdown(options=g.MONTHS),
            ], style={"width":"50%", "margin":"5px"}),
        ], className="multicolumn"),
        dcc.Tabs(children=[
            dcc.Tab(label = "Introducción",
                    children = intro.tab,
                    className="mtab",
                    selected_className="selt1"),
            dcc.Tab(label = "Tarjetas de Crédito", className="mtab",
                    disabled=True),
            dcc.Tab(label = "Gastos Corrientes", className="mtab",
                    disabled=True),
            dcc.Tab(label = "Meses sin Intereses", className="mtab",
                    disabled=True),
            dcc.Tab(label = "Portafolio", className="mtab",
                    disabled=True),
        ], className="maintabs")
    ]),
    html.Div(children=[

    ]),
    html.Footer(children=[
        html.H6("Author: David Peña Peralta")
    ])
])





if __name__ == "__main__":
    app.run(debug= True)
