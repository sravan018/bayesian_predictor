# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P


from __future__ import print_function
from logic import *
import turtle,copy

def main():
	input_text=raw_input("Enter the file name to be processed: ")
	print(input_text)
	bnn=createBayesianNetwork(input_text)
	blanket=[]
	blanket=computeMarkovBlanket(bnn,bnn.getnode('B'))
	for i in blanket:
		print(i.name,end=" ")
	print("")
	t=turtle
	t.title("BAYESIAN PREDICTOR")
	t.ht()
	t.setup(910,610)
	t.setworldcoordinates(0,-610,910,0)
	t.speed(0)
	draw_gui(t)
	t.mainloop()

main()