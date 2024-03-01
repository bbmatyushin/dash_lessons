from dash import dcc
from pandas import DataFrame


def rplanet_selector(df: DataFrame) -> dcc.RangeSlider:
    rplanet_selector = dcc.RangeSlider(
        id='range-slider',
        min=min(df['RPLANET']),
        max=max(df['RPLANET']),
        marks={5: '5', 10: '10', 20: '20', 30: '30', 40: '40'},
        step=1,
        value=[5, 50]  # значения по умолчанию
    )

    return rplanet_selector


def star_size_selector() -> dcc.Dropdown:
    names = ['small', 'similar', 'bigger']
    options = [{'label': n, 'value': n} for n in names]  # в словаре сначала идет видимая часть в web'e, потом его значение

    star_size_selector = dcc.Dropdown(
        id='star-selector',
        options=options,
        value=['small', 'similar', 'bigger'],  # значения по умолчанию
        multi=True
    )

    return star_size_selector


if __name__ == "__main__":
    print(1)


