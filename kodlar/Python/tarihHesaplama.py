import datetime
import time
import turtle
b = datetime.date.today()
a = datetime.date(2026 , 5 , 26)
print( a - b)
z = 30
c = -30
turtle.speed(100)
for i in range(25) :
    turtle.color("red")
    turtle.penup()
    turtle.setx(c)
    turtle.sety(c)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.setx(z)
    turtle.sety(z)
    turtle.pendown()
    turtle.color("blue")
    turtle.circle(100)
    z = z + 10
    c = c - 10
time.sleep(2)
turtle.bye
time.sleep(1200)