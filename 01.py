#01. Ülesnnae
#Asso Eesmäe 05.12.24

#Impordib kilpkonna mooduli
import turtle

#näita kilpkonna, avab graafilise akna
turtle.showturtle()
#muudab kuvatava kilpkonna visuaali(classic, turtle, arrow, circle)
turtle.shape("turtle")
#liigub otse edasi (ühikut), lühem käsk: turtle.fd
turtle.forward(200)
#liigutab kilpkonna vasakule(mitu kraadi), lühem: turtle.lt
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.lt(120)

#süda

#tõstab kilpkonna üles, et ei joonistaks
turtle.penup()
#liigutab kilpkonna soovitud kohale
turtle.goto(-300,0)
#paneb kilkonna tagasi, et joonistaks
turtle.pendown()
#liigutab kilpkonna edasi
turtle.fd(100)
#joonistab poolringi
turtle.circle(50,180)
#keerab kilpkonna paremale
turtle.rt(90)
turtle.circle(50,180)
turtle.fd(100)
#keerabkilpkonna vasakule
turtle.lt(90)
#kilpkonna peatamine, et ei jokseks graafiline aken kokku
turtle.done()

