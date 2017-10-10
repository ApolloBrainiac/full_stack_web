import turtle

def draw_petal(some_turtle):
    for i in range(1,3):
        some_turtle.right(45)
        some_turtle.forward(100)
        some_turtle.right(135)
        some_turtle.forward(100)

def art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    trey = turtle.Turtle()
    trey.shape("classic")
    trey.color("red")
    trey.speed(15)

    for i in range(1,36):
        draw_petal(trey)
        trey.right(10)

    trey.right(100)
    trey.forward(300)

    window.exitonclick()

art()
