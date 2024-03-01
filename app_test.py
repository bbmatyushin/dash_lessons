import requests
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output


url = 'http://asterank.com/api/kepler?query={}&limit=2000'

response = requests.get(url=url)
df = pd.json_normalize(response.json())

fig = px.scatter(df, x='TPLANET', y='A')

rplanet_selector = dcc.RangeSlider(
    id='range-slider',
    min=min(df['RPLANET']),
    max=max(df['RPLANET']),
    marks={5: '5', 10: '10', 20: '20', 30: '30', 40: '40'},
    step=1,
    value=[5, 50]  # значения по умолчанию
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Hello Lesson!'),
    html.Div('Select planet main semi-axis range'),
    html.Div(rplanet_selector,
             style={'width': '400px',
                    'margin-bottom': '40px'}),
    html.Div('Planet Temperature ~ Distance from the STAR'),
    dcc.Graph(id='dist-temp-chart', figure=fig)
],
    style={'margin-left': '80px',
           'margin-right': '80px'}
)


@app.callback(
    Output(component_id='dist-temp-chart', component_property='figure'),
    Input(component_id='range-slider', component_property='value')
)
def upd_dist_temp_chart(radius_range):  # это компонент из Input - value
    chart_data = df[(df['RPLANET'] >= radius_range[0]) &
                    (df['RPLANET'] <= radius_range[1])]

    fig = px.scatter(chart_data, x='TPLANET', y='A')

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
