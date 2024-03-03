from dash import html, dcc, Dash
import dash_bootstrap_components as dbc


# Charts ~~~~~~~~~~~~~~~~~~~~~~~
tab1_content = [dbc.Row([
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
                html.Div('Select planet main semi-axis range'),
                html.Div(rplanet_selector)
            ],
                md=2
            ),
            dbc.Col([
                html.Div('Star Size'),
                html.Div(star_size_selector)
            ],
                width={'size': 3, 'offset': 1}
            ),
            dbc.Col(dbc.Button('Apply', id='submit-val', n_clicks=0, className='mr-2'))
        ],
            style={'margin-bottom': 40}
        ),
        dbc.Tabs([
            dbc.Tab(tab1_content, label='Charts'),
            dbc.Tab(html.Div('Tab 2 Content'), label='Tab2'),
            dbc.Tab(html.Div('About Page'), label='About')
        ])
    ],
        style={'margin-left': '80px',
               'margin-right': '80px'}
    )
