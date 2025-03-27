import json
import requests

aloitus = input("Paina ENTER, jos haluat Chuck Norrisin vitsin")

#haetaan json- dataa
pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    #lähetetään pyyntö nettiin ja sadaan vastaus
    vastaus = requests.get(pyyntö)
    #testataan oliko status koodi OK (=200)
    if vastaus.status_code==200:
        #mutetaan saatu data python sanakirja muotoiseksi
        json_vastaus = vastaus.json()
        print("Tässä vitsisi, ole hyvä!")
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")