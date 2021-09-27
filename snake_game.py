import turtle
from turtle import *
import time
from time import *
import random
from random import *
from tkinter import *


a=Screen()
a.title('Snake game')
a.bgcolor('light green')
a.setup(width=1200,height=800)
a.tracer(0)
delay=0.1

score_A=0
high_score_A=0
score_B=0
high_score_B=0


ram=Turtle()
ram.speed(0)
ram.shape('circle')
ram.color('purple')
ram.pensize(0.5)
ram.penup()
ram.goto(50,0)
ram.direction = 'stop'

snow=Turtle()
snow.speed(0)
snow.shape('circle')
snow.color('navy')
snow.pensize(0.5)
snow.penup()
snow.goto(-50,0)
snow.direction = 'stop'




def move_ram():
    if ram.direction == 'up':
        y=ram.ycor()
        ram.sety(y+20)
    if ram.direction == 'down':
        y=ram.ycor()
        ram.sety(y-20)
    if ram.direction == 'right':
        x=ram.xcor()
        ram.setx(x+20)
    if ram.direction == 'left':
        x=ram.xcor()
        ram.setx(x-20)
        

def go_up_ram():
    if ram.direction != 'down':
        ram.direction = 'up'
def go_down_ram():
    if ram.direction != 'up':
        ram.direction = 'down'
def go_right_ram():
    if ram.direction != 'left':
        ram.direction = 'right'
def go_left_ram():
    if ram.direction != 'right':
        ram.direction = 'left'


def move_snow():
    if snow.direction == 'up':
        y=snow.ycor()
        snow.sety(y+20)
    if snow.direction == 'down':
        y=snow.ycor()
        snow.sety(y-20)
    if snow.direction == 'right':
        x=snow.xcor()
        snow.setx(x+20)
    if snow.direction == 'left':
        x=snow.xcor()
        snow.setx(x-20)
        

def go_up_snow():
    if snow.direction != 'down':
        snow.direction = 'up'
def go_down_snow():
    if snow.direction != 'up':
        snow.direction = 'down'
def go_right_snow():
    if snow.direction != 'left':
        snow.direction = 'right'
def go_left_snow():
    if snow.direction != 'right':
        snow.direction = 'left'
        


a.listen()
a.onkey(go_up_ram,'w')
a.onkey(go_down_ram,'s')
a.onkey(go_left_ram,'a')
a.onkey(go_right_ram,'d')
a.onkey(go_up_snow,'Up')
a.onkey(go_down_snow,'Down')
a.onkey(go_left_snow,'Left')
a.onkey(go_right_snow,'Right')



food1=Turtle()
food1.speed(0)
food1.shape('circle')
food1.penup()
food1.color('red')
m1 = randint(-480,480)
n1 = randint(-280,280)
food1.goto(m1,n1)
segments1 = []

food2=Turtle()
food2.speed(0)
food2.shape('circle')
food2.penup()
food2.color('dark orange')
m2 = randint(-480,480)
n2 = randint(-280,280)
food2.goto(m2,n2)
segments2 = []


pen1 = Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 320)
pen1.write("Score of A: 0  High Score of A: 0", align="center", font=("Times", 24, "normal"))


pen2 = Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 290)
pen2.write("Score of B: 0  High Score of B: 0", align="center", font=("Times", 24, "normal"))



bor=Turtle()
bor.speed(0)
bor.color('black')
bor.pensize(5)
bor.penup()
bor.goto(0,290)
bor.pendown()
bor.goto(508,290)
bor.goto(508,-290)
bor.goto(-508,-290)
bor.goto(-508,290)
bor.goto(0,290)
bor.hideturtle()



while True:
    a.update()
    if (ram.distance(food1) < 20) or (ram.distance(food2) < 20):
        x = randint(-490,490)
        y = randint(-280,280)
        if (ram.distance(food1) < 20):
            food1.goto(x, y)
        else:
             food2.goto(x, y)
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('magenta')
        new_segment.pensize(0.5)
        new_segment.penup()
        segments1.append(new_segment)
        delay -= 0.001
        score_A += 10
        if score_A > high_score_A:
            high_score_A = score_A 
        pen1.clear()
        pen1.write("Score of A: {}  High Score of A: {}".format(score_A, high_score_A), align="center", font=("Times", 24, "normal"))

        
    for i in range (len(segments1)-1,0,-1):
        x = segments1[i-1].xcor()
        y = segments1[i-1].ycor()
        segments1[i].goto(x,y) 
    if len(segments1) > 0:
            x = ram.xcor()
            y = ram.ycor()
            segments1[0].goto(x,y)
    move_ram()

    
    if ram.xcor() > 500 or ram.xcor() < -500 or ram.ycor() < -290 or ram.ycor() > 290:
        sleep(1)
        ram.goto(50,0)
        ram.direction = 'stop'
        for segment1 in segments1:
            segment1.goto(1000,1000)
        segments1.clear()
        score_A = 0
        delay = 0.1
        pen1.clear()
        pen1.write("Score of A: {}  High Score of A: {}".format(score_A, high_score_A), align="center", font=("Times", 24, "normal")) 

        
    for segment1 in segments1:
        if segment1.distance(ram) <= 15:
            sleep(1)
            ram.goto(0,0)
            ram.direction = 'stop'
            for segment1 in segments1:
                segment1.goto(1000,1000)
            segments1.clear()
            score_A = 0
        delay = 0.1
        pen1.clear()
        pen1.write("Score of A: {}  High Score of A: {}".format(score_A, high_score_A), align="center", font=("Times", 24, "normal"))










        
    if (snow.distance(food1) < 20) or (snow.distance(food2) < 20):
        x = randint(-490,490)
        y = randint(-280,280)
        if (snow.distance(food1) < 20):
            food1.goto(x, y)
        else:
             food2.goto(x, y)
        new_segment2 = Turtle()
        new_segment2.speed(0)
        new_segment2.shape('circle')
        new_segment2.color('cyan')
        new_segment2.pensize(0.5)
        new_segment2.penup()
        segments2.append(new_segment2)
        delay -= 0.001
        score_B += 10
        if score_B > high_score_B:
            high_score_B = score_B 
        pen2.clear()
        pen2.write("Score of B: {}  High Score of B: {}".format(score_B, high_score_B), align="center", font=("Times", 24, "normal"))

        
    for i in range (len(segments2)-1,0,-1):
        x = segments2[i-1].xcor()
        y = segments2[i-1].ycor()
        segments2[i].goto(x,y) 
    if len(segments2) > 0:
            x = snow.xcor()
            y = snow.ycor()
            segments2[0].goto(x,y)
    move_snow()

    
    if snow.xcor() > 500 or snow.xcor() < -500 or snow.ycor() < -290 or snow.ycor() > 290:
        sleep(1)
        snow.goto(-50,0)
        snow.direction = 'stop'
        for segment2 in segments2:
            segment2.goto(1000,1000)
        segments2.clear()
        score_B= 0
        delay = 0.1
        pen2.clear()
        pen2.write("Score of B: {}  High Score of B: {}".format(score_B, high_score_B), align="center", font=("Times", 24, "normal")) 

        
    for segment2 in segments2:
        if segment2.distance(snow) <= 15:
            sleep(1)
            snow.goto(-50,0)
            snow.direction = 'stop'
            for segment2 in segments2:
                segment2.goto(1000,1000)
            segments2.clear()
            score_B = 0
        delay = 0.1
        pen2.clear()
        pen2.write("Score of B: {}  High Score of B: {}".format(score_B, high_score_B), align="center", font=("Times", 24, "normal"))


    if ram.distance(snow) < 20:
        sleep(1)
        snow.goto(50,0)
        snow.direction = 'stop'
        for segment2 in segments2:
            segment2.goto(1000,1000)
        segments2.clear()
        score_B = 0
        delay = 0.1
        pen2.clear()
        pen2.write("Score of B: {}  High Score of B: {}".format(score_B, high_score_B), align="center", font=("Times", 24, "normal"))
        ram.goto(-50,0)
        ram.direction = 'stop'
        for segment1 in segments1:
            segment1.goto(1000,1000)
        segments1.clear()
        score_A= 0
        delay = 0.1
        pen1.clear()
        pen1.write("Score of A: {}  High Score of A: {}".format(score_B, high_score_B), align="center", font=("Times", 24, "normal"))

    
    #for i in range (len(segments1)-1,-1,-1):
        #if segments1[i].distance(snow) < 15:
            #for n in range (i,-1,-1):
                #segments1[n].goto(1000,1000)
                #segments1.pop(n)
            
    
    sleep(delay)
a.mainloop()
   
        
