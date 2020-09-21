import logging
import pandas as pd
from models.utils.plot import plot
from models.utils.pred_model import predictive_model
from flask import Flask, render_template


df = pd.read_csv("models/data.csv")
pkl_path = "models/Prophet.pkl"




logging.basicConfig(level=logging.ERROR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDVfvfd5fdxv5565856gfbgfbgvbmLKJLGUIl5tfh5ghTHRGHFGHfg985248202h0tgsfd'


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

# /////////////////
# ГЛАВНАЯ СТРАНИЦА
# /////////////////
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="KSA")

@app.route('/calc', methods=['GET'])
def calc():
    fig = create_plot(7, df, pkl_path, save_path=False)
    print(777)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)