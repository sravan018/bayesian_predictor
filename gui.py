# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P

from __future__ import print_function
import turtle,copy


def draw_gui(t,b):
	t.ht()
	# drawing border
	t.pensize(3)
	t.fd(990)
	t.rt(90)
	t.fd(990)
	t.rt(90)
	t.fd(990)
	t.rt(90)
	t.fd(990)
	t.rt(90)
	t.pensize(2)
	t.pu()
	t.home()
	# heading boxes
	t.goto(120,-20)
	draw_box(t,170,40,"#8db2e0")
	t.goto(120+85,-20-30)
	t.write("Query variables",False,"center",("Arial",12,"normal"))
	t.goto(120,-20)
	t.goto(510,-20)
	draw_box(t,220,40,"#8db2e0")
	t.goto(510+110,-20-30)
	t.write("Condition variables",False,"center",("Arial",12,"normal"))
	# bottom boxes
	t.goto(90,-870)
	draw_box(t,700,40,"#9db860")
	t.goto(90+100 ,-870-30)
	t.write("Generated Query: ",False,"center",("Arial",12,"normal"))
	t.goto(90,-920)
	draw_box(t,700,40,"#9db860")
	t.goto(90+55,-920-30)
	t.write("Answer: ",False,"center",("Arial",12,"normal"))
	# options
	options(t,b,115,-85)
	options(t,b,535,-85)

def options(t,l,x,y):
	t.pu()
	x1=x
	x2=x+80+10
	for i in range(len(l)):
		t.goto(x1,y)
		draw_box(t,80,40,"#9db860")
		t.goto(x1+40,y-30)
		t.write(l[i],False,"center",("Arial",12,"normal"))
		t.goto(x2,y)
		draw_box(t,80,40,"#9db860")
		t.goto(x2+40,y-30)
		t.write("~"+l[i],False,"center",("Arial",12,"normal"))
		y-=50
		


def draw_box(t,l,b,color):
	t.pd()
	t.color("gray",color)
	t.begin_fill()
	t.fd(l)
	t.rt(90)
	t.pensize(4)
	t.fd(b)
	t.rt(90)
	t.fd(l)
	t.rt(90)
	t.pensize(2)
	t.fd(b)
	t.rt(90)
	t.end_fill()
	t.pu()
	t.color("black")




xclick = 0
yclick = 0

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables)

def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print(xclick)
    print(yclick)

getcoordinates()