from MyNode import Node
from enum import Enum
from abc import ABCMeta,abstractmethod

class Direction(Enum):
	
	FWD = 1
	BWD = 2
class AppendMode(Enum):
	
	TOTAIL = 1
	TOHEAD = 2

class LinkedList:
	__metaclass__ = ABCMeta
	
	def appendNode(self,data,mode=AppendMode.TOTAIL):
		#print self.__class__.__name__
		# inserts a node at the end of the list
		if self.head is None:
			self.head= Node(data)
		else:
			if mode == AppendMode.TOTAIL:
				self.appendToTail(data)
			else:
				self.appendToHead(data)

	def appendToTail(self,data):

		if self.tail is None:
                           #(DATA,PREV     ,NEXT)
			self.tail = Node(data,self.head)
			self.head.next = self.tail
		else:
			self.temp = Node(data,self.tail)
			self.tail.next = self.temp
			self.tail = self.temp	

	def appendToHead(self,data):

		temp = Node(data,None,self.head)
		self.head.prev = temp
		self.tail = self.head
		self.head = temp

	@abstractmethod
	def deleteNode(self,data):
		pass
	
		


	def printLinkedList(self,direction = Direction.FWD):
		
		current = self.head if direction == Direction.FWD else self.tail
		result = ""
		while current is not None:
			#print current.data
			 
		#	result = result + str(current.data) + ("-->" if current.next is not None else "") if direction == Direction.FWD else ("<--" if current.prev is not None else "")
			result = result + str(current.data) + (("-->" if direction == Direction.FWD else "<--") if (current.next if direction == Direction.FWD else current.prev) is not None else "") 
			current = current.next if direction == Direction.FWD else current.prev
		print result

					
				
#ll = LinkedList(AppendMode.ATOHEAD,4,5,6)
#ll.printLinkedList(Direction.FWD)
