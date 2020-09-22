import requests


class NeuroeneftAPI():
    def __init__(self, API_URL='http://neft,maxa-progy.ru', API_VERSION='v1'):
        self.API_URL = API_URL
        self.API_VERSION = API_VERSION

    def api_query(self, api_method, param={}):
        return requests.get(self.API_URL + '/api/' + api_method, json=param, verify=False).json()

    # Получить прогноз цены на дату
    def get_predprice_for_date(self, date):
        return self.api_query("get_predprice_for_date", {'date': date})

    # Получить список цен на выбранный диапозон дат
    def get_predprice_for_period(self, input_date_start, input_date_end):
        return self.api_query("get_predprice_for_period", {'input_date_start': input_date_start,
                                                           'input_date_end': input_date_start})
