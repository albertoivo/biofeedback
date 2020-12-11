import logging
from logging import Formatter, FileHandler

from flask import Flask, jsonify

from hrv.hrv import hrv_bp

APPLICATION_NAME = "app.py"
app = Flask(__name__)

# -------------------------------------------------------------------------- #
# Blueprints register.
# -------------------------------------------------------------------------- #

app.register_blueprint(hrv_bp)


# -------------------------------------------------------------------------- #
# Routes.
# -------------------------------------------------------------------------- #


@app.route('/')
def hello_world():
    """Home."""
    return jsonify('Home')


@app.route('/health')
def health():
    """Health."""
    return jsonify('health')


@app.route('/api/help')
def api_help_json():
    """Print available functions."""

    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


# -------------------------------------------------------------------------- #
# Error handler.
# -------------------------------------------------------------------------- #


@app.errorhandler(Exception)
def errorhandler(e):
    return jsonify({
        'code': str(e.code),
        'name': str(e.name),
        'description': str(e.description)
    }), e.code


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()
