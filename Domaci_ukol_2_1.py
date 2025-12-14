import requests

ico = input("Zadej IČO subjektu: ").strip()

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"
url = url.replace("ICO", ico)

response = requests.get(url)

data = response.json()

obchodni_jmeno = data.get("obchodniJmeno")
sidlo = data.get("sidlo", {})
adresa = sidlo.get("textovaAdresa")
if obchodni_jmeno and adresa:
    print(obchodni_jmeno)
    print(adresa)
else:
    print("Informace nebyly nalezeny.")
