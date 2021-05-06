import platform

def create_db(db):

    inserts = ['animaux_data.sql','animaux_types_data.sql','animaux_velages_data.sql','complications_data.sql',
               'familles_data.sql','types_data.sql','velages_data.sql','velages_complications_data.sql']

    sql_insert = open('webSite/sql-data/schema.sql')
    sql_as_string = sql_insert.read()
    db.executescript(sql_as_string)
    print("The database has been initialized")

    for insert in inserts:

        if platform.system() == "Windows":
            print("\r- Inserting '{}' into the database [".format(insert) + ' ... ' + "]")
            sql_insert = open('webSite/sql-data/' + str(insert), encoding='utf-8')
            db.executescript(sql_insert.read())
            print("\r- Inserting '{}' into the database [".format(insert) + ' DONE ' + "]", end="\n")
        else:


print(platform.system(),platform.release(),platform.version())