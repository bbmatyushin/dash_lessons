import pandas as pd
import plotly.express as px
from io import StringIO

from dash import Dash, Input, Output, State, html, dcc, dash_table
import dash_bootstrap_components as dbc

from dash_selectors.selectors import rplanet_selector, star_size_selector
from dash_layout.layout import get_layout
from dash_df.planet_df import get_planet_df
from dash_tables.tables import raw_data_table
from dash_design.charts_template import CHARTS_TEMPLATE, COLOR_STATUS_VALUES


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
@app.callback(Output(component_id='filtered-data', component_property='data'),
              [Input(component_id='submit-val', component_property='n_clicks')],
              [State(component_id='range-slider', component_property='value'),
               State(component_id='star-selector', component_property='value')]
              )
def filter_data(n, radius_range, star_size):
    """Через такой callback можно отдельно строить фильтрацию всего DF.
    Т.е. получить данные для фильтрации от пользователя, здесь обработать,
    и потом строить графики."""
    my_data = df[(df['RPLANET'] >= radius_range[0]) &
                 (df['RPLANET'] <= radius_range[1]) &
                 (df['StarSize']).isin(star_size)]

    return my_data.to_json(date_format='iso', orient='split', default_handler=str)


@app.callback(
    [Output(component_id='dist-temp-chart', component_property='children'),
     Output(component_id='celestial-chart', component_property='children'),
     Output(component_id='relative-dist-chart', component_property='children'),
     Output(component_id='mstar-tstar-chart', component_property='children'),
     Output(component_id='raw-data-table', component_property='children')],
    [Input(component_id='filtered-data', component_property='data')]
)
def upd_dist_temp_chart(data):  # это компоненты из Input и State - component_property
    # Если использовать read_json(data), то выдает предупреждение.
    # Необходимо data передать через StringIO
    chart_data = pd.read_json(StringIO(data), orient='split')

    if not len(chart_data):  # если в фильтры пустые (ничего не выбрали)
        return html.Div('Not selector filter'), html.Div(), \
               html.Div(), html.Div(), html.Div()

    # dist-temp-chart
    fig1 = px.scatter(chart_data, x='TPLANET', y='A', color='StarSize')
    fig1.update_layout(template=CHARTS_TEMPLATE)
    html1 = [html.H4('Planet Temperature ~ Distance from the STAR'),
             dcc.Graph(figure=fig1)]

    # celestial-chart
    fig2 = px.scatter(chart_data, x='RA', y='DEC', size='RPLANET',
                      color='status', color_discrete_sequence=COLOR_STATUS_VALUES)
    fig2.update_layout(template=CHARTS_TEMPLATE)
    html2 = [html.H4('Position on the Celestial Sphere'),
             dcc.Graph(figure=fig2)]

    # relative-dist-chart
    fig3 = px.histogram(chart_data, x='relative_dist',
                        color='status', color_discrete_sequence=COLOR_STATUS_VALUES,
                        barmode='overlay', marginal='violin')
    fig3.add_vline(x=1, y0=0, y1=150, annotation_text='Earth', line_dash='dot')
    fig3.update_layout(template=CHARTS_TEMPLATE)
    html3 = [html.H4('Relative Distance (AU/Sol radii)'),
             dcc.Graph(figure=fig3)]

    # mstar-tstar-chart
    fig4 = px.scatter(chart_data, x='MSTAR', y='TSTAR', size='RPLANET',
                      color='status', color_discrete_sequence=COLOR_STATUS_VALUES)
    fig4.update_layout(template=CHARTS_TEMPLATE)
    html4 = [html.H4('Star Mass ~ Star Temperature'),
             dcc.Graph(figure=fig4)]

    # raw-data-table
    tbl = raw_data_table(chart_data)
    html5 = [html.H5('Raw Data'), tbl]

    # Возвращаем в той же последовательность, что и в Output
    return html1, html2, html3, html4, html5


if __name__ == "__main__":
    app.run_server(debug=True)
