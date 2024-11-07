from dash import html, dcc
from dash import callback, Input, Output


tab = html.Div(children=[
    html.Div(children = [
        html.H1("Primeros Pasos"),
        html.P("Para comenzar con FinanceDash ocupara subir una serie de archivos \
               (Para mayor información consulte el documento README.md)",
               className="divtext"),
        html.Div(children=[
            html.Div(children=[
                html.H2("Tarjetas de Crédito")
            ], style={"width":"50%"}),
            html.Div(children=[
                    dcc.Upload(
                        id="upload-data",
                        children=html.Div([
                            "Drag and drop or click to select a file to upload."]),
                        className="divupload",
                        multiple=True
                    ),
                    html.H2("File List"),
                    html.Ul(id="file-list"),
                        ], style={"width":"50%"})
        ], className="multicolumn")
    ]),
    html.Div(children = [
    html.H1("Ingresos", className="divtitle"),
    html.P("Los ingresos son nuestra entrada de efectivo. Parte fundamental a \
           considerar dentro de este dashboard", className="divtext"),
    html.Div(children=[
        html.Div(children=[
            html.H2("Ingresos mensuales del año en curso")
        ], style={"width":"50%"}),
        html.Div(children=[
            html.H2("Distribución mensual del ingreso")
        ], style={"width":"50%"})
    ], className="multicolumn")
    ]),
])
