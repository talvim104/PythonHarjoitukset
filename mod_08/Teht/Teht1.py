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

def hae_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on: {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
    return

icao_koodi = input("Anna kentän ICAO-koodi: ")
hae_tiedot(icao_koodi)



