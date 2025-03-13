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



# #	    Leia, kui palju on broneeringuid teenusele "Massaaž".
import requests
import json
import datetime
#Algselt on 0 massaaži
massaaz = 0
#Lehekülg kus fail asub
url = 'https://metshein.com/kordamine/json/broneeringud.json'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # for broneering in data["broneeringud"]:
    #     if broneering["teenus"]=="Massaaž":
    #         massaaz += 1
    # print(massaaz)

# #     Loetle unikaalsed teenused ja mitu korda neid broneeriti.
    # teenused = {}
    # for broneering in data["broneeringud"]:
    #     teenus = broneering["teenus"]
    #     if teenus in teenused:
    #         teenused[teenus] += 1
    #     else:
    #         teenused[teenus] = 1
    # print(teenused)

    
 # #	Leia kõik broneeringud, mis toimuvad pärast kella 12:00.       
    

# tänane kuupäev
    täna = datetime.datetime.now()
# praegune aeg
    praegu = täna.time()
# broneeringud pärast 12:00
    for broneering in data["broneeringud"]:
        aeg = datetime.datetime.strptime(broneering["aeg"], "%H:%M").time()
        if aeg > datetime.time(12, 0):
         print(broneering) 











else:
    print("Päring ebaõnnestus, staatuskood:", response.status_code)