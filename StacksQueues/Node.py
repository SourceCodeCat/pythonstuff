class Node:

	def __init__(self,d=None,p=None,n=None):
		
		self.prev = p
		self.next = n
		self.data = d

	def getPrev(self):
		return self.prev
	def getNext(self):
		return self.next
	def getData(self):
		return self.data
	def setData(self,d):
		self.data = data
	def setPrev(self,node):
		self.prev = node
	def setNext(self,node):
		self.next = node


