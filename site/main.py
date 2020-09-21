import logging
import pandas as pd
from models.utils.plot import plot
from models.utils.pred_model import predictive_model
from flask import Flask, render_template, jsonify, request
import datetime
from datetime import timedelta

try:
    df = pd.read_csv("../models/data.csv")
    pkl_path = "../models/Prophet.pkl"
except:
    df = pd.read_csv("models/data.csv")
    pkl_path = "models/Prophet.pkl"


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

def get_price(input_data, df, pkl_path):
    model = predictive_model(df).load_pickle(pkl_path)
    model.set_periods(input_data)
    return model.get_pred_price()

logging.basicConfig(level=logging.ERROR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDVfvfd5fdxv5565856gfbgfbgvbmLKJLGUIl5tfh5ghTHRGHFGHfg985248202h0tgsfd'


# /////////////////
# ГЛАВНАЯ СТРАНИЦА
# /////////////////
@app.route('/', methods=['GET'])
def index():
    tomorrow_date = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow_pred = get_price(tomorrow_date, df, pkl_path)
    tomorrow_date = tomorrow_date.split('-')
    tomorrow_date = '/'.join(tomorrow_date[1:3] + [tomorrow_date[0]])
    return render_template('index.html', title="KSA", tomorrow_date=tomorrow_date, tomorrow_pred = tomorrow_pred)

@app.route('/pred', methods=['GET'])
def pred():
    date = request.args.get('date').split('/')
    date = '-'.join([date[2]] + date[0:2])
    pred_price = get_price(date, df, pkl_path)
    return jsonify({'price': pred_price})

@app.route('/calc/<int:days>', methods=['GET'])
def calc(days):
    create_plot(days, df, pkl_path, save_path=f"static/media/image/{days}.png")
    return jsonify([])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
