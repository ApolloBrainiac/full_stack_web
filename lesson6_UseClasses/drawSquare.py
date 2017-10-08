import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")
    brad.speed(10)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()
    
draw_square()
