#Asso Eesmäe
#ITS-24
#13.03.25
#Kordamine


# 2. broneeringud.json
# 	Leia, kui palju on broneeringuid teenusele "Massaaž".
# 	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.
# 	Leia kliendid, kelle broneeringud on nädalavahetusel.
# 	Leia päev, millel on kõige rohkem broneeringuid.
# 	Loetle unikaalsed teenused ja mitu korda neid broneeriti.



import requests
import json

#Lehekülg kus fail asub
url = 'https://metshein.com/kordamine/json/broneeringud.json'
response = requests.get(url).json()


# if response.status_code == 200:
    # data = response.json()
massaaž = [b for b in response if b["teenus"] == "Massaaž"]
    # for broneering in data:
    #     if broneering ["teenus" == "Massaaž"]:
print(f"Massaaži bron. arv: {len(massaaž)}")
# else:
#     print(f"Faili alla laadimine ebaõnnestus: {response.status_code}")
