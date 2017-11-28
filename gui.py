# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P

from __future__ import print_function
from logic import *
import turtle,copy,itertools


# main gui drawer function

def draw_gui(t,b):
	global var
	var=b
	t.ht()
	# drawing border
	t.color("black")
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
	draw_box(t,170,40,"#90b1dd")
	t.goto(120+85,-20-30)
	t.write("Query variables",False,"center",("Arial",12,"normal"))
	t.goto(120,-20)
	t.goto(510,-20)
	draw_box(t,220,40,"#90b1dd")
	t.goto(510+110,-20-30)
	t.write("Condition variables",False,"center",("Arial",12,"normal"))
	# bottom boxes
	t.goto(90,-870)
	draw_box(t,700,40,"#9cb95e")
	t.goto(90+90 ,-870-30)
	t.write("Generated Query: ",False,"center",("Arial",12,"normal"))
	t.goto(820,-870)
	draw_box2(t,160,40,"#dabcbd")
	t.goto(820+80 ,-870-30)
	t.color("red")
	t.write("Compute Query",False,"center",("Arial",12,"normal"))
	t.color("black")
	t.goto(90,-920)
	draw_box(t,700,40,"#9cb95e")
	t.goto(90+55,-920-30)
	t.write("Answer: ",False,"center",("Arial",12,"normal"))
	t.goto(820,-920)
	draw_box2(t,160,40,"#dabcbd")
	t.goto(820+80 ,-920-30)
	t.color("red")
	t.write("New Query",False,"center",("Arial",12,"normal"))
	t.color("black")
	# exit box
	t.goto(820,-20)
	draw_box(t,160,40,"red")
	t.goto(820+80,-20-30)
	t.write("Exit",False,"center",("Arial",12,"normal"))
	# options
	options(t,b,115,-85)
	options1(t,b,115+cond_quer,-85)
	button_responses()

# draws the buttons for the variables

def options(t,l,x,y):
	t.pu()
	x1=x
	x2=x+l_box+sp_btw_l
	for i in range(len(l)):
		t.goto(x1,y)
		check_list.append([[x1,y],l[i]])
		draw_box(t,l_box,b_box,"#9cb95e")
		t.goto(x1+l_box/2,y-10-b_box/2-2)
		t.write(l[i],False,"center",("Arial",12,"normal"))
		t.goto(x2,y)
		draw_box(t,l_box,b_box,"#9cb95e")
		t.goto(x2+l_box/2,y-10-b_box/2-2)
		t.write("~"+l[i],False,"center",("Arial",12,"normal"))
		y-=b_box+sp_btw_b

def options1(t,l,x,y):
	t.pu()
	x1=x
	x2=x+l_box+sp_btw_l
	for i in range(len(l)):
		t.goto(x1,y)
		draw_box(t,l_box,b_box,"#9db860")
		t.goto(x1+l_box/2,y-10-b_box/2-2)
		t.write(l[i],False,"center",("Arial",12,"normal"))
		t.goto(x2,y)
		draw_box(t,l_box,b_box,"#9db860")
		t.goto(x2+l_box/2,y-10-b_box/2-2)
		t.write("~"+l[i],False,"center",("Arial",12,"normal"))
		y-=b_box+sp_btw_b
		


def draw_box(t,l,b,color):
	t.pd()
	t.color("#a7ad9c",color)
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
	t.color("black")
	t.pu()

def draw_box2(t,l,b,color):
	t.pd()
	t.color(color,"white")
	t.fd(l)
	t.rt(90)
	t.pensize(5)
	t.fd(b)
	t.rt(90)
	t.fd(l)
	t.rt(90)
	t.pensize(2)
	t.fd(b)
	t.rt(90)
	t.color("black")
	t.pu()

#variable list
var=[]

# button dimensions for options
l_box=80
b_box=40
# space between button in options
sp_btw_l=10
sp_btw_b=10
# space between query options and conditional options
cond_quer=535-115

# button select check list
check_list=[]

# to keep track of selected points for markov blanket drawing
mar_quer=[]
mar_cond=[]

# selected variables
cond_v=[]
query_v=[]

#click varibles
xclick = 0
yclick = 0

#bayesian network
bayesnet=None

#making compute query clickable only once
click_once=0


# onclick functions
def button_responses():
    turtle.onscreenclick(modifyglobalvariables)

def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    
    xclick = int(rawx//1)
    yclick = int(rawy//1)

    check_click_options(xclick,yclick)


def check_click_options(x,y):
	global l_box,b_box,sp_btw_l,sp_btw_b,cond_quer,cond_v,query_v,check_list,mar_quer,mar_cond,click_once
   	t=turtle
   	t.ht()
   	t.pu()
   	if 820<=x<=820+160 and -20-40<=y<=-20 : # exit option
   		exit()
   	elif 820<=x<=820+160 and -870-40<=y<=-870 and click_once==0: # compute query option
   		t.onscreenclick(None)
   		if len(query_v)==0 :
   			print("Invalid query, must have at least one query variable.")
			t.onscreenclick(None)
			# clearing screen
			t.home()
			t.fd(18)
			t.rt(90)
			t.fd(18)
			t.lt(90)
			t.pu()
			t.color("black","white")
			t.begin_fill()
			t.fd(972)
			t.rt(90)
			t.fd(972)
			t.rt(90)
			t.fd(972)
			t.rt(90)
			t.fd(972)
			t.rt(90)
			t.end_fill()
			t.pensize(2)
			# re-iniatizing variables
			check_list=[]
			cond_v=[]
			query_v=[]
			mar_quer=[]
			mar_cond=[]
			click_once=0
			draw_gui(t,var)
   		else:
   			t.onscreenclick(None)
   			t.goto(90+187 ,-870-30)
   			st1=""
   			st2=""
   			for i in query_v:
   				st1+=i+","
   			for i in cond_v:
   				st2+=i+","
   			t.write("P("+st1[:len(st1)-1]+" | "+st2[:len(st2)-1]+")",False,"left",("Arial",12,"normal"))
   			ans=computeProbability(query_v,cond_v,bayesnet,t)
   			markov_blanket_displayer(t)
   			t.goto(90+110,-920-30)
   			t.write(str(ans),False,"left",("Arial",12,"normal"))
   			click_once=1
   			t.onscreenclick(modifyglobalvariables)
   		
   	elif 820<=x<=820+160 and -920-40<=y<=-920 :	# new query option
		t.onscreenclick(None)
		# clearing screen
		t.home()
		t.fd(18)
		t.rt(90)
		t.fd(18)
		t.lt(90)
		t.pu()
   		t.color("black","white")
   		t.begin_fill()
		t.fd(972)
		t.rt(90)
		t.fd(972)
		t.rt(90)
		t.fd(972)
		t.rt(90)
		t.fd(972)
		t.rt(90)
		t.end_fill()
		t.pensize(2)
		# re-iniatizing variables
		check_list=[]
		cond_v=[]
		query_v=[]
		mar_quer=[]
		mar_cond=[]
		click_once=0
		draw_gui(t,var)
   	else: # option select for variables
   		t.onscreenclick(None)
		for i in check_list:
			if i[0][0]<=x<=i[0][0]+l_box and i[0][1]-b_box<=y<=i[0][1] and len(query_v)<10:
				query_v.append(i[1])
				t.goto(i[0][0],i[0][1])
				draw_box(t,l_box,b_box,"#ffc001")
				t.goto(i[0][0]+l_box/2,i[0][1]-10-b_box/2)
				t.write(i[1],False,"center",("Arial",12,"normal"))
				check_list.remove(i)
				mar_quer.append(i)
				break
			elif i[0][0]+sp_btw_l+l_box<=x<=i[0][0]+sp_btw_l+l_box+l_box and i[0][1]-b_box<=y<=i[0][1] and len(query_v)<10:
				query_v.append("~"+i[1])
				t.goto(i[0][0]+sp_btw_l+l_box,i[0][1])
				draw_box(t,l_box,b_box,"#ffc001")
				t.goto(i[0][0]+sp_btw_l+l_box+l_box/2,i[0][1]-10-b_box/2)
				t.write("~"+i[1],False,"center",("Arial",12,"normal"))
				check_list.remove(i)
				mar_quer.append(i)
				break
			elif i[0][0]+cond_quer<=x<=i[0][0]+cond_quer+l_box and i[0][1]-b_box<=y<=i[0][1] and len(cond_v)<10:
				cond_v.append(i[1])
				t.goto(i[0][0]+cond_quer,i[0][1])
				draw_box(t,l_box,b_box,"#ffc001")
				t.goto(i[0][0]+cond_quer+l_box/2,i[0][1]-10-b_box/2)
				t.write(i[1],False,"center",("Arial",12,"normal"))
				check_list.remove(i)
				mar_cond.append(i)
				break
			elif i[0][0]+sp_btw_l+l_box+cond_quer<=x<=i[0][0]+sp_btw_l+l_box+cond_quer+l_box and i[0][1]-b_box<=y<=i[0][1] and len(cond_v)<10:
				cond_v.append("~"+i[1])
				t.goto(i[0][0]+sp_btw_l+l_box+cond_quer,i[0][1])
				draw_box(t,l_box,b_box,"#ffc001")
				t.goto(i[0][0]+sp_btw_l+l_box+cond_quer+l_box/2,i[0][1]-10-b_box/2)
				t.write("~"+i[1],False,"center",("Arial",12,"normal"))
				check_list.remove(i)
				mar_cond.append(i)
				break
		t.onscreenclick(modifyglobalvariables)
	



# GUI functions for displaying markov blanket

def markov_blanket_string(node_list):
	st="{"
	for i in node_list:
		st+=i.name+","
	st=st[:len(st)-1]
	return st+"}"

def markov_blanket_displayer(t):
	global mar_quer,mar_cond,bayesnet
	t.goto(120+190,-20-70)
	t.color('blue')
	t.write("Markov Blanket",False,"left",("Arial",12,"normal"))
	t.goto(510+240,-20-70)
	t.write("Markov Blanket",False,"left",("Arial",12,"normal"))
	t.color('black')
	for i in mar_quer:
		t.goto(i[0][0]+180,i[0][1]-30)
		st=markov_blanket_string(computeMarkovBlanket(bayesnet,bayesnet.getnode(i[1])))
		t.write(st,False,"left",("Arial",9,"bold"))
	for i in mar_cond:
		t.goto(i[0][0]+180+cond_quer,i[0][1]-30)
		st=markov_blanket_string(computeMarkovBlanket(bayesnet,bayesnet.getnode(i[1])))
		t.write(st,False,"left",("Arial",9,"bold"))


# non-GUI related functions

def createExpression(t,b,bnn):
	global bayesnet
	bayesnet=bnn
	draw_gui(t,b)

def computeProbability(quer,cond,bnn,t):
	t.goto(800,-520)
	draw_box2(t,160,40,"#dabcbd")
	t.goto(800+80 ,-520-30)
	t.color("red")
	t.write("Processing Query",False,"center",("Arial",12,"normal"))
	numo=[]
	deno=[]
	for i in quer:
		if i[0]=="~":
			numo.append(i[1])
		else:
			numo.append(i)
	for i in cond:
		if i[0]=="~":
			deno.append(i[1])
		else:
			deno.append(i)
	numo+=deno
	numo=list(set(numo))
	deno=list(set(deno))
	num=cal_prob(quer,cond,numo,bnn,0)
	if len(deno)==0:
		den=1
	else:
		den=cal_prob(quer,cond,deno,bnn,1)
	t.goto(795,-515)
	t.pd()
	t.color("white","white")
	t.begin_fill()
	t.fd(180)
	t.rt(90)
	t.fd(60)
	t.rt(90)
	t.fd(180)
	t.rt(90)
	t.fd(60)
	t.rt(90)
	t.end_fill()
	t.pu()
	t.color("black")
	return num/den

# calculates probability value for numerator or denominator term
def cal_prob(quer,cond,lis,bnn,typer): # lis is either numo or deno (type=0 for numo and type=1 for deno)
	temp=copy.deepcopy(lis)
	k=0
	while k < len(lis):
		mtemp=computeMarkovBlanket(bnn,bnn.getnode(lis[k]))
		for j in mtemp:
			lis.extend(j.name)
			lis=remove_dup(lis)
		k+=1
	lis=list(set(lis)-set(temp))
	#generating combos
	lst = list(itertools.product([0, 1], repeat=len(lis)))
	s=0
	for i in lst:
		ind=0
		temp_append=[]
		for j in i:
			if j==0:
				temp_append.append("~"+lis[ind])
				ind+=1
			elif j==1:
				temp_append.append(lis[ind])
				ind+=1
		if typer==0:
			temp_append=temp_append+quer+cond
			s+=cal_comb(temp_append,bnn)
		elif typer==1:
			temp_append=temp_append+cond
			s+=cal_comb(temp_append,bnn)
	return s



def cal_var(var,lis,bnn): # var is variable whose prob is calculated, lis is list of (quer+cond)+comb/(cond+comb) : returns the probability for that var
	n=bnn.getnode(var)
	par_list=n.parent_list
	index_s=""
	for i in par_list:
		if i in lis:
			index_s+="1"
		elif "~"+i in lis:
			index_s+="0"
	if len(par_list)==0:
		return n.cpt[0]
	else:
		return n.cpt[int(index_s,2)]

def cal_comb(lis,bnn): # returns the probability product for a given combo
	p=1
	for i in lis:
		if i[0]=="~":
			p*=(1-cal_var(i[1],lis,bnn))
		else:
			p*=cal_var(i,lis,bnn)
	return p

# for removing duplicate elements in the list
def remove_dup(l):
	temp=[]
	for i in l:
		if i not in temp:
			temp.append(i)
	return temp