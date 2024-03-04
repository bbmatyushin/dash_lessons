import dash_bootstrap_components as dbc
from dash import html

from dash_tables.tables import table_about


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


def get_tab_about():
    table = table_about()
    text_a = 'Data are sourced from Kepler API via asterank.com'

    tab = [
        dbc.Row(html.A(text_a, href='http://www.asterank.com/kepler'),
                style={'margin-top': 20}),
        dbc.Row(html.Div(children=table),
                style={'margin-top': 20})
     ]

    return tab
