from flask import Flask,render_template,request,redirect,url_for
import os, git


def styleSheet():
    stylesheet = "/static/styles/light_theme.css"
    if request.cookies.get('darktheme') == 'True':
        stylesheet = "/static/styles/dark_theme.css"
    return stylesheet

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

    # On every reload ... do this
    @app.before_request
    def before_request():
        global stylesheet
        stylesheet = styleSheet()

    # Allows to render the favicon in all the website
    @app.route('/favicon.ico')
    def favicon():
        return redirect(url_for('static',filename='img/logo.ico'))

    # Principal link
    @app.route('/', endpoint='index')
    def index():
        return render_template('index.html',style=stylesheet)

    # Auto reload for pythonanywhere
    @app.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('/home/JulienDv/Projet2-Site-Web')
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html',style=stylesheet)

    from webSite import db_init
    db_init.init_app(app)

    from . import pages
    app.register_blueprint(pages.bp)

    return app