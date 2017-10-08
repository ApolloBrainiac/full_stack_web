import turtle


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")
    brad.speed(10)

    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    criss = turtle.Turtle()
    criss.shape("classic")
    criss.color("red")

    a = 0
    while a < 3:
        criss.backward(100)
        criss.left(120)
        a += 1

    window.exitonclick()
    
draw_shapes()
