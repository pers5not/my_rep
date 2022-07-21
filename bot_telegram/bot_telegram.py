#!/usr/bin/env python3
import requests
from pprint import pprint



open_weather_token = "640ed18495b76956708530218158f379"
bot_token = "5453264543:AAF5YUJSDpGHCIpmIDExZ1CBjHgRl7pPDCA"


def func(city):
        try:
            result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={open_weather_token}")
            r = result.json()
            pprint(r)
        except Exception:
            print("Error .......")


def main():
    city = input("Введите название города - ")
    func(city)
    

if __name__ == '__main__':
    main()