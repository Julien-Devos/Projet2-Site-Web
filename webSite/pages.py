from flask import Blueprint, render_template,send_from_directory
from webSite.__init__ import styleSheet
import webSite.graphs as figures
import os

bp = Blueprint('pages', __name__)


# On every reload check wich style to use
@bp.before_request
def before_request():
    global stylesheet
    stylesheet = styleSheet()

@bp.route('/figure1')
def figure1():

    graph_data = figures.figure1()

    return render_template('figure1.html', style=stylesheet, data=graph_data)


@bp.route('/figure2')
def figure2():

    graph_data = figures.figure2()

    return render_template('figure2.html', style=stylesheet, data=graph_data)


@bp.route('/figure3')
def figure3():

    graph_data = figures.figure3()

    return render_template('figure3.html', style=stylesheet, data=graph_data)


@bp.route('/figure4')
def figure4():

    graph_data = figures.figure4()

    return render_template('figure4.html', style=stylesheet, data="TODO")


@bp.route('/figure5')
def figure5():

    graph_data = figures.figure5()

    return render_template('figure5.html', style=stylesheet, data=graph_data)