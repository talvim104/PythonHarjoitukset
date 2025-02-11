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
