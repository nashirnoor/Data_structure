import math,turtle
def xt(t):
    return 16* math.sin(t) ** 3


def yt(t):
    return 13 * math.cos(t) - 5 * \
           math.cos(2*t) - 2 * \
           math.cos(3*t) - \
           math.cos(4*t)

t =turtle.Turtle()
t.speed(999999500000000000)
t.width(96)  

turtle.colormode(255)
turtle.Screen().bgcolor(0,0,0)
for i in range(250):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor(255, 0, 0)  # Set color to red
    t.goto(0,0)

t.hideturtle()
t.penup()
t.goto(0, -150)  
t.color("white")
t.write("Python, you complete my code with love.", align="center", font=("Arial", 22, "bold"))

t.goto(0, -280)

t.write("Happy Valentine's Day!", align="center", font=("Arial", 22, "bold"))

turtle.update()
turtle.mainloop()