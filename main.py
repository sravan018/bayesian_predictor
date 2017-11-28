# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P


from __future__ import print_function
from gui import *
from logic import *
import turtle,copy


# to get the variable list which used in the gui phase
def get_names(bayes):
	b=[]
	for i in bayes.node_list:
		b.append(i.name)
	b.sort()
	return b

def main():
	input_text=raw_input("Enter the file name that is to be processed: ")
	print("Parent       Children")
	bnn=createBayesianNetwork(input_text)
	b=get_names(bnn)
	print("")
	var=raw_input("Enter a variable to find its markov blanket\n[variable name in capital letters/(n - if markov blanket is not needed)]: ")
	if var!='n':
		print("Markov Blanket of ",var," :")
		blanket=[]
		blanket=computeMarkovBlanket(bnn,bnn.getnode(var))
		st="{"
		for i in blanket:
			st+=i.name+", "
		st=st[:len(st)-2]+"}"
		print(st)
	t=turtle
	t.title("BAYESIAN PREDICTOR")
	t.ht()
	t.setup(1000,700)
	t.setworldcoordinates(0,-1000,1000,0)
	t.speed(0)
	createExpression(t,b,bnn)
	t.mainloop()
	print(query_v)
	print(cond_v)



main()