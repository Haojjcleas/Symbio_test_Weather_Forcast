# -*- coding: utf-8 -*-
# Create:       2022-07-29
# Last modify:  2022-07-29
# Author:       Junjie Hao
# Contact:      mail@haojjcleas.net

class InsufficientParameterException(Exception):
    def __init__(self, handler, msg='Insufficient Parameter Exception',):
        self.msg = msg
        handler.msg = {"code": "503", "msg": msg}

    def __str__(self):
        return f'{self.msg}'


class CityNameNotRecordException(Exception):
    def __init__(self, handler, city_name="", msg='City Name Not in Record'):
        self.msg = msg
        self.city_name = city_name
        handler.msg = {"code": "503", "msg": msg}

    def __str__(self):
        return f'{self.msg},City name:{self.city_name}'


class UnknownFormatException(Exception):
    def __init__(self, handler, msg='Unknown Format'):
        self.msg = msg
        handler.msg = {"code": "503", "msg": msg}
