import dash_bootstrap_components as dbc
from dash import html


def get_tab_charts():
    tab = [dbc.Row([
        dbc.Col([html.Div(id='dist-temp-chart')], md=6),
        dbc.Col([html.Div(id='celestial-chart')], md=6)
    ],
        style={'margin-top': 20}
    ),
        dbc.Row([
            dbc.Col(html.Div(id='relative-dist-chart'), md=6),
            dbc.Col(html.Div(id='mstar-tstar-chart'), md=6)
        ])
    ]

    return tab
