from LinkedList import *

class Stack(LinkedList):

	def __init__(self,args=[],mode=AppendMode.TOTAIL):
		self.head = None
		self.tail = None
		self.nodeCount = 0
		# If we received elements to create a llist from them...
		if len(args) > 0:
			for e in args:
				self.appendNode(e,mode)
				self.nodeCount +=1

	def pop(self):
		# pop() in A stack removes the object in the tail
		# and returns it
		if self.tail is not None:
			v = self.tail.data
			if self.head != self.tail:
				self.tail = self.tail.prev
				self.tail.next = None
			else:
				self.head,self.tail = None,None
			self.nodeCount -=1
			return v
		else:
			print "pop(): The stack is empty!!.."
			return None

	def peek(self):
		# peek returns the top of the stack without removing it
		if self.tail is not None:
			return self.tail.data
		else:
			print "peek(): The Stack is empty!!.."
			return None
	
	def push(self,data):
		# inserts a new node to the tail
		# in my implementation the append mode is AppendMode.TOTAIL
		self.appendNode(data)
		self.nodeCount +=1

	def isEmpty(self):
		# for this implementation I added a count variable
		return True if self.nodeCount == 0 else False

#	def deleteNode(self,data):
#		current = self.head
#		previous = None
#		while current is not None:
#			if current.data == data:
#				if previous is None:
#					self.head = self.head.next
#					self.head.prev = None
#				else:
#					previous.next = current.next
#					current.next.prev = previous
#			previous, current = current, current.next
			

#sll = Stack([9,8,7,6,5,4,3,2,1],AppendMode.TOTAIL)
#print "Original List:"
#sll.printLinkedList() 
#print "Print it BWDs"
#sll.printLinkedList(Direction.BWD)
