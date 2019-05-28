#03-27 snow

from graphics import *
import random

#make a blue window
window = GraphWin("Snow", 600, 600)
window.setBackground("LightBlue3")

#make a list to store a bunch of points
flakes = []
dy = []
for i in range(500):
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    flakes.append(Point(x, y))
    dy.append(random.randint(3, 5))

# make them all white and draw them to the screen
for flake in flakes:
    flake.setFill("White")
    flake.draw(window)

# keep looping until escape is pushed
while window.checkKey() != "Escape":
    # move each flake down a bit
    for flake in flakes:
        flake.move(0, dy[index])
        if flake.getY >= 600:
            flake.move(0, -600)


window.close()
