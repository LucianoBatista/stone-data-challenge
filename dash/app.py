import numpy as np
import pandas as pd
from pandas import CategoricalDtype

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

data = pd.read_csv("../data/to_analysis.csv")

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Stone - Data Challenge"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="👾", className="header-emoji"),
                html.H1(children="Stone - Data Challenge", className="header-title"),
                html.P(
                    children="Entendendo a melhor curva de acionamento ao cliente.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Estado", className="menu-title"),
                        dcc.Dropdown(
                            id="estado-filter",
                            options=[
                                {"label": estado, "value": estado}
                                for estado in np.sort(data.estado.unique())
                            ],
                            value="SP",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Cidade", className="menu-title"),
                        dcc.Dropdown(
                            id="cidade-filter",
                            options=[
                                {"label": cidade, "value": cidade}
                                for cidade in np.sort(data.cidade.unique())
                            ],
                            value="São Paulo",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Segmento", className="menu-title"),
                        dcc.Dropdown(
                            id="segmento-filter",
                            options=[
                                {"label": segmento, "value": segmento}
                                for segmento in data.segmento.unique()
                            ],
                            value="Alimentação",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(children="Sub Segmento", className="menu-title"),
                        dcc.Dropdown(
                            id="subsegmento-filter",
                            options=[
                                {"label": subsegmento, "value": subsegmento}
                                for subsegmento in data.subsegmento.unique()
                            ],
                            value="Alimentação Rápida",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="boxplot-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="barplot-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [Output("boxplot-chart", "figure"), Output("barplot-chart", "figure")],
    [
        Input("estado-filter", "value"),
        Input("cidade-filter", "value"),
        Input("segmento-filter", "value"),
        Input("subsegmento-filter", "value"),
    ],
)
def update_charts(estado, cidade, segmento, subsegmento):
    mask = (
        (data.estado == estado)
        & (data.cidade == cidade)
        & (data.segmento == segmento)
        & (data.subsegmento == subsegmento)
    )

    prop_columns = [column for column in data.columns if column.startswith("prop_")]

    df_filtered = data.loc[mask, :][prop_columns]
    df_melted = df_filtered.melt(value_vars=prop_columns, var_name="props")
    to_plot = df_melted.groupby(["props"])["value"].agg(np.nanmedian).reset_index()

    prop_categories = CategoricalDtype(
        [
            "prop_success_dsp5",
            "prop_success_dsp10",
            "prop_success_dsp15",
            "prop_success_dsp30",
            "prop_success_dsp60",
            "prop_success_dsp90",
            "prop_success_dspp15",
            "prop_success_dspp30",
            "prop_success_dspp45",
        ],
        ordered=True,
    )
    to_plot["props"] = to_plot["props"].astype(prop_categories)
    to_plot_sorted = to_plot.sort_values("props")

    boxplot_chart_figure = {
        "data": [
            {
                "x": to_plot_sorted["props"],
                "y": to_plot_sorted["value"],
                "type": "bar",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Valor médio do total de clientes pelos filtros aplicados.",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    barplot_chart_figure = {
        "data": [
            {
                "x": to_plot_sorted["props"],
                "y": to_plot_sorted["value"],
                "type": "bar",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Valor médio do total de clientes pelos filtros aplicados.",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return boxplot_chart_figure, barplot_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)
