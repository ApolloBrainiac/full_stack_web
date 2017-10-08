import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")
    brad.speed(3)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #criss = turtle.Turtle()
    #criss.shape("classic")
    #criss.color("red")

    #a = 0
    #while a < 3:
    #    criss.backward(100)
    #    criss.left(120)
    #    a += 1

    window.exitonclick()
    
draw_shapes()
