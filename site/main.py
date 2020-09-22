import logging
import pandas as pd
from models.utils.plot import plot
from models.utils.pred_model import predictive_model
from flask import Flask, render_template, jsonify, request, make_response
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
        try:
            figure.savefig(save_path)
        except:
            pass
        try:
            figure.savefig(save_path[2:])
        except:
            pass
        try:
            figure.savefig(save_path[1:])
        except:
            pass
    return figure


def get_price(input_data, df, pkl_path):
    model = predictive_model(df).load_pickle(pkl_path)
    model.set_periods(input_data)
    return model.get_pred_price()


def get_range_date(input_date_start, input_date_end, df, pkl_path):
    """
    get_range_date("2020-09-20", "2020-09-30", df, pkl_path)
    """
    model = predictive_model(df).load_pickle(pkl_path)
    delta = (pd.to_datetime(input_date_end) - pd.to_datetime(input_date_start)).days
    model.set_periods(input_date_end)
    forecast = model.predict()
    forecast = forecast[["ds", "yhat"]][-delta:]
    ds, y = forecast["ds"].dt.to_pydatetime(), forecast["yhat"].to_list()
    return [(i, ds[i], y[i]) for i in range(len(ds))]


logging.basicConfig(level=logging.ERROR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDVfvfd5fdxv5565856gfbgfbgvbmLKJLGUIl5tfh5ghTHRGHFGHfg985248202h0tgsfd'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# /////////////////
# ГЛАВНАЯ СТРАНИЦА
# /////////////////
@app.route('/', methods=['GET'])
def index():
    tomorrow_date = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow_pred = get_price(tomorrow_date, df, pkl_path)
    tomorrow_date = tomorrow_date.split('-')
    tomorrow_date = '/'.join(tomorrow_date[1:3] + [tomorrow_date[0]])
    return render_template('index.html', title="KSA", tomorrow_date=tomorrow_date,
                           tomorrow_pred='$ ' + str(round(tomorrow_pred, 4)))


@app.route('/pred', methods=['GET'])
def pred():
    date = request.args.get('date').split('/')
    date = '-'.join([date[2]] + date[0:2])
    pred_price = get_price(date, df, pkl_path)
    return jsonify({'price': '$ ' + str(round(pred_price, 4))})


@app.route('/calc/<int:days>', methods=['GET'])
def calc(days):
    create_plot(days, df, pkl_path, save_path=f"./static/media/image/{days}.png")
    return jsonify([])


# API #
@app.route('/api/get_predprice_for_date', methods=['GET'])
def get_predprice_for_date():
    return jsonify([get_price(request.json['date'], df, pkl_path)])


@app.route('/api/get_predprice_for_period', methods=['GET'])
def get_predprice_for_period():
    return jsonify(get_range_date(request.json['input_date_start'], request.json['input_date_end'], df, pkl_path))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
