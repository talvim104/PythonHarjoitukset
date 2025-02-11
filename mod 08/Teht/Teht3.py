import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='talvi',
        password='kosm4529m',
        autocommit=True,
        collation='utf8mb4_unicode_ci'
        )

def hae_koordinaatit(icao):
        sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()
        return tulos

airport_1 = input("Anna lentokentän ICAO-koodi: ")
airport_2 = input("Anna toisen lentokentän ICAO-koodi: ")


newport_ri = hae_koordinaatit(airport_1)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).km)