#02 Ülesanne
#Asso Eesmae 05.12.24
"""
    Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
    Akna suurus 500×400
    Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
    Joone paksus 6
    Kiirus 0

"""
#impordime kilpkonna
import turtle

turtle.screensize(500, 400)

#sinine
turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(6)
turtle.circle(50,360)

#must
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.circle(50,360)

#red
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.color("red")
turtle.circle(50,360)

#yellow
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50,360)

#green
turtle.penup()
turtle.goto(-40,50)
turtle.pendown()
turtle.color("green")
turtle.circle(50,360)

turtle.done()