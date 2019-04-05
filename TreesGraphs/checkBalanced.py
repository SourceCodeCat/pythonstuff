from Tree import *
from sys import *

#########################################################
# creates a Binary Search tree based on
# an ordered list of elements
########################################################			
def createBST(l):
	if(len(l)==0):
		return None
	else:
		middle = len(l)/2
		#print "middle value: %s" % l[middle]
		node = TreeNode(l[middle])
		node.lChild = createBST(l[:middle])
		node.rChild = createBST(l[middle+1:])
		return node

	
def getDepth(root,level):#,lss,rss):


	if root is not None:
		if root.lChild is not None:
			return getDepth(root.lChild,level+1)
		elif root.rChild is not None:
			return getDepth(root.rChild,level+1)
		else:
			print "Depth:%s" % level
			return level #print level
	else:
		return level

def isBalanced(root):
	if root is not None:
		left = getDepth(root.lChild,1)
		right = getDepth(root.rChild,1)
		return True if abs(left-right) < 2 else False
	else:
		print "root node was null, hence the tree has Depth:0"
		return True

		



if __name__ == "__main__":

	l = []
	if len(argv) > 1:
		l =[int(e) for e in argv[1].split(',')]
	print l
	
	###################################
	# This is a test case where it is 
	# not Balanced
	##################################	
	#n = TreeNode(1)
	#n.lChild = TreeNode(2)
	#n.rChild = TreeNode(3)
	#n.lChild.lChild = TreeNode(4)
	#n.lChild.rChild = TreeNode(5)
	#n.lChild.lChild.rChild = TreeNode(7)
	#t = Tree(n)	
	##################################		
	
	##################################
	# The create BST method creates a minimum 
	# BST from a ordered list of numbers...
	# therefore...it should be Balanced...
	##################################
	#t = Tree(createBST(l))
	##################################
	
	t = Tree()
	t.printInOrder()
	print isBalanced(t.root)
	

