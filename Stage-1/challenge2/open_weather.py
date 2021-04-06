import requests
import requests_cache
import pandas as pd
import json

API_key = "155b4d6acbf49ae8044c54f654953578"


def get_service_data_by_city_name(service, city_name):
    url = "http://api.openweathermap.org/data/2.5/" + service \
          + "?appid=" + API_key \
          + "&q=" + city_name

    return requests.get(url).json()

# Apr 2019 and March 2020
def get_history(city_name):
    requests_cache.install_cache('ow_history') # creates a cache
    #url = "http://history.openweathermap.org/data/2.5/history/city?q=" + city_name + ",PT&appid=" + API_key
    url = "http://history.openweathermap.org/data/2.5/aggregated/year?q=" + city_name + ",PT&appid=" + API_key \
            + "&start=2019-04-01" \
            + "&end=2020-03-31" \

    return requests.get(url).json()

def testes():
    print("-------------------------------------------------------------------------------------")
    print(get_service_data_by_city_name("weather", "Aveiro"))
    print("-------------------------------------------------------------------------------------")
    print(get_service_data_by_city_name("forecast", "Cascais"))
    print("-------------------------------------------------------------------------------------")
    print(get_service_data_by_city_name("weather", "Alcochete"))
    print("-------------------------------------------------------------------------------------")

def aggregate_per_year(history):
    result = history.get("result")

    val = 0.0
    count = 0.0

    for day in range(len(result)):
        mean = result[day].get("precipitation").get("mean")
        num = result[day].get("precipitation").get("num")

        val = val + (mean*num)
        count = count + num

    return val/count

# ------------------------------
city = "Alcochete"
h = get_history(city)               # vou buscar os dados
# print(h)
h_per_year = aggregate_per_year(h)  # calculo a média para o ano
print(h_per_year)
