import requests
import json

url =' http://api.weatherapi.com/v1/history.json?key=91527cfed8b8479f80e214050232911&q=Dallas&dt=2023-11-24&end_dt=2023-11-30'


response=requests.get(url).json()
w=response['forecast']
hourly
