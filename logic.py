# Bhavanam Sravan Kumar Reddy
# 2015A7PS0072P

from __future__ import print_function
import turtle,copy

# data structure for storing variables
class node():
	def __init__(self,name,parent_list,cpt):
		self.name=name
		self.parent_list=parent_list
		self.cpt=cpt
		self.parent_pointers=[] # pointers to parent nodes of the current node 
		self.children_pointers=[] # pointers to children nodes of the current node
	def add_parent_pointer(self,nod_e): 
		self.parent_pointers.append(nod_e)
	def add_children_pointer(self,nod_e):
		self.children_pointers.append(nod_e)


# data structure for bayesian network
class BayesianNetwork():
	def __init__(self):
		self.node_list=[]
	def add_node(self,node_add):
		self.node_list.append(node_add)
	def getnode(self,node_name):
		for i in self.node_list:
			if i.name==node_name:
				return i
	def find_children(self,p): 
		children=[]
		for i in self.node_list:
			if p in i.parent_list:
				children.append(i.name)
		return children

	def print_children(self,l):
		st=""
		for i in l:
			st+=i+","
		if len(st)-1>0:
			st=st[:len(st)-1]
		return st
	def __repr__(self):
		st=""
		for i in self.node_list:
			st+=i.name+"   ------->  "+self.print_children(self.find_children(i.name))+"\n"
		if len(st)-1>0:
			st=st[:len(st)-1]
		return st


def createBayesianNetwork(input_text):
	bnn=BayesianNetwork()
	f=open(input_text,"r")
	for line in f:
		if line=="$$":
			break
		[t1,t4,t3]=line.split(" >> ")
		t2=t4[1:len(t4)-1].split(", ")
		if t2[0]=='':
			t2=[]
		n=node(t1,t2,map(float,t3.split()))
		bnn.add_node(n)

	# linking nodes
	for i in bnn.node_list:
		for j in i.parent_list:
			i.add_parent_pointer(bnn.getnode(j))
		children=bnn.find_children(i.name)
		for j in children:
			i.add_children_pointer(bnn.getnode(j))

	print(bnn)
	return bnn


def computeMarkovBlanket(bayesian_network,nod_e):
	blanket=[]
	node_names=[]
	node_names.append(nod_e.name)
	node_names+=nod_e.parent_list
	child=bayesian_network.find_children(nod_e.name)
	for i in child:
		node_names+=bayesian_network.getnode(i).parent_list
	node_names+=child
	node_names=list(set(node_names))
	for i in node_names:
		blanket.append(bayesian_network.getnode(i))
	return blanket

# createExpression function is defined in gui.py
	
# computeProbability function is defined in gui.py