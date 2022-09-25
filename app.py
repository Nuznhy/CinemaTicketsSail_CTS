import os

from flask import Flask

app = Flask('CTS')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':

    from waitress import serve
    match os.getenv('FLASK_DEBUG'):
        case "0":
            serve(app, host="0.0.0.0", port=8080)
        case "1":
            app.run()
        case other:
            raise 'Specify FLASK_DEBUG variable'
