import turtle
import random

ts = turtle.Screen()
ts.title("TURTLE")
turtle = turtle.Turtle()

rand_pos = []

rand_color = []

while len(rand_pos) < 32:
    rand_pos.append(random.randint(0, 255))


print(rand_pos)
print(rand_color)
    
