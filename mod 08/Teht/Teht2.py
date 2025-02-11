import mysql.connector
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='talvi',
        password='kosm4529m',
        autocommit=True,
        collation='utf8mb4_unicode_ci'
        )

def hae_tiedot(maatunnus):
    sql = "SELECT type, COUNT(type) FROM airport where iso_country=%s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql,(maatunnus,))
    result = kursori.fetchall()

    if result:
        print("Lentokenttätyypit ja niiden lukumäärä:", result)



maatunnus_2 = input("Anna kentän maatunnus: ")
hae_tiedot(maatunnus_2)