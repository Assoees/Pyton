# 03 Ülesanne
# Asso Eesmäe 05.12.24


#3.1
nimi = "Asso" #sõne, string
vanus = 33 #int, integer, täisarv
keskmine_hinne = 5.5 #komaarv, float
#plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne "+str(keskmine_hinne))
#komaga saan mitut asja printida
print(nimi,",",vanus, "aastat vana ja kesmine hinne", keskmine_hinne)
#lause vormindamine
print(f"{nimi}, on {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}!")

# 3.7
"""
    Ülesanne 3.7: Python Turtle kolmnurk
    Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
    Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
    Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
    Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
    Iga kolmnurk on järgmisest 1,5 korda eemal
    Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal
"""

#Impordib kilpkonna mooduli
import turtle

kylje_pikkus = 100
nurk = 120
varv = "red"

#näita kilpkonna, avab graafilise akna
turtle.color(varv)
#muudab kuvatava kilpkonna visuaali(classic, turtle, arrow, circle)
turtle.shape("circle")
#liigub otse edasi (ühikut), lühem käsk: turtle.fd
turtle.forward(kylje_pikkus)
#liigutab kilpkonna vasakule(mitu kraadi), lühem: turtle.lt
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.lt(nurk)
turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.lt(nurk)
turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.lt(nurk)
turtle.penup()
turtle.pendown()

turtle.done()