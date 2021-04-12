import sqlite3 as sqlite
from flask import current_app, g
from flask.cli import with_appcontext
from webSite.db_create import create_db
import click, os


def init_db():
    db = get_db()
    create_db(db)


# Initialisation de la commande $ flask create-db
@click.command('create-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create the database"""
    if os.path.exists(current_app.config['DATABASE']):
        click.echo('The database already exists, the file has been overwritten')
        os.remove(current_app.config['DATABASE'])
    init_db()
    click.echo('The database has been successfully filled with the data !')


def get_db():
    if 'db' not in g:
        g.db = sqlite.connect(
            current_app.config['DATABASE']
        )
        g.db.row_factory = sqlite.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)