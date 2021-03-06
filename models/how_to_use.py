# read the Prophet model object
import pickle
import pandas as pd

pkl_path = "Prophet.pkl"

with open(pkl_path, 'rb') as f:
    model = pickle.load(f)

forecast = pd.read_pickle(pkl_path)

df = pd.read_csv("data.csv")

last_date = df["ds"][-1:].values
now_date = "2020-10-19"
delta = pd.to_datetime(now_date) - pd.to_datetime(last_date)
periods = delta.days[0]

future = model.make_future_dataframe(periods=periods)
future.tail()

forecast = model.predict(future)
"""
yhat - предсказанное значение
yhat_lower/yhat_upper - диапазон
"""
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()  # tail(number=5) - выводит последние строки

fig1 = model.plot(forecast)

fig2 = model.plot_components(forecast)

print(forecast["yhat"][-1:].values[0])  # предсказанное значение
