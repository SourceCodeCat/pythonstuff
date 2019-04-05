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
				
def nodesPerLevel(root,level,l):
	#print l	
	if root is not None:
		if len(l) >= level:
			l[level-1].append(root.data)
		else:
			l.append([root.data])
		
		l = nodesPerLevel(root.lChild,level+1,l)
		l = nodesPerLevel(root.rChild,level+1,l)
		return l
	else:
		return l
		
		



if __name__ == "__main__":

	l = []
	if len(argv) > 1:
		l =[int(e) for e in argv[1].split(',')]
	print l
		
	t = Tree(createBST(l))
	print nodesPerLevel(t.root,1,[])
	

