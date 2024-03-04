from dash.dash_table import DataTable
from dash import html
import dash_bootstrap_components as dbc
from pandas import DataFrame


def raw_data_table(data: DataFrame) -> DataTable:
    raw_data = data.drop(['relative_dist', 'StarSize', 'ROW', 'temp', 'gravity'], axis=1)
    tbl = DataTable(data=raw_data.to_dict('records'),
                    columns=[{'name': i, 'id': i} for i in raw_data.columns],
                    style_data={'width': '100px',
                                'maxWidth': '100px',
                                'minWidth': '100px'},
                    style_header={'textAlign': 'center'},
                    page_size=30)

    return tbl


def table_about() -> dbc.Table:
    table_header = [
        html.Thead(html.Tr([
            html.Th('Field Name'),
            html.Th('Details')
        ]))
    ]

    expl = {
        'KOI': 'Object of Interest number',
        'A': 'Semi-major axis (AU)',
        'RPLANET': 'Planetary radius (Earth radii)',
        'RSTAR': 'Stellar radius (Sol radii)',
        'TSTAR': 'Effective temperature of host star as reported in KIC (k)',
        'KMAG': 'Kepler magnitude (kmag)',
        'TPLANET': 'Equilibrium temperature of planet, per Borucki et al. (k)',
        'T0': 'Time of transit center (BJD-2454900)',
        'UT0': 'Uncertainty in time of transit center (+-jd)',
        'PER': 'Period (days)',
        'UPER': 'Uncertainty in period (+-days)',
        'DEC': 'Declination (@J200)',
        'RA': 'Right ascension (@J200)',
        'MSTAR': 'Derived stellar mass (msol)'
    }

    tbl_row = [html.Tr([html.Td(k), html.Td(v)]) for k, v in expl.items()]

    table_body = [html.Tbody(tbl_row)]

    table = dbc.Table(table_header + table_body, bordered=True)

    return table
