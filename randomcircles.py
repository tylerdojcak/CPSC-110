import random

r = random.randint(5, 200)
x = random.randint(0, 400)
y = random.randint(0, 400)
color = random.randint(1, 3)

from graphics import *

# open up a graphics window
win = GraphWin("Test Program", 400, 400)

# create a circle at (200, 200) with radius 100
c = Circle(Point(x,y), r)

# make the circle random color
if color == 1:
    c.setFill("wheat")
elif color == 2:
    c.setFill("tomato4")
else:
    c.setFill("seashell")

# draw the circle onto the window
c.draw(win)

# wait for the user to click the window
win.getMouse()

# close the window
win.close()
