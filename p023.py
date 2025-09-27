''' Rajzol egy 150 pontos egyenlő szárú háromszöget a képernyő közepére.
Színe piros. Rajz indul a "h" betűre. Kilépés a "q" betűre.'''

import turtle

def haromszog():
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.goto(-75, -37.5)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.pensize(5)

    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

#App
ablak = turtle.Screen()

turtle.listen()
turtle.onkey(haromszog, "h")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()

