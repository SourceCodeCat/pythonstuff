from SingleLinkedList import *
from sys import *

def partition(p,head):
	
	sll_left = SingleLinkedList()
	sll_right = SingleLinkedList([None])
	current = head
	#print "the value of the sll2 partition is: %s" % sll2_partition.data
	while current is not None:
		#sll2.printLinkedList()
		if current.data < p:
			#print "append to head"
			#sll2.appendToHead(current.data)
			sll_left.appendNode(current.data)	
		else:
			if current.data > p and sll_right.head.data is None:
				print "setting as partition value %s" % current.data
				#sll2_partition.data = current.data
				sll_right.head.data = current.data
			else:
				print "append to tail"
				sll_right.appendNode(current.data) 
		current = current.next
			

	#current = sll_right.head
	#while current is not None:
	#	sll_left.appendNode(current.data)
	#	current = current.next
	
	sll_left.tail.next = sll_right.head
	sll_left.printLinkedList()



if __name__ == "__main__":
	
	l =[]
	if len(argv) > 1:
		l = [int(e) for e in argv[1].split(',')]
		#print l
	
	sll = SingleLinkedList(l,AppendMode.TOTAIL)
	sll.printLinkedList()
	partition(int(argv[2]),sll.head)
