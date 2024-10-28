"""
    Finance App
"""
# DashBoard
from dashboard import title
from dashboard import principal_tabs as ptab


from dash import Dash
from dash import html, dcc, Input, Output


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
        dcc.Tab(label = "Portafolio", children=ptab.portfoly,
                selected_style= SELECTED_STYLE["principal tabs"]),
        dcc.Tab(label = "Resumen", children=ptab.sum_ary,
                selected_style= SELECTED_STYLE["principal tabs"]),
        dcc.Tab(label = "Gastos", children=ptab.expenses,
                selected_style= SELECTED_STYLE["principal tabs"])
    ], style=STYLE['principal tabs'])
]
)




if __name__ == "__main__":
    app.run(debug=True)
