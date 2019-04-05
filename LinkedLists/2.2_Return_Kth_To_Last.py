from SingleLinkedList import *
from sys import *


def kthElementToLast(kth,sLinkedList):

	#print "kth var: %s" % kth
	last = None
	current = sLinkedList.head
	i = 0

	while current is not None:
		if i < kth:
			i +=1
		else:
			#print current.data
			last = current
			break
		
		current = current.next 


	if last is not None:
		current = sLinkedList.head
		while last.next is not None:
			#print "El kth elemento adelante es: %s" % last.data
			#print "el current element is: %s" % current.data
			current = current.next
			last = last.next
		print "The kth element before last is: %s" % current.data
		
	else:
		print "the LinkedList  is not that big for a kth=%s" % kth 


if __name__ == "__main__":
	
	l =[]
	if len(argv) > 1:
		l = argv[1].split(',')
		#print l
	
	sll = SingleLinkedList(l,AppendMode.TOTAIL)
	sll.printLinkedList()
	kthElementToLast(int(argv[2]),sll)
