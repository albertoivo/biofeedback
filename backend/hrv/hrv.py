import matplotlib.pyplot as plt
import pandas as pd
from flask import Blueprint, abort

import utils

hrv_bp = Blueprint('hrv', __name__, url_prefix='/hrv')


@hrv_bp.route('/data')
def data():
    df = pd.read_excel('hrv/HRV_teste.xlsx', index_col=0)

    return df.to_json(date_format='iso', orient='index')


@hrv_bp.route('/statistics')
def statistics():
    df = pd.read_excel('hrv/HRV_teste.xlsx', index_col=0)

    return df['Reading'].describe().to_json()


@hrv_bp.route('/graph')
def hrv_graph():
    try:
        graph = pd.read_excel('hrv/HRV_teste.xlsx', index_col=0)
        graph = graph.dropna()
        graph[['Ln rMSSD 7-Day Rolling Average', 'Upper limit',
               'Lower Limit']].plot(figsize=(21, 7), grid=True)

        return utils.matplotlib_to_base64(plt)
    except ValueError as r:
        abort(404, r)
