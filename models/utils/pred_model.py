import pickle
import pandas as pd
from datetime import date, timedelta, datetime
import calendar

def next_date(n):
  """
  n принимает значения соотвктствующие:
  days - 3 дня
  week - 7 дней
  month - месяц
  """
  today = date.today()
  if n == "days":
    days = 3
  elif n == "week":
    days = 7
  elif n == "month":
    days = calendar.monthrange(today.year, today.month)[1]
  else:
    current_datetime = datetime.now().date() # дата в системе
    return pd.to_timedelta(f"{n} days") + pd.to_datetime(current_datetime)
  next_month_date_ = today + timedelta(days=days)
  return pd.to_datetime(next_month_date_)


class predictive_model():
    """
    пример использования:
    input_date = "2020-10-14"
    model = predictive_model().load_pickle()
    model.set_periods(input_date) #создает датафрейм для предсказания
    model.get_pred_price() #возвращает цену на заданный день
    week = model.plot_for_weekend() #возвращает forecast(предсказание)
    model.plot() #строит грфик и возращает его
    model.plot_components() #строит грфик и возращает его
    """

    def __init__(self, data):
        self.model = None  # модель
        self.data = data  # данные
        self.periods = None  # кол-во дней для создания датафрейма
        self.future = None  # датафрейм для предсказания
        self.forecast = None  # предсказанный датафрейм
        self.pred_price = None  # предсказанная цена
        self.input_date = None  # дата пользователя
        self.last_date = None  # последняя дата в данных

    def load_pickle(self, pkl_path="./Prophet.pkl"):
        self.model = pickle.load(open(pkl_path, 'rb'))  # загружаем модель
        return self

    def get_periods(self, input_date):
        self.input_date = input_date
        self.last_date = self.data["ds"][-1:].values  # последняя дата записи в данных
        delta = pd.to_datetime(input_date) - pd.to_datetime(self.last_date)  # разница между датами в днях
        periods = delta.days[0]  # число, кол-во дней для предсказания
        return periods

    def set_periods(self, input_date):
        self.input_date = input_date
        self.last_date = self.data["ds"][-1:].values  # последняя дата записи в данных
        delta = pd.to_datetime(input_date) - pd.to_datetime(self.last_date)  # разница между датами в днях
        self.periods = delta.days[0]  # число, кол-во дней для предсказания
        self.future = self.model.make_future_dataframe(periods=self.periods)

    def predict(self):
        self.forecast = self.model.predict(self.future)  # предсказание
        return self.forecast

    def get_pred_price(self):
        self.forecast = self.model.predict(self.future)  # предсказание
        self.pred_price = self.forecast["yhat"][-1:].values[0]  # предсказание на заданный день
        return self.pred_price

    def plot_for_weekend(self):
        self.last_date = self.data["ds"][-1:].values  # последняя дата записи в данных
        current_datetime = datetime.now().date()  # дата в системе
        delta = pd.to_timedelta("7 days") + pd.to_datetime(current_datetime) - pd.to_datetime(
            self.last_date)  # кол-во дней для предсказания на 7 дней вперед
        self.future = self.model.make_future_dataframe(periods=delta.days[0])  # создание датафрейма для предсказания
        self.forecast = self.model.predict(self.future)  # само предсказание
        return self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper', "trend"]]

    def save_model(self, pkl_path="./Prophet.pkl", frcst_path="./forecast.pkl"):  # сохраняем файлы модели
        with open(pkl_path, "wb") as f:
            pickle.dump(self.model, f)

        self.forecast.to_pickle(pkl_path)


    def plot(self, save=False, path="./figure.jpeg"):  # график
        fig = self.model.plot(self.forecast)
        if save:
            fig.savefig(path)
        return fig

    def plot_components(self, save=False, path="./figure.jpeg"):  # грфик тренда
        fig = self.model.plot_components(self.forecast)
        if save:
            fig.savefig(path)
        return fig
