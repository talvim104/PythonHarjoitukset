import json
import requests

paikkakunta = input("Anna paikkakunnan nimi: ")

api_key = "1b9f7a6d3ea3538bf0e07f5bf6562743"

pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"

try:
    vastaus = requests.get(pyyntö)

    print("Statuskoodi:", vastaus.status_code)
    print("Tekstivastaus:", vastaus.text)

    if vastaus.status_code == 200:
        data = vastaus.json()
        kuvaus = data["weather"][0]["description"]
        lampotila = data["main"]["temp"] - 273.15
        print("Tässä säätilasi, ole hyvä!")
        print(f"Sää: {kuvaus}")
        print(f"Lämpötila: {lampotila:.1f} °C")
    else:
        print("Paikkakuntaa ei löytynyt. Tarkista nimi.")

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")
