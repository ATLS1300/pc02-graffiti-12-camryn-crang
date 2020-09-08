#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = Turtle()
panel.bgcolor("purple")
t.pensize(20)
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.color("pink")
t.pensize(10)
t.up()
t.goto(20,50)
t.down()
t.circle(50)
t.color("red")
t.pensize(30)
t.up()
t.goto(30,60)
t.down()
t.forward(150)











