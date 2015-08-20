from flask import Flask, abort
import os

app = Flask(__name__)

@app.errorhandler(404)
def handle_all_things(e):
    return '404 not found!', 404


@app.route('/')
def hello_world():
    abort(404)


if __name__ == '__main__':

    ip = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = os.environ.get('FLASK_PORT', 5000)

    app.run(port=int(port), host=ip)
