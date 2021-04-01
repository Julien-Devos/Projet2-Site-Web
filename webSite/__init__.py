from flask import Flask,render_template
import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Principal link
    @app.route('/', endpoint='index')
    def index():
        return render_template('index.html')

    from . import db_init
    db_init.init_app(app)

    return app

