import plotly.graph_objects as go


CHARTS_TEMPLATE = go.layout.Template(
    layout={
        'legend': {
            'orientation': 'h',
            'title_text': '',
            'x': 0,
            'y': 1.1
        },
        'font': {
            'family': 'Century Gothic',
            'size': 14
        }
    }
)

# цвета для колонки 'status' ['challenging', 'extreme', 'promising']
COLOR_STATUS_VALUES = ['lightgray', '#78063c', '#05502a']
