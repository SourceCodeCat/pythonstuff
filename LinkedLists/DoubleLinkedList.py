from LinkedList import *

class DoubleLinkedList(LinkedList):

	def __init__(self,args=[],mode=AppendMode.TOTAIL):
		self.head = None
		self.tail = None
        # If we received elements to create llist from them...
		if len(args) > 0:
			for e in args:
				self.appendNode(e,mode)

	def deleteNode(self,data):
		current = self.head
		previous = None
		while current is not None:
			if current.data == data:
				if previous is None:
					self.head = self.head.next
					self.head.prev = None
				else:
					previous.next = current.next
					current.next.prev = previous
			previous, current = current, current.next
			

#sll = DoubleLinkedList(AppendMode.ATOTAIL,9,8,7,6,5,4,3,2,1)
#print "Original List:"
#sll.printLinkedList() 
#sll.deleteNode(5)
#print "Updated List:"
#sll.printLinkedList()
#print "Print it BWDs"
#sll.printLinkedList(Direction.BWD)
