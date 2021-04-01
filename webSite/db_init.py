import sqlite3 as sqlite
from flask import current_app, g
from flask.cli import with_appcontext
from webSite.db_create import create_db
import click


def init_db():
    db = get_db()
    create_db(db)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('The database has been successfully filled with the data !')


def get_db():
    if 'db' not in g:
        g.db = sqlite.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite.PARSE_DECLTYPES
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