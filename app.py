import plotly.express as px

from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc

from dash_selectors.selectors import rplanet_selector, star_size_selector
from dash_layout.layout import get_layout
from dash_df.planet_df import get_planet_df


df = get_planet_df()

app = Dash(__name__,
           external_stylesheets=[dbc.themes.COSMO])

selectors_dict = {
    'rplanet_selector': rplanet_selector(df),
    'star_size_selector': star_size_selector()
}

get_layout(app, selectors_dict)


""" State - это состояния которые хранят в себе измененные данные
    Input - это то, что триггерит изменение состояний.
    Т.е., после нажатия на кноплку сработает триггер, который новые данные выведит на дашборт
"""
@app.callback(
    Output(component_id='dist-temp-chart', component_property='figure'),
    [Input(component_id='submit-val', component_property='n_clicks')],
    [State(component_id='range-slider', component_property='value'),
     State(component_id='star-selector', component_property='value')]
)
def upd_dist_temp_chart(n, radius_range, star_size):  # это компонент из Input - value
    chart_data = df[(df['RPLANET'] >= radius_range[0]) &
                    (df['RPLANET'] <= radius_range[1]) &
                    (df['StarSize']).isin(star_size)]

    # print(n)  # сколько раз кликнули на кнопку

    fig = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')

    return fig


@app.callback(
    Output(component_id='celestial-chart', component_property='figure'),
    [Input(component_id='submit-val', component_property='n_clicks')],
    [State(component_id='range-slider', component_property='value'),
     State(component_id='star-selector', component_property='value')]
)
def upd_celestail_chart(n, radius_range, star_size):  # это компонент из Input - value
    chart_data = df[(df['RPLANET'] >= radius_range[0]) &
                    (df['RPLANET'] <= radius_range[1]) &
                    (df['StarSize']).isin(star_size)]

    fig = px.scatter(chart_data, x='RA', y='DEC', size='RPLANET', color='status')

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
