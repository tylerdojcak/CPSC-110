from graphics import *

#window creation
win = GraphWin("Window", 615, 615)

#ball creation
ball = Circle(Point(307, 307), 4.5)
ball.draw(win)
ball.setFill("light green")

#ball speed
dx = -.01
dy = .01

#paddle creation
paddle = Rectangle(Point(290, 575), Point(340, 585))
paddle.draw(win)
paddle.setFill("orchid")

#play
while True:
    ball.move(dx, dy)
    key = win.checkKey()
    if key == "Left":
        paddle.move(-20, 0)
    if key == "Right":
        paddle.move(20, 0)
    center = ball.getCenter()
    x = center.getX()
    if x <= 4.5:
        dx = -1*dx
    if x >= 610.5:
        dx = -1*dx
    y = center.getY()
    if y <= 4.5:
        dy = -1*dy
    if y >= 610.5:
        ball.move(0, -600)
    padcenter = paddle.getCenter()
    px = padcenter.getX()
    if x + 4.5 < px + 25 and x - 4.5 > px - 25 and y + 4.5 >=575:
        dy = -1.1*dy
        dx = 1.1*dx
        
  
    

  
