from dash import html, dcc, Dash
import dash_bootstrap_components as dbc

from dash_tabs.tabs import get_tab_charts, get_tab_about


tab_charts = get_tab_charts()
tab_about = get_tab_about()


def get_layout(app: Dash, selectors_dict: dict):
    """:param selectors_dict - dcc selectors"""

    rplanet_selector: dcc.RangeSlider = selectors_dict['rplanet_selector']
    star_size_selector: dcc.Dropdown = selectors_dict['star_size_selector']

    app.layout = html.Div([
        # Header ~~~~~~~~~~~~~~~~~~~~~~~~
        dbc.Row(html.H1("Hello Dash's lessons!"),
                style={'margin-bottom': 40}),
        # Filters ~~~~~~~~~~~~~~~~~~~~~~~
        dbc.Row([
            dbc.Col([
                html.H6('Select planet main semi-axis range'),
                html.Div(rplanet_selector)
            ],
                md=2
            ),
            dbc.Col([
                html.H6('Star Size'),
                html.Div(star_size_selector)
            ],
                width={'size': 3, 'offset': 1}
            ),
            dbc.Col(dbc.Button('Apply', id='submit-val', n_clicks=0, className='mr-2'))
        ],
            style={'margin-bottom': 40}
        ),
        dbc.Tabs([
            dbc.Tab(tab_charts, label='Charts'),
            dbc.Tab(dbc.Row(html.Div(id='raw-data-table')), label='Data'),
            dbc.Tab(tab_about, label='About')
        ])
    ],
        style={'margin-left': '80px',
               'margin-right': '80px'}
    )
