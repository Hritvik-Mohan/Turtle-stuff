import turtle

bob = turtle.Turtle()

bob.color("blue", "cyan")

bob.begin_fill() 

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.penup()
bob.forward(150)
bob.pendown()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.end_fill()


turtle.done()