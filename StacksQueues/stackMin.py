from Stack import *
from sys import *

def getMin(stck):
	temp = Stack()
	theMin = None
	while not stck.isEmpty():
		v = stck.pop()
		if theMin is None:
			theMin = v
		else:
			if v < theMin:
				theMin = v
		
		temp.push(v)
	stck = temp
	print "The min value is : %s" % theMin
	#stck.printLinkedList()




if __name__ == "__main__":
	
	l =[]

	if len(argv) > 1:
		l = [int(e) for e in argv[1].split(',')]
		#print l
	
	stack = Stack(l)
	stack.printLinkedList()
	getMin(stack)
