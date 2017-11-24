# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P


from __future__ import print_function
from logic import *
from gui import *
import turtle,copy

def get_names(bayes):
	b=[]
	for i in bayes.node_list:
		b.append(i.name)
	b.sort()
	return b

def main():
	input_text="input1.txt"#raw_input("Enter the file name to be processed: ")
	print(input_text)
	bnn=createBayesianNetwork(input_text)
	b=get_names(bnn)
	blanket=[]
	blanket=computeMarkovBlanket(bnn,bnn.getnode('B'))
	for i in blanket:
		print(i.name,end=" ")
	print("")
	t=turtle
	t.title("BAYESIAN PREDICTOR")
	t.ht()
	t.setup(1000,1000)
	t.setworldcoordinates(0,-1000,1000,0)
	t.speed(0)
	draw_gui(t,b)
	t.mainloop()

main()