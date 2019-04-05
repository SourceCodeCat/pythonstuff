from Stack import *
from sys import *


def sortStack(s1):
	s2 = Stack()
	while not s1.isEmpty():
		v = s1.pop()
		if s2.isEmpty():
			s2.push(v)
		else:
			continue_ = True
			while continue_:
				v2 = s2.peek()
				if v2 is None:
					continue_ = False
					s2.push(v)
				else:
					if v > v2:
						s1.push(s2.pop())
					else:
						continue_ = False
						s2.push(v)
	s2.printLinkedList()

if __name__ == "__main__":
	
	l = []
	if len(argv) > 1:
		l = [int(e) for e in argv[1].split(',')]
		#print l
	
	s1 = Stack(l)
	s1.printLinkedList()
	sortStack(s1)
