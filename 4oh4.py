from flask import Flask, abort
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '404 not found!'

@app.after_request
def everything_not_found(response):
    response.status_code = 404
    return response


if __name__ == '__main__':

    ip = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = os.environ.get('FLASK_PORT', 5000)

    app.run(port=int(port), host=ip)
