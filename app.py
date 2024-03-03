import plotly.express as px

from dash import Dash, Input, Output, State, html, dcc
import dash_bootstrap_components as dbc

from dash_selectors.selectors import rplanet_selector, star_size_selector
from dash_layout.layout import get_layout
from dash_df.planet_df import get_planet_df


app = Dash(__name__,
           external_stylesheets=[dbc.themes.COSMO])

df = get_planet_df()
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
    [Output(component_id='dist-temp-chart', component_property='children'),
     Output(component_id='celestial-chart', component_property='children')],
    [Input(component_id='submit-val', component_property='n_clicks')],
    [State(component_id='range-slider', component_property='value'),
     State(component_id='star-selector', component_property='value')]
)
def upd_dist_temp_chart(n, radius_range, star_size):  # это компонент из State - value
    chart_data = df[(df['RPLANET'] >= radius_range[0]) &
                    (df['RPLANET'] <= radius_range[1]) &
                    (df['StarSize']).isin(star_size)]

    # print(n)  # сколько раз кликнули на кнопку

    if not len(chart_data):  # если в фильтры пустые (ничего не выбрали)
        return html.Div('Not selector filter'), html.Div()

    fig1 = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')
    html1 = [html.Div('Planet Temperature ~ Distance from the STAR'),
             dcc.Graph(figure=fig1)]

    fig2 = px.scatter(chart_data, x='RA', y='DEC', size='RPLANET', color='status')
    html2 = [html.Div('Position on the Celestial Sphere'),
             dcc.Graph(figure=fig2)]

    # Возвращаем в той же последовательность, что и в Output
    return html1, html2


if __name__ == "__main__":
    app.run_server(debug=True)
