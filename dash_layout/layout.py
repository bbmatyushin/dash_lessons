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
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.Img(src=app.get_asset_url('images/planet.jpg'),
                             style={'width': '85px', 'marginLeft': '40px'}),
                    md=1
                ),
                dbc.Col([
                    html.H1("Exoplanet Data Visualization"),
                    html.A('Read about Exoplaten', href='https://ru.wikipedia.org/wiki/%D0%AD%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0',
                           style={'marginLeft': '12px'})
                ],
                    md=7
                ),
                dbc.Col(html.Div([
                    html.P('Contact information'),
                    html.A('Git Repository', href='https://github.com/bbmatyushin/dash_lessons/tree/lesson_14')
                ], className='app-referral'),
                    md=4
                )
            ],
                className='app-header')  # app-header - класс который создан в header.css
        ]),

        dcc.Store(id='filtered-data', storage_type='session'),

        html.Div([
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
            className='app-body'
        ),
    ])
    star_size_selector: dcc.Dropdown = selectors_dict['star_size_selector']

