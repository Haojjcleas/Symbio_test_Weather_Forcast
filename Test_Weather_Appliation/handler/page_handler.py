# -*- coding: utf-8 -*-
# Create:       2022-07-29
# Last modify:  2022-07-29
# Author:       Junjie Hao
# Contact:      mail@haojjcleas.net

from flask import render_template
from flask.views import View


class ErrorMsg(View):
    def dispatch_request(self):
        return render_template('404.html')
