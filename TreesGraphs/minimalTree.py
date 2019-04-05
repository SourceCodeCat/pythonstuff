from Tree import *
from sys import *

			
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
				
def visitPreOrder(node):
	if node is not None:
		print node.data
		visitPreOrder(node.lChild)
		visitPreOrder(node.rChild)

		



if __name__ == "__main__":

	l = []
	if len(argv) > 1:
		l =[int(e) for e in argv[1].split(',')]
	print l
		
	t = Tree(createBST(l))

###################################
# for this case it should be
# PreOrder: 12453
# InOrder: 42513
# PostOrder: 45231

#	n = TreeNode(1)
#	n.lChild = TreeNode(2)
#	n.rChild = TreeNode(3)
#	n.lChild.lChild = TreeNode(4)
#	n.lChild.rChild = TreeNode(5)
#	t = Tree(n)

##################################		
	#visitPreOrder(t.root)	
	print "--PreOrder--"
	t.printInPreorder()
	print "--InOrder--"
	t.printInOrder()
	print "--PostOrder--"
	t.printInPostOrder()
	
	

