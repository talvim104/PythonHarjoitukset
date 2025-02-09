import mysql.connector

def hae_kentan_tiedot(icao):
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


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    # Huom: käyttäjän root salasana EI saa olla root!!!
    user='root',
    password='root',
    autocommit=True
    )

icao_koodi = input("Anna lentoaseman ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)