import os

from flask import Flask
from url_compressor.config import config

def create_app(environment='default'):
    app = Flask(__name__, instance_relative_config=True)

    configuration = config.get(environment, 'default')
    app.config.from_object(configuration)
    # configuration.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_pyfile('application.cfg', silent=True)

    print(app.config)

    from url_compressor import view
    app.register_blueprint(view.bp)

    return app
