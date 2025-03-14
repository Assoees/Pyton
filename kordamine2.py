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

# impordime request mooduli, HTTP päringute tegemiseks
import requests
# Impordime json, json failide lugemise
import json
# Impordime aja mooduli
import datetime

#Lehekülg kus fail asub
url = 'https://metshein.com/kordamine/json/broneeringud.json'
#Kontrollib lehekülje kättesaadavust
response = requests.get(url)
#Kui lehekülg on kättesaadav
if response.status_code == 200:
# Võtab andmed lehelt ja teeb (.json()) need pytonis kasutatavaks andmeteks, listiks/loendiks
    data = response.json()

# # #------------------------- ülemine jääb, alumist saab võtta välja kommentaarist    

#     #Algselt on 0 massaaži
#     massaaz = 0
# # # Käib loendi läbi (broneering asemel võib olla mis iganes sõna/täht)
#     for broneering in data["broneeringud"]:
# # Otsitakse teenuseid ja kui teenuseks on massaaž siis lisatakse +1
#         if broneering["teenus"]=="Massaaž":
#             massaaz += 1
# # Väljastab vastuse
#     print(massaaz)

# # #-----------------------------------

# #     Loetle unikaalsed teenused ja mitu korda neid broneeriti.

# Tühja sõnastiku loomine
    teenused = {}
# Käib loendi läbi (broneering asemel võib olla mis iganes sõna/täht)
    for broneering in data["broneeringud"]:
# Defineerime millele vastab teenus loetavas failis
        teenus = broneering["teenus"]
# Käib läbi faili ja otsib sealt välja teenus
        if teenus in teenused:
# Kui teenus leiti siis lisatakse +1 lõpp vastusele
            teenused[teenus] += 1
# Kui ei leitud siis aaab teenus endale väärtuseks 1
        else:
            teenused[teenus] = 1
# Väljastab vastuse
    print(teenused)

# # #-------------------------------------------------
    
# # Leia kõik broneeringud, mis toimuvad pärast kella 12:00.       

# # Käib loendi läbi (broneering asemel võib olla mis iganes sõna/täht)
#     for broneering in data["broneeringud"]:
# # Võtame ainult tunnid ja minutid
#         aeg = datetime.datetime.strptime(broneering["aeg"], "%H:%M").time()
# # Kui aeg on suurem kui 1200, siis väljastab selle vastusena
#         if aeg > datetime.time(12, 0):
# # Väljastab vastuse
#          print(broneering) 










# # kui lehekülg ei vasta prindib antud välja koos, ebaõnnestumise koodiga
else:
    print("Päring ebaõnnestus, staatuskood:", response.status_code)