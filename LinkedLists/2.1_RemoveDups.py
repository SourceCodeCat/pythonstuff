from SingleLinkedList import *
from sys import *


def removeDuplicates(sLinkedList):
	current = sLinkedList.head
	
	
	while current is not None:
		previous = current
		iterator = current.next
		while iterator  is not None:
			if current.data == iterator.data:
				previous.next = iterator.next
				iterator = iterator.next
			else:
				previous = iterator
				iterator = iterator.next
		current = current.next
	sLinkedList.printLinkedList()


if __name__ == "__main__":
	
	l =[]
	if len(argv) > 1:
		l = argv[1].split(',')
		#print l
	
	sll = SingleLinkedList(l,AppendMode.TOTAIL)
	sll.printLinkedList()
	removeDuplicates(sll)
	
#	sll2 = SingleLinkedList()
#	sll2.printLinkedList()
#	sll2.appendNode(90)
#	sll2.appendNode(10)
#	sll2.printLinkedList()	