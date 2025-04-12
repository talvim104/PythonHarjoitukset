from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/testiyhteys')
def testaa_yhteys():
    try:
        yhteys = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='lentopeli',
            user='talvi',
            password='4529m4',
            autocommit=True,
            collation='utf8mb4_unicode_ci'
        )

        if yhteys.is_connected():
            return "Yhteys tietokantaan onnistui!"
        else:
            return "Ei saatu yhteyttä tietokantaan."

    except Error as e:
        return f"❌ Virhe tietokantayhteydessä: {e}"

    finally:
        try:
            yhteys.close()
        except:
            pass

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
