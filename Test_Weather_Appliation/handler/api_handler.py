# -*- coding: utf-8 -*-
# Create:       2022-07-29
# Last modify:  2022-07-30
# Author:       Junjie Hao
# Contact:      mail@haojjcleas.net

from handler.exception import *
from flask.views import View
from flask import request
import requests
import json

with open('./City_Code.json') as jo:
    CITY_CODE_DIC = json.load(jo)


class Greeting(View):

    def dispatch_request(self):
        return 'hello word from my first flask api'

    def greeting_end_point(self):
        return


class Weather(View):
    base_url = 'http://t.weather.sojson.com/api/weather/city'

    WEATHER_CHN_ENG = {
        "多云": "Partly Cloudy",
        "小雨": "Light Rain",
        "中雨": "moderate rain",
        "大雨": "heavy rain",
        "暴雨": "rainstorm",
        "雷阵雨": "Scattered Thunderstorms",
        "阴": "Cloudy",
        "晴": "Sunny"
    }

    def __init__(self):
        super(Weather, self).__init__()
        self.city_code = None
        self.resp = None
        self.msg = ""

    def _translate(self):
        for character, replacement in self.WEATHER_CHN_ENG.items():
            self.weather = self.weather.replace(character, replacement)
        return

    def _fetch_weather_info(self):
        try:
            self.resp = requests.get(f'{self.base_url}/{self.city_code}').text
        except:
            raise InsufficientParameterException()
        try:
            self.weather = str(json.loads(self.resp)['data']['forecast']).replace("'", "\"").replace("高温", "").replace("低温", "").replace("℃", "").replace("级", " Level")
        except KeyError:
            raise UnknownFormatException()

    def _require_city(self):
        try:
            self.city = request.args.get('city').lower()
        except:
            raise InsufficientParameterException

    def _get_city_code(self):
        self.city_code = CITY_CODE_DIC[self.city]

    def dispatch_request(self):
        self._require_city()
        try:
            self._get_city_code()
            self._fetch_weather_info()
            self._translate()
            self.msg = self.weather
        except KeyError:
            raise CityNameNotRecordException(handler=self, city_name=self.city)

        except Exception as e:
            self.msg = e
        finally:
            return self.msg

    def weather_end_point(self):
        return
