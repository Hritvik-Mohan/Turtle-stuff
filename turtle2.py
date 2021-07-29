import turtle
import math

bob = turtle.Turtle()
bob.color("blue", "cyan")
bob.speed(10)

bob.begin_fill()
for i in range(2000):
    bob.forward(math.sqrt(i))
    bob.left(i%180)

bob.end_fill()


turtle.done()