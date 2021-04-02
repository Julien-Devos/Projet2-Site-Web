from flask import Flask,render_template,request
import os, git


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
    
    # Auto reload for pythonanywhere blablabla
    @app.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('/home/JulienDv/Projet2-Site-Web')
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400

    from . import db_init
    db_init.init_app(app)

    return app

