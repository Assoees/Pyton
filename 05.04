#Ülesanne 5

'''
    Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
    Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”,
    kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja kasutama
    randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0, siis
    võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
    Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
    Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline
    ring; kui valesti, siis punane ring.
'''

# 0 kiri
# 1 kull

import random
import turtle


try:
    valik = random.randint(0,1)
    arvamus = int(input("vali kull 1 või kiri 0:"))
    if arvamus >=0 and arvamus <=1:
        if valik == arvamus:
            print("Arvasid ära")
            turtle.color("green")
            turtle.circle(50)
        else:
            print("Arvasid valesti")
            turtle.color("red")
            turtle.circle(50)
        turtle.done()
    else:
        print("sellist valikut ju pilnud!")
except:
    print("Viga sisestusel!")
    