from flask import Flask, request

from application.message_processor import MessageProcessor
from excepts.illegal_request_exception import IllegalRequestException

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/message')
def message():
    return 'hello'


@app.route('/autoBot', methods=['POST'])
def auto_bot():
    try:
        return MessageProcessor(request.headers, request.json).process()
    except IllegalRequestException as ex:
        return ex.message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
