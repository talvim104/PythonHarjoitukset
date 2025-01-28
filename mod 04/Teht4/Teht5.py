oikea_salasana = "rules"
oikea_käyttäjätunnus = "python"
yritukset = 0
while yritukset <= 5:
    login = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")
    if login == oikea_käyttäjätunnus and password == oikea_salasana:
        print("Tervetuloa!")
    yritukset = yritukset + 1
else:
    print("Pääsy evätty!")