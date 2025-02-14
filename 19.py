# Ülesanne 19
# Asso Eesmae
# IKT-24
# Kasutame ülesande lahendamiseks haridustulemused.json andmefaili:

# Kuva 12.klassi õpilaste nimekiri
# Kuva mitu õpilast õpib 10, 11 ja 12 klassis
# Kuva millistes trennides 12. klassi õpilased käivad
# Kuva 12 klassi õpilaste hinneteleht (nimi, ained, punktid)

import json

klass12opilased = []
kokku12klass = 0
# Korjan kokku kõik ringid milles käiakse
huvialad =  []



# Faili avamine ja JSON-i laadimine
with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    students = json.load(file)
    for student in students:
        # print(student["nimi"])
        if student["klass"]=="12":
            klass12opilased.append(student["nimi"])
            kokku12klass+=1
        # print(student["tegevused"])
            for tegevus in student["tegevused"]:
                if tegevus not in huvialad:
                    huvialad.append(tegevus)
            #hinneteleht
            print("------------------------HINNETELEHT---------------------------------")
            print(student["nimi"])
            d=student["hinded"]
            for k, v in d.items():
                print(k, v)
            
            print("-----------------------------------------------------------------")
# print(klass12opilased)            
# print(kokku12klass, "õpilast")
# for i in huvialad:
#     print(i)