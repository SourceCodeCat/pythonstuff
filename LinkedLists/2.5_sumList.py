from SingleLinkedList import *
from sys import *


def sumList(cNode1,cNode2,recLev):

	if cNode1 is None and cNode2 is None:
		print "goingBack!"
		return SingleLinkedList(),0
	else:
		n1Data = 0 if cNode1 is None else cNode1.data
		n2Data = 0 if cNode2 is None else cNode2.data
		
		res_ll,carry = sumList(None if cNode1 is None else cNode1.next,None if cNode2 is None else cNode2.next,recLev+1)
		s = (n1Data+n2Data+carry)
		print "sum:%s" % s
		carry,int_part = (0,s) if recLev == 0 else divmod(s,10)
		res_ll.appendNode(int_part,AppendMode.TOHEAD)
		#res_ll.appendNode(int_part)
		return res_ll,carry		


if __name__ == "__main__":
	
	l1 =[]
	l2 = []

	if len(argv) > 1:
		l1 = [int(e) for e in argv[1].split(',')]
		l2 = [int(e) for e in argv[2].split(',')]
		#print l
	
	sll1 = SingleLinkedList(l1,AppendMode.TOHEAD)
	sll1.printLinkedList()
	sll2 = SingleLinkedList(l2,AppendMode.TOHEAD)
	sll2.printLinkedList()
	r,carry = sumList(sll1.head,sll2.head,0)
	r.printLinkedList() 
