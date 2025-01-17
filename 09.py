# Ülesanne 09
#Asso Eesmäe
# 17.01.2025
# Kuna tsüklid on oluline osa programmeerimisel, siis on oluline mõista selle kasutamist. Seepärast leiad natuke pikema nimekirja ülesannetega.

# # Genereeri ja kuva arvud arvud 1-20
# for i in range(1, 21):
#     print(i, end=' ')
# # Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# import random
# print(random.randint(1, 99), end=' ')
# # Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# # Leia paaris ja paaritud arvud ning lisa oma loendisse
# paaris = []
# paaritud = []
# for nr in loend:
#     if nr % 2 == 0:
#         paaris.append(nr)
#     else:
#         paaritud.append(nr)
# print(paaris)
# print(paaritud)
# Kuva paaris ja paaritute arvude summad
# print(sum(paaris))
# print(sum(paaritud))
# # Kuva arvud 1-42
# # Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# # Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# # Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
# for i in range(1, 43):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} TIKTAK")
#     elif i % 3 == 0:
#         print(f"{i} TIK")
#     elif i % 5 == 0:
#         print(f"{i} TAK")
#     else:
#         print(i)
# # Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
# for i in range(200, 321):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=', ')
# Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# #9.11 Tärnide ülesanne
# for i in range(1, 6):
#     print(" " * i, end="")
#     print('*' * (6-i))
# # Ülesanne 9.13
# # Mitmemõõtmelise massiivi kasutamine for-tsükliga
# # Tutvu elektriautode nimekirjaga, mis sisaldab 10 elektriauto mudelit, nende läbisõidu ulatust ja hinda. 
# # Mõista, kuidas andmed on struktureeritud.
# # Kuva andmed ridade kaupa, vorminda tulpadena
# # Leia keskmine läbisõidu ulatus ja hind
# # Kuva auto nimed, mille läbisõidu ulatus on suurem kui 300 km
# # Analüüsi andmeid, et tuvastada, kas kõrgema hinnaga autodel on tõepoolest pikem läbisõidu ulatus
# ev_data = [
# ['vehicle', 'range', 'price'],
# ['Tesla Model Y Long Range', '330', '58990'],
# ['Volkswagen ID.4 Pro', '260', '39995'],
# ['Ford Mustang Mach-E', '300', '42995'],
# ['Audi e-tron GT', '238', '102700'],
# ['Nissan Leaf', '149', '27400'],
# ['BMW iX xDrive50', '324', '83995'],
# ['Polestar 2', '265', '45500'],
# ['Kia EV6 Long Range', '310', '47795'],
# ['Mercedes-Benz EQS 450+', '350', '102310'],
# ['Hyundai Kona Electric', '258', '37400']
# ]
# ranges = []

# for autod in ev_data:
#     print(f"{autod[0]:30} {autod[1]:5} {autod[2]:7}") #vormindamine (tulba laius ":7")
#     if autod[1].isnumeric():
#         ranges.append(int(autod[1]))
#     # for i in autod:
#     #     print(i)
# print(f"Keskmine läbisõit on: {sum(ranges)/len(ranges)}")

# for autod in ev_data:
#     if autod[1].isnumeric() and int(autod[1]) > 300:
#         print(autod[0])

# Ülesanne 9.14 MINU TEHA ON KUJUND 4
import turtle