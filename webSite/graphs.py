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

@bp.route('/figure_5')
def figure_5():
    db = get_db()
    donnees = []
    for donnee in db.execute('SELECT animaux.sexe, velages.mere_id, velages.date, familles.nom, animaux.mort_ne, animaux.decede FROM velages, '
                             'animaux_velages, animaux, familles WHERE animaux_velages.velage_id = velages.id and '
                             'animaux_velages.animal_id = animaux.id  and familles.id = animaux.famille_id  ORDER BY velages.id'):
        donnees.append(donnee)

    d = {}

    for donnee in donnees:
        sexe, mere_id, date_naiss, nom, mort_ne, decede = donnee[0], donnee[1], donnee[2], donnee[3], donnee[4], donnee[5]
        if nom not in d:
            if sexe == 'F':
                d[nom] = [1, 0, [(mere_id, date_naiss)], 0, mort_ne + decede]
            elif sexe == 'M':
                d[nom] = [0, 1, [(mere_id, date_naiss)], 0, mort_ne + decede]
        else:
            if sexe == 'F':
                d[nom][0] += 1
            elif sexe == 'M':
                d[nom][1] += 1
            if mere_id == d[nom][2][0] and date_naiss == d[nom][2][1]:
                d[nom][3] += 1
            else:
                d[nom][2] = (mere_id, date_naiss)
            d[nom][4] += mort_ne + decede

    d_2 = {}
    for i in d.items():
        d_2[i[0]] = [round(((i[1][0] / (i[1][0]+i[1][1]))*100)), round(((i[1][3] / (i[1][0]+i[1][1]))*100)), round(((i[1][4] / (i[1][0]+i[1][1]))*100))]
    d_2 = {k: v for k, v in sorted(d_2.items(), key=lambda item: item[1][0], reverse=False)}

    data_list = [[], [], [], []]
    for i in d_2.items():
        data_list[0].append(i[0])
        data_list[1].append(i[1][0])
        data_list[2].append(i[1][1])
        data_list[3].append(i[1][2])
    print (data_list)
    return render_template('figure_5.html', data=data_list)