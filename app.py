import requests
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from dash_selectors.selectors import rplanet_selector, star_size_selector


def get_df():
    url = 'http://asterank.com/api/kepler?query={}&limit=2000'
    response = requests.get(url=url)
    df = pd.json_normalize(response.json())
    df = df[df['PER'] > 0]

    bins = [0, 0.8, 1.2, 100]  # для разбивки на категории относительно размера солнца: 0-80%, 80-120%, 120-1000%
    names = ['small', 'similar', 'bigger']
    df['StarSize'] = pd.cut(df['RSTAR'], bins=bins, labels=names)

    return df


df = get_df()

app = Dash(__name__,
           external_stylesheets=[dbc.themes.COSMO])

app.layout = html.Div([
    # Head
    dbc.Row(html.H1("Hello Dash's lessons!"),
            style={'margin-bottom': 40}),
    # Filters
    dbc.Row([
        dbc.Col([
            html.Div('Select planet main semi-axis range'),
            html.Div(rplanet_selector(df))
        ],
            md=2
        ),
        dbc.Col([
            html.Div('Star Size'),
            html.Div(star_size_selector())
        ],
            width={'size': 3, 'offset': 1}
        )
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
        )
    ],
        style={'margin-bottom': 40}
    )
],
    style={'margin-left': '80px',
           'margin-right': '80px'}
)

# app.layout = html.Div([
#     html.H1('Hello Lesson!'),
#
#     html.Div('Select planet main semi-axis range'),
#     html.Div(rplanet_selector(df),
#              style={'width': '400px',
#                     'margin-bottom': '40px'}),
#
#     html.Div('Star Size'),
#     html.Div(star_size_selector(),
#              style={'width': '400px',
#                     'margin-bottom': '40px'}),
#
#     html.Div('Planet Temperature ~ Distance from the STAR'),
#     dcc.Graph(id='dist-temp-chart')  # график (figure) возвращается из upd_dist_temp_chart()
# ],
#     style={'margin-left': '80px',
#            'margin-right': '80px'}
# )


@app.callback(
    Output(component_id='dist-temp-chart', component_property='figure'),
    [Input(component_id='range-slider', component_property='value'),
     Input(component_id='star-selector', component_property='value')]
)
def upd_dist_temp_chart(radius_range, star_size):  # это компонент из Input - value
    chart_data = df[(df['RPLANET'] >= radius_range[0]) &
                    (df['RPLANET'] <= radius_range[1]) &
                    (df['StarSize']).isin(star_size)]

    fig = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
