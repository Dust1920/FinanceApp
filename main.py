"""
    Finance App
"""
# DashBoard
## Dash Libraries
from dash import Dash
from dash import html, dcc

# Personal Libraries
from dashboard import title
from dashboard import portfoly as pf
from dashboard import expenses as xp
from dashboard import summary as sm




SELECTED_STYLE = {
    "principal tabs": {
        "color": "red",
        "border-radius":20
    }
}

STYLE = {
    "principal tabs": {
        "color": "blue",
        "fontSize": 20,
        "border-radius":20

    }
}

# Create DashBoard
app = Dash(__name__)
app.title = "Finanzas Personales"


app.layout = html.Div(children=[
    title.PRINCIPAL,
    dcc.Tabs(children=[
        dcc.Tab(label = "Portafolio", children=pf.PORTFOLY,
                selected_style= SELECTED_STYLE["principal tabs"]),
        dcc.Tab(label = "Resumen", children= sm.SUMMARY,
                selected_style= SELECTED_STYLE["principal tabs"]),
        dcc.Tab(label = "Gastos", children= xp.EXPENSES,
                selected_style= SELECTED_STYLE["principal tabs"])
    ], style=STYLE['principal tabs'])
]
)

if __name__ == "__main__":
    app.run(debug=True)
