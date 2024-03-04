import pandas as pd
import numpy as np
import requests


def get_planet_df():
    url = 'http://asterank.com/api/kepler?query={}&limit=2000'
    response = requests.get(url=url)
    df = pd.json_normalize(response.json())
    df = df[df['PER'] > 0]
    df['KOI'] = df['KOI'].astype(int, errors='ignore')

    # для разбивки на категории относительно размера солнца: 0-80%, 80-120%, 120-1000%
    bins_sun_size = [0, 0.8, 1.2, 100]
    names = ['small', 'similar', 'bigger']
    df['StarSize'] = pd.cut(df['RSTAR'], bins=bins_sun_size, labels=names)

    # для разбивки по температуре в K
    bins_temperature = [0, 200, 400, 500, 5000]
    tp_labels = ['low', 'optimal', 'high', 'extreme']
    df['temp'] = pd.cut(df['TPLANET'], bins=bins_temperature, labels=tp_labels)

    # для разбивки по размеру ГРАВИТАЦИИ планеты (относительно Земли)
    bins_gravity_size = [0, 0.5, 2, 4, 100]
    gravity_labels = ['low', 'optimal', 'high', 'extreme']
    df['gravity'] = pd.cut(df['RPLANET'], bins=bins_gravity_size, labels=gravity_labels)

    # Статус планеты
    df['status'] = np.where(
        (df['temp'] == 'optimal') &
        (df['gravity'] == 'optimal'),
        'promising', None
    )

    df.loc[:, 'status'] = np.where(
        (df['temp'] == 'optimal') &
        (df['gravity'].isin(['low', 'high'])),
        'challenging', df['status']
    )

    df.loc[:, 'status'] = np.where(
        (df['gravity'] == 'optimal') &
        (df['temp'].isin(['low', 'high'])),
        'challenging', df['status']
    )

    df['status'] = df.status.fillna('extreme')

    #Reative distance (distance to SUN / SUM radii)
    df.loc[:, 'relative_dist'] = df['A'] / df['RSTAR']

    return df
