import requests
import json

nazev = input("Zadej název subjektu (nebo jeho část): ").strip()

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

response = requests.post(url)

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = json.dumps({
    "obchodniJmeno": nazev
})

response = requests.post(url, headers=headers, data=data)

vysledek = response.json()

pocet = vysledek.get("pocetCelkem", 0)
print(f"Nalezeno subjektů: {pocet}")

for subjekt in vysledek.get("ekonomickeSubjekty", []):
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{jmeno}, {ico}")
