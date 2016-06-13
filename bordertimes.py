from flask import Flask, request, jsonify, render_template, abort
from scraper import scrape

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # to maintain OrderedDict order


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/api')
def all():
    wait_times = scrape()
    if not wait_times:
        abort(400)
    return jsonify(meta=dict(status=200, message='OK'), data=wait_times)


@app.route('/api/list')
def ports():
    wait_times = scrape()
    if not wait_times:
        abort(400)
    return jsonify(meta=dict(status=200, message='OK'),
                   data=sorted(list(wait_times.keys())))


@app.route('/api/<port>')
def single(port):
    try:
        wait_times = scrape(port)
    except KeyError:
        abort(404, {'message': 'Invalid `port` value.'})

    if not wait_times:
        abort(400)

    return jsonify(meta=dict(status=200, message='OK'), data=wait_times)


@app.errorhandler(400)
@app.errorhandler(404)
def bad_request(error):
    status, message = error.code, error.description['message'] or \
        'Couldn\'t retrieve data.'

    response = jsonify(meta=dict(status=status, message=message), data=None)
    return response, error.code

if __name__ == '__main__':
    import os
    port = os.environ.get('PORT', 8000)
    app.run(host='127.0.0.1', port=int(port), debug=True)
