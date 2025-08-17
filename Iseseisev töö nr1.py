# Iseseisev töö nr1 (Kujund 2 https://www.metshein.com/wp-content/uploads/2023/10/python-turtle-KT-scaled.jpg)
# Asso Eesmäe 17.08.25


import turtle

Külg = 200	

turtle.speed(4)
turtle.pensize(3)

for _ in range(1):
    turtle.left(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg/2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(Külg/4)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    turtle.right(90)
    turtle.forward(Külg)
    


turtle.done()
