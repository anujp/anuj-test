from flask import Flask, request
import requests
import logging
from logging.handlers import RotatingFileHandler
application = Flask(__name__)


@application.route('/')
def dashboard():
    result = requests.get('http://0.0.0.0:5001/hardware/').json()
    hardware = [
        '{} - {}: {}'.format(r['provider'], r['name'], r['availability'])
        for r in result
    ]

    return '<br>'.join(hardware)


if __name__ == "__main__":
    logHandler = RotatingFileHandler('portal.log', maxBytes=1000, backupCount=1)

    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    application.logger.setLevel(logging.INFO)

    application.logger.addHandler(logHandler)

    application.run(host='0.0.0.0', port=5000)
