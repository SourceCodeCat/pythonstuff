from SingleLinkedList import *
from sys import *

#########################################################################
#
#	This code deletes de middle node by finding
#	the middle node recursively. But the problem
#	states we are not given access to the head node
#	therefore we can copy the values from the "next" nodes
#	and then at the end, just remove the last node....
#	the tricky part is that we can delete neither the head or the tail
#	one approach would be just marking the last node as a dummy
#########################################################################
def deleteMiddleNode(node,nodeIndex,total):
	
	nodeIndex +=1
	if node.next is not None:
		total = deleteMiddleNode(node.next,nodeIndex,0)
	else:
		total = nodeIndex		
		return (total/2 if total % 2 == 0 else (total/2)+1) if total > 2 else None

	if total is not None:	
		if nodeIndex == (total - 1):
			#node.next = node.next.next
			print "we have to delete Node:%s, with value:%s" % (nodeIndex+1,node.next.data)
			node.next = node.next.next
	else:
		print "The LinkedList needs to be greater than 2... sorry :("
	
	return total
	
	


			

if __name__ == "__main__":
	
	l =[]
	if len(argv) > 1:
		l = argv[1].split(',')
		#print l
	
	sll = SingleLinkedList(l,AppendMode.TOTAIL)
	sll.printLinkedList()
	deleteMiddleNode(sll.head,0,0)
	sll.printLinkedList()
