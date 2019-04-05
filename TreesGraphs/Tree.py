from TreeNode import *

class Tree:
	def __init__(self,r=None):
		self.root = None
		if r is not None:
			self.root = r
		else:
			self.root = TreeNode()

	def __preOrderTraversal(self,node):
		
		if node is not None:
			print node.data
			self.__preOrderTraversal(node.lChild)
			self.__preOrderTraversal(node.rChild)

	def __inOrderTraversal(self,node):
		
		if node is not None:
			self.__inOrderTraversal(node.lChild)
			print node.data
			self.__inOrderTraversal(node.rChild)

	def __postOrderTraversal(self,node):

		if node is not None:
			self.__postOrderTraversal(node.lChild)
			self.__postOrderTraversal(node.rChild)
			print node.data

	def printInPreorder(self):
		self.__preOrderTraversal(self.root)

	def printInOrder(self):
		self.__inOrderTraversal(self.root)

	def printInPostOrder(self):
		self.__postOrderTraversal(self.root)
		
