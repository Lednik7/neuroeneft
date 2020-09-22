from api_client import NeuroeneftAPI

api = NeuroeneftAPI(API_URL='http://127.0.0.1:10000')
print(api.get_predprice_for_date("2020-10-10"))
print(api.get_predprice_for_period("2020-10-10", "2020-11-10"))