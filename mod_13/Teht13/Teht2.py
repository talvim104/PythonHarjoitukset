from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/kentta/<icao>')
def hae_tiedot(icao):

    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='lentopeli',
        user='talvi',
        password='4529m4',
        autocommit=True,
        collation='utf8mb4_unicode_ci'
    )

    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            nimi = rivi[0]
            kaupunki = rivi[1]
            vastaus = f"{icao} - {nimi}, {kaupunki}"
    else:
        vastaus = "Väärä ICAO-koodi."

    kursori.close()
    yhteys.close()

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)