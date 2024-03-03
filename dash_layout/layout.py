from dash import html, dcc, Dash
import dash_bootstrap_components as dbc


def get_layout(app: Dash, selectors_dict: dict):
    """:param selectors_dict - dcc selectors"""

    rplanet_selector: dcc.RangeSlider = selectors_dict['rplanet_selector']
    star_size_selector: dcc.Dropdown = selectors_dict['star_size_selector']

    app.layout = html.Div([
        # Head
        dbc.Row(html.H1("Hello Dash's lessons!"),
                style={'margin-bottom': 40}),
        # Filters
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
        # Charts
        dbc.Row([
            dbc.Col([
                html.Div('Planet Temperature ~ Distance from the STAR'),
                dcc.Graph(id='dist-temp-chart')  # график (figure) возвращается из upd_dist_temp_chart()
            ],
                md=6
            ),
            dbc.Col([
                html.Div('Position on the Celestial Sphere'),
                dcc.Graph(id='celestial-chart')
            ])
        ],
            style={'margin-bottom': 40}
        )
    ],
        style={'margin-left': '80px',
               'margin-right': '80px'}
    )