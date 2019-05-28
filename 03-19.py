from graphics import *

window = GraphWin()

location = window.getMouse()
print("Click at (", location.getX(), ",", location.getY(), ")")
window.close()
