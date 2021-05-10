from webSite.db_init import get_db
from datetime import date, datetime
from . import moon


def figure1():
    db = get_db()

    velages = []
    for velage in db.execute('SELECT velages.date FROM velages ORDER BY velages.id'):
        velages.append(velage)

    d = {'New Moon': 0, 'Waxing Crescent': 0, 'First Quarter': 0, 'Waxing Gibbous': 0, 'Full Moon': 0,
         'Waning Gibbous': 0, 'Last Quarter': 0, 'Waning Crescent': 0}
    for dates in velages:
        dateSplit = dates[0].split("/")
        date = datetime(int(dateSplit[2]), int(dateSplit[1]), int(dateSplit[0]))
        moonPhase = moon.phase(date)
        d[moonPhase] += 1

    data = []
    for phaseCount in d.keys():
        data.append(d[phaseCount])

    return data


def figure2():
    db = get_db()

    data_from_db = []
    for dcd in db.execute('SELECT animaux.mort_ne, velages.date FROM velages, '
                          'animaux_velages, animaux WHERE animaux_velages.velage_id = velages.id and '
                          'animaux_velages.animal_id = animaux.id ORDER BY velages.id'):
        data_from_db.append(dcd)
    # print(data_from_db[1][1])
    data_3 = [[] for i in range(1, 13)]
    for i in range(len(data_from_db)):
        new_date = data_from_db[i][1].split("/")
        # print(new_date)
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

    return data_3


def figure3():
    db = get_db()

    velages = []
    for velage in db.execute('SELECT animaux.mort_ne, animaux.decede, familles.nom FROM velages, animaux_velages, animaux,'
                             'familles WHERE animaux_velages.velage_id = velages.id and animaux_velages.animal_id = '
                             'animaux.id  and familles.id = animaux.famille_id  ORDER BY velages.id'):
        velages.append(velage)

    Data = {}
    for velage in velages:
        # Schéma du dictionnaire {'nom_famille': ['nb_vivant','nb_mort_ne','nb_mort_prem']'}
        mort_ne, decede, nom = velage[0], velage[1], velage[2]
        if nom == 'Myrtille':
            print(mort_ne,decede)
        if nom not in Data:
            if mort_ne == 0 and decede == 0:
                Data[nom] = [1, 0, 0]
            else:
                Data[nom] = [0, mort_ne, decede]
        else:
            if mort_ne == 0 and decede == 0:
                Data[nom][0] += 1
            elif mort_ne == 1 and decede == 0:
                Data[nom][1] += 1
            elif mort_ne == 0 and decede == 1:
                Data[nom][2] += 1

    for family_name in Data.keys():
        nb_vivant = Data[family_name][0]
        nb_mort_ne = Data[family_name][1]
        nb_mort_prem = Data[family_name][2]
        vel_total = nb_vivant + nb_mort_ne + nb_mort_prem

        if family_name == 'Myrtille':
            print(family_name,nb_vivant,nb_mort_ne,nb_mort_prem)

        Data[family_name][0] = round((nb_vivant * 100) / vel_total,2)
        Data[family_name][1] = round((nb_mort_ne * 100) / vel_total,2)
        Data[family_name][2] = round((nb_mort_prem * 100) / vel_total,2)
        Data[family_name].append(vel_total)

    # Sort the data
    Data = {k: v for k, v in sorted(Data.items(), key=lambda item: item[1][1], reverse=True)}

    data_lst = [[], [], [], [], []]
    for nom in Data:
        data_lst[0].append(nom)
        data_lst[1].append(Data[nom][0])
        data_lst[2].append(Data[nom][1])
        data_lst[3].append(Data[nom][2])
        data_lst[4].append(Data[nom][3])

    return data_lst


def figure4():
    # db = get_db()
    # infor= []
    # for infos in db.execute('SELECT animaux.decede, familles.nom, velages.date, complications.complication FROM velages, '
    #                              'animaux_velages, animaux, familles, complications, velages_complications WHERE animaux_velages.velage_id = velages.id and '
    #                              'animaux_velages.animal_id = animaux.id and velages_complications.velage_id = velages.id '
    #                              'and complications.id = velages_complications.complication_id and familles.id = animaux.famille_id ORDER BY velages.id'):
    #     infor.append(infos)
    # dico= {}
    # for info in infor:
    #     day, month, year = int(info[2].split('/')[0]), int(info[2].split('/')[1]), int(info[2].split('/')[2])
    #     decede, nom, d, complications = info[0], info[1], date(year, month, day), info[3]
    #     if nom not in dico:
    #         if decede == 0:
    #             dico[nom] = [1, 0, d, d]
    #         else:
    #             dico[nom] = [0, decede, d, d]
    #     else:
    #         if d < dico[nom][2]:
    #             dico[nom][2] = d
    #         elif d > dico[nom][3]:
    #             dico[nom][3] = d
    #         if decede == 0:
    #             dico[nom][0] += 1
    #         else:
    #             dico[nom][1] += 1
    #
    # for data in dico.keys():
    #     dico[data][2] = (dico[data][3] - dico[data][2]).days / 365
    #     dico[data].pop()
    #     if dico[data][2] != 0:
    #         dico[data][0] = round(dico[data][0] / dico[data][2], 4)
    #         dico[data][1] = round(dico[data][1] / dico[data][2], 4)
    #     dico[data].append(dico[data][0] + dico[data][1])
    #
    # dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[1][4], reverse=True)}
    #
    # data_liste = [[], [], [], []]
    # for nom in dico:
    #     data_liste[0].append(nom)
    #     data_liste[1].append(dico[nom][0])
    #     data_liste[2].append(dico[nom][1])
    #     data_liste[3].append(dico[nom][2])

    return None


def figure5():
    """
    Calcule les taux de vaches femelles, de jumeaux, et de morts prématurés pour chaque famille.
    """
    # Requête vers la base de donnée SQL pour aller prendre les valeurs nécessaires à nos calculs
    db = get_db()
    donnees = []
    for donnee in db.execute(
            'SELECT animaux.sexe, velages.mere_id, velages.date, familles.nom, animaux.mort_ne, animaux.decede FROM velages, '
            'animaux_velages, animaux, familles WHERE animaux_velages.velage_id = velages.id and '
            'animaux_velages.animal_id = animaux.id  and familles.id = animaux.famille_id  ORDER BY velages.id'):
        donnees.append(donnee)

    # Création du dictionnaire qui servira de répertoire
    d = {}

    # Boucle pour parcourir les valeurs des vaches une par une
    for donnee in donnees:
        # Attribution de nom de variables pour chauque valeur
        sexe, mere_id, date_naiss, nom, mort_ne, decede = donnee[0], donnee[1], donnee[2], donnee[3], donnee[4], donnee[5]

        # Si la famille n'est pas encore dans le repertoire, on l'ajoute sous la forme suivante:
        # d[nom] = [Nbre de vaches total, Nbre de femelles, (id de la mère et date de maissance du dernier veau né),...
        # ... Nbre de jumeaux au total, Série de jumeaux, Nbre de morts prématurés]
        if nom not in d:
            # Vérifie si la première vache est femelle
            if sexe == 'F':
                d[nom] = [1, 1, (mere_id, date_naiss), 0, 0, mort_ne + decede]
            else:
                d[nom] = [1, 0, (mere_id, date_naiss), 0, 0, mort_ne + decede]

        # Si la famille est déjà dans le dictionnaire, on:
        else:
            # Ajoute une vache au total
            d[nom][0] += 1
            # Si c'est une femelle, on l'ajoute au total
            if sexe == 'F':
                d[nom][1] += 1
            # Vérifie si le dernier veau né a la même mère et la même date de naissance
            if mere_id == d[nom][2][0] and date_naiss == d[nom][2][1]:
                # Si c'est le cas, on regarde si il y avait d'autres veaux jumeaux avant
                if d[nom][4] == 0:
                    # Si c'est les premiers jumeaux de la série, on ajoute 2 au total des jumeaux et on set 1 à la
                    # variable qui détermine si ils sont en série
                    d[nom][3] += 2
                    d[nom][4] = 1
                else:
                    # Si il y a une série de jumeaux déjà en cours, l'on ajoute juste 1 au compteur de jumeaux
                    d[nom][3] += 1
            # Si le dernier veau de la famille n'est pas jumeau avec le current, l'on set la nouvelle date de naissance
            # comme réference et l'on set la série de jumeaux à 0.
            else:
                d[nom][2] = (mere_id, date_naiss)
                d[nom][4] = 0
            # On ajoute ici les morts prématurés si c'est le cas
            d[nom][5] += mort_ne + decede

    # On va maintenant calculer les taux pour chaque famille à partir des valeurs récoltés et les mettre dans d_2
    d_2 = {}
    # d_2 aura la forme : { Nom: [Taux de femelles, Taux de jumeaux, Taux de mort préma], ... }
    for i in d.items():
        d_2[i[0]] = [round(((i[1][1] * 100)/ i[1][0]), 2), round(((i[1][3] * 100)/i[1][0]), 2),
                     round(((i[1][4] * 100)/ i[1][0]), 2), i[1][0]]
        # On additionne les taux obtenus pour pouvoir trier le graphique par leur somme
        d_2[i[0]].append((d_2[i[0]][0] + d_2[i[0]][1] + d_2[i[0]][2]))

    # On trie les familles par la somme de leur 3 taux
    d_2 = {k: v for k, v in sorted(d_2.items(), key=lambda item: item[1][3], reverse=False)}

    # On forme ici la liste qu'on va retourner
    data_list = [[], [], [], [], []]
    for i in d_2.items():
        data_list[0].append(i[0])  # Nom de la famille
        data_list[1].append(i[1][0])  # Taux de femelles
        data_list[2].append(i[1][1])  # Taux de jumeaux
        data_list[3].append(i[1][2])  # Taux de morts prématurés
        data_list[4].append(i[1][3])  # Nombre de vaches total de la famille

    return data_list
