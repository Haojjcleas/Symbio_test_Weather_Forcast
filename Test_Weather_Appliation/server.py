# -*- coding: utf-8 -*-
# Create:       2022-07-29
# Last modify:  2022-07-29
# Author:       Junjie Hao
# Contact:      mail@haojjcleas.net

from flask import Flask
from flask import render_template

from handler.page_handler import ErrorMsg
from handler.api_handler import Greeting, Weather

application = Flask("Hello Word", template_folder='html_template')

application.add_url_rule('/', view_func=ErrorMsg.as_view(''), methods=['GET'])
application.add_url_rule('/api/greeting', view_func=Greeting.as_view(''), methods=['GET'],
                         endpoint='greeting_end_point')
application.add_url_rule('/api/weather', view_func=Weather.as_view(''), methods=['GET'],
                         endpoint='weather_end_point')


# @application.route('/', methods=['GET'])
# def say_hello():
#     return render_template("hello_word.html")


def main():
    application.run(port=5001,
                    ssl_context=(
                        './crt_key/server.crt',
                        './crt_key/server.key'
                    ),
                    debug=True
    )


if __name__ == "__main__":
    main()
