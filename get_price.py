 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_price():

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'symbol':'BTC,ETH',
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'be2617fe-c0cf-462b-97fb-04a01cc62e91',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    return e
