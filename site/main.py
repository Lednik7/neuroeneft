import logging
import pandas as pd
from models.utils.plot import plot
from models.utils.pred_model import predictive_model
from flask import Flask, render_template, jsonify


df = pd.read_csv("../models/data.csv")
pkl_path = "../models/Prophet.pkl"


def create_plot(n, df, pkl_path, save_path=False):
    """
    create_plot(7, df, pkl_path, "save_path")
    """
    model = predictive_model(df).load_pickle(pkl_path)
    forecast = model.plot_for_n(n)
    figure = plot(df, forecast)
    if save_path:
        figure.savefig(save_path)
    return figure


logging.basicConfig(level=logging.ERROR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDVfvfd5fdxv5565856gfbgfbgvbmLKJLGUIl5tfh5ghTHRGHFGHfg985248202h0tgsfd'


# /////////////////
# ГЛАВНАЯ СТРАНИЦА
# /////////////////
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="KSA")


@app.route('/calc/<int:days>', methods=['GET'])
def calc(days):
    create_plot(days, df, pkl_path, save_path=f"site/static/media/image/{days}.png")
    return jsonify([])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
