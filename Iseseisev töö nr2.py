# Iseseisev töö nr2
# Asso Eesmäe 17.08.25
#
# KILPKONN
# Kirjuta programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, 
# valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.

# Näide:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused 
# või väljuda programmist,jättes sisendi tühjaks.

import turtle
import random
turtle.pensize(2)
turtle.speed(5) 
külg = 60
rad = 60
kujund = input("Millise kujundi joonistame (ruut, ring, viisnurk, suvaline): ")
arv = int(input("Mitu kujundit joonistan: "))


def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(külg)
        turtle.left(72)

def joonista_ring():
    turtle.circle(rad)

def joonista_ruut():
    for _ in range(4):
        turtle.forward(külg)
        turtle.left(90)

def suvaline_kujund():
    kuju = random.choice(["ring", "ruut", "viisnurk"])
    if kuju == "ring":
        joonista_ring()
    elif kuju == "ruut":
        joonista_ruut()
    else:
        joonista_viisnurk()
        



for _  in range(arv):
    x = random.randint(-200,200) 
    y = random.randint(-200,200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
            
    if kujund == "viisnurk":
        joonista_viisnurk()
    elif kujund == "ruut":
        joonista_ruut()
    elif kujund == "ring":
        joonista_ring()
    elif kujund == "suvaline":
        suvaline_kujund()
    else:
        print("Võõras kujund")
        break
