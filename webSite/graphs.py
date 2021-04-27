from flask import Blueprint,render_template
from webSite.db_init import get_db
from datetime import date,datetime
from webSite.__init__ import styleSheet
from . import moon

bp = Blueprint('graphs', __name__)

# On every reload check wich style to use
@bp.before_request
def before_request():
    global stylesheet
    stylesheet = styleSheet()

@bp.route('/figure1_1')
def figure1_1():
    db = get_db()

    velages = []
    for velage in db.execute('SELECT velages.date FROM velages ORDER BY velages.id'):
        velages.append(velage)

    d = {'New Moon': 0,'Waxing Crescent': 0,'First Quarter': 0,'Waxing Gibbous': 0,'Full Moon': 0,'Waning Gibbous': 0,'Last Quarter': 0,'Waning Crescent': 0}
    for dates in velages:
        dateSplit = dates[0].split("/")
        date = datetime(int(dateSplit[2]),int(dateSplit[1]),int(dateSplit[0]))
        moonPhase = moon.phase(date)
        d[moonPhase] += 1

    data = []
    for phaseCount in d.keys():
        data.append(d[phaseCount])
    print(data)

    return render_template('figure1_1.html',style=stylesheet,data=data)


@bp.route('/figure3_1')
def figure3_1():
    db = get_db()

    data_from_db = []
    for dcd in db.execute('SELECT animaux.mort_ne, velages.date FROM velages, '
                                 'animaux_velages, animaux WHERE animaux_velages.velage_id = velages.id and '
                                 'animaux_velages.animal_id = animaux.id ORDER BY velages.id'):
        data_from_db.append(dcd)

    #print(data_from_db[1][1])
    data_3 = [[] for i in range(1,13)]
    for i in range(len(data_from_db)) :
        new_date = data_from_db[i][1].split("/")
        #print(new_date)
        if int(new_date[1]) == 1:
            data_3[0].append(data_from_db[i][0])
        if int(new_date[1]) == 2:
            data_3[1].append(data_from_db[i][0])
        if int(new_date[1]) == 3:
            data_3[2].append(data_from_db[i][0])
        if int(new_date[1]) == 4:
            data_3[3].append(data_from_db[i][0])
        if int(new_date[1]) == 5:
            data_3[4].append(data_from_db[i][0])
        if int(new_date[1]) == 6:
            data_3[5].append(data_from_db[i][0])
        if int(new_date[1]) == 7:
            data_3[6].append(data_from_db[i][0])
        if int(new_date[1]) == 8:
            data_3[7].append(data_from_db[i][0])
        if int(new_date[1]) == 9:
            data_3[8].append(data_from_db[i][0])
        if int(new_date[1]) == 10:
            data_3[9].append(data_from_db[i][0])
        if int(new_date[1]) == 11:
            data_3[10].append(data_from_db[i][0])
        if int(new_date[1]) == 12:
            data_3[11].append(data_from_db[i][0])

    for i in range(len(data_3)):
        data_3[i] = sum(data_3[i])
    print(data_3)

    return render_template('figure3_1.html',style=stylesheet, data_3=data_3)


@bp.route('/figure3_2')
def figure3_2():
    db = get_db()

    velages = []
    for velage in db.execute('SELECT animaux.mort_ne, animaux.decede, familles.nom, velages.date FROM velages, '
                                 'animaux_velages, animaux, familles WHERE animaux_velages.velage_id = velages.id and '
                                 'animaux_velages.animal_id = animaux.id  and familles.id = animaux.famille_id  ORDER BY velages.id'):
        velages.append(velage)

    Data = {}
    for velage in velages:
        # Schéma du dictionnaire {'nom_famille': ['nb_vivant','nb_mort_ne','nb_mort_prem,'MinDate','MaxDate']'}
        day, month, year = int(velage[3].split('/')[0]), int(velage[3].split('/')[1]), int(velage[3].split('/')[2])
        mort_ne, decede, nom, d = velage[0], velage[1], velage[2], date(year, month, day)
        if nom not in Data:
            if mort_ne == 0 and decede == 0:
                Data[nom] = [1, 0, 0, d, d]
            else:
                Data[nom] = [0, mort_ne, decede, d, d]
        else:
            if d < Data[nom][3]:
                Data[nom][3] = d
            elif d > Data[nom][4]:
                Data[nom][4] = d
            if mort_ne == 0 and decede == 0:
                Data[nom][0] += 1
            elif mort_ne == 1 and decede == 0:
                Data[nom][1] += 1
            else:
                Data[nom][2] += 1

    for data in Data.keys():
        Data[data][3] = (Data[data][4] - Data[data][3]).days / 365
        Data[data].pop()
        if Data[data][3] != 0:
            Data[data][0] = round(Data[data][0] / Data[data][3], 4)
            Data[data][1] = round(Data[data][1] / Data[data][3], 4)
            Data[data][2] = round(Data[data][2] / Data[data][3], 4)
        Data[data].append(Data[data][0] + Data[data][1] + Data[data][2])

    # Sort the data
    Data = {k: v for k, v in sorted(Data.items(), key=lambda item: item[1][4], reverse=True)}

    data_lst = [[], [], [], [], []]
    for nom in Data:
        data_lst[0].append(nom)
        data_lst[1].append(Data[nom][0])
        data_lst[2].append(Data[nom][1])
        data_lst[3].append(Data[nom][2])
        data_lst[4].append(Data[nom][4])

    return render_template('figure3_2.html',data=data_lst,style=stylesheet)


@bp.route('/figure4_2')
def figure4_2():
    return render_template('figure4_2.html',style=stylesheet)


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
                d[nom] = [1, 0, [(mere_id, date_naiss)], 0, mort_ne + decede, 1, 0]
            elif sexe == 'M':
                d[nom] = [0, 1, [(mere_id, date_naiss)], 0, mort_ne + decede, 1, 0]
        else:
            if sexe == 'F':
                d[nom][0] += 1
            elif sexe == 'M':
                d[nom][1] += 1
            if mere_id == d[nom][2][0] and date_naiss == d[nom][2][1]:
                if d[nom][6] == 0:
                    d[nom][3] = 2
                    d[nom][6] += 1
                else:
                    d[nom][3] += 1
            else:
                d[nom][2] = (mere_id, date_naiss)
            d[nom][4] += mort_ne + decede
            d[nom][5] += 1

    d_2 = {}
    for i in d.items():
        d_2[i[0]] = [round(((i[1][0] / i[1][5])*100)), round(((i[1][3] / i[1][5])*100)), round(((i[1][4] / i[1][5])*100)), i[1][5]]
        d_2[i[0]].append((d_2[i[0]][0]+d_2[i[0]][1]+d_2[i[0]][2]))
    d_2 = {k: v for k, v in sorted(d_2.items(), key=lambda item: item[1][3], reverse=False)}

    data_list = [[], [], [], [], []]
    for i in d_2.items():
        data_list[0].append(i[0])
        data_list[1].append(i[1][0])
        data_list[2].append(i[1][1])
        data_list[3].append(i[1][2])
        data_list[4].append(i[1][3])
    return render_template('figure_5.html', data=data_list,style=stylesheet)