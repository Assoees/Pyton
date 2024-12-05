#04. ülesanne
#Asso Eesmäe 05.12.24

# 4.1

"""
    Aia pikkus
    Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
    Aed on ristküliku kujuline.
    Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
    Väljasta lause, kasutades f-string vormindamist.
    Näide:
    Kasutaja sisestab: 4 ja 5
    Programm väljastab: Aia kogupikkus on 18 meetrit.
"""



a = int(input("Sisesta üks külg: "))
b = int(input("Sisesta teine külg: "))

ymber = 2*(a+b)
print(f"Aia pikkus on {ymber} meetrit.")