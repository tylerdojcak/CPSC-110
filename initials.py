#initials

from graphics import *

win = GraphWin("initials", 400, 400)

l1 = Line(Point(220,20),Point(180,50))
l2 = Line(Point(180,50),Point(220,80))
l3 = Line(Point(220,80),Point(180,110))

l4 = Line(Point(160,140),Point(240,140))
l5 = Line(Point(200,140),Point(200,230))

l6 = Line(Point(170,260),Point(170,360))
l7 = Line(Point(170,260),Point(230,310))
l8 = Line(Point(170,360),Point(230,310))

l1.draw(win)
l2.draw(win)
l3.draw(win)
l4.draw(win)
l5.draw(win)
l6.draw(win)
l7.draw(win)
l8.draw(win)

l1.setFill("purple")
l2.setFill("purple")
l3.setFill("purple")
l6.setFill("red")
l7.setFill("red")
l8.setFill("red")


win.getMouse()
win.close()
