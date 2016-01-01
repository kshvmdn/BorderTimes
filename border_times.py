import os

from flask import Flask, request, jsonify, render_template, abort
from scraper import scrape

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/api')
def api():
    port_name = request.args.get("port", type=str)
    wait_times = scrape() if port_name is None or port_name == '' else scrape(port_name)

    if wait_times:
        response = jsonify(meta=dict(status=200, message='OK'), data=wait_times)
    else:
        abort(400)
    return response


@app.errorhandler(400)
def bad_request(error):
    response = jsonify(meta=dict(status=error.code, message=error.message))
    return response, error.code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='127.0.0.1', port=port)
