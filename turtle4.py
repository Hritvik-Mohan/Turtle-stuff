import turtle

pegasus = turtle.Turtle()
pegasus.getscreen().bgcolor("#994444")
pegasus.speed(10)

pegasus.penup()
pegasus.goto((-200, 100))
pegasus.pendown()

# for i in range(5):
#     pegasus.forward(200)
#     pegasus.left(216)

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)


star(pegasus, 360)

turtle.done()