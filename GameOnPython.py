from turtle import Screen, Turtle 
from time import sleep
from random import randint
import time

scr = Screen()
scr.cv._rootwindow.resizable(False,False)
scr.setup(800,600)
scr.bgpic('Terrain.png')
scr.title('Game')
scr.addshape('Player.gif')
scr.addshape('Apple.gif')

bomb0 = Turtle()
bomb0.speed(100)
bomb0.shape('Apple.gif')
bomb0.penup()
bomb0.setposition(randint(-300,300), 390)

bomb1 = Turtle()
bomb1.speed(100)
bomb1.shape('Apple.gif')
bomb1.penup()
bomb1.setposition(randint(-300,300), 600)

plr = Turtle()
plr.speed(100)
plr.shape('Player.gif')
plr.penup()
plr.setposition(0,-225)

Font = ("Alef", 48)
score = Turtle(visible = False)
score.speed(100)
score.penup()
score.setposition(-25,225)
score.color('darkred')
_score = 0
score.write(_score, font = Font)

def move_right():
    y = plr.xcor() + 50
    if y > 315:
        y = 315
    plr.setx(y)

def move_left():
    y = plr.xcor() - 50
    if y < -315:
        y = -315
    plr.setx(y)

scr.listen()
scr.onkeypress(move_right,"d")
scr.onkeypress(move_left, "a")

while True:
    bomb0.sety(bomb0.ycor() - randint(5,6))
    bomb1.sety(bomb1.ycor() - randint(5,6))
    if bomb0.ycor() + 30 >= plr.ycor() and bomb0.ycor() - 30 <= plr.ycor() and \
        bomb0.xcor() + 45 >= plr.xcor() and bomb0.xcor() - 45 <= plr.xcor():
        bomb0.setposition(randint(-300,300), 390)
        score.clear()
        _score += 1
        score.write(_score, font = Font)
    if bomb1.ycor() + 30 >= plr.ycor() and bomb1.ycor() - 30 <= plr.ycor() and \
        bomb1.xcor() + 45 >= plr.xcor() and bomb1.xcor() - 45 <= plr.xcor():
        bomb1.setposition(randint(-300,300), 390)
        score.clear()
        _score += 1
        score.write(_score, font = Font)

    if bomb0.ycor() <= -340 or bomb1.ycor() <= -340:
        score.clear()
        score.color('red')
        _score = "you Loser"
        score.setposition(-125,225)
        score.write(_score, font=Font) 
        time.sleep(1)
        break 
    if _score >= 10:
        score.clear()
        score.color('gold')
        _score = "You win"
        score.setposition(-125,225)
        score.write(_score, font=Font)
        time.sleep(1)
        break 