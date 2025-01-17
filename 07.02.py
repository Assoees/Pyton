#Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
#“jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
#Kuva mõõdetava kuu nimetus
#Kuva viimase mõõtmise tulemus
#Kuva ainult temperatuurid
#Leia kuu maksimaalne ja minimaalne temperatuur
#Leia kuu keskmine temperatuur
#Mitu korda esines -20 kraadi
#Eemalda element nr 5
#Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
#Sorteeri temperatuurid nimekirjas kasvavas järjekorras

jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"Mõõdetav kuu: {jtemp[0]}")
print(f"Kuva viimase mõõte tulemus: {jtemp[-1]}")

maks = 0 #maksimaalne temperatuur
min = 100 #minimaalne temperatuur
summa = 0 #summa
kokku = 0 #kokku
kordused = 0 #kordused

for t in range(1, len(jtemp)): #temperatuurid
    print(jtemp[t], end= " ") 
    if jtemp[t] > maks: #maksimaal
        maks = jtemp[t] 
    if jtemp[t] < min: #minimaal
        min = jtemp[t]
    summa += jtemp[t] #summa
    kokku += 1
    if jtemp[t] == -20:#kordused
        kordused += 1   
jtemp.pop(5)    #kustutab
jtemp.insert(5, 33) #lisab
#jtemp.sort() #sorteeritud


print(f"Kuu maksimaalne temperatuur: {maks}") #maksimaalne temperatuur
print(f"Kuu minimaalne temperatuur: {min}") #minimaalne temperatuur
print(f"Kuu keskmine temperatuur: {summa/kokku :0.2f}") #keskmine temperatuur   
print(f"-20 kraadi esines {kordused} korda") #kordused
print(jtemp) #kustutatud ja lisatud temperatuurid

