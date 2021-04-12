from flask import Blueprint,render_template
from webSite.db_init import get_db

bp = Blueprint('graphs', __name__)

@bp.route('/graph')
def graph():
    db = get_db()

    velages = []
    for velage in db.execute('SELECT animaux.mort_ne, animaux.decede, familles.nom, velages.date FROM velages, '
                             'animaux_velages, animaux, familles WHERE animaux_velages.velage_id = velages.id and '
                             'animaux_velages.animal_id = animaux.id  and familles.id = animaux.famille_id  ORDER BY velages.id'):
        velages.append(velage)


    return render_template('graph.html',velage=velages)