from Graph import *
from sys import *
"""
	def DFSTraversal(self,nodeName,level=0):
		# nodeName is the name of the node from where we want to
		# start the traversal.
		if nodeName not in self.nodes:
			return None
		else:
			print "%s%s" % (" "*level,self.nodes[nodeName].name)
			self.nodes[nodeName].state = GraphNodeState.VISITED
			for n in self.nodes[nodeName].adjacentNodes:
				if self.nodes[n].state == GraphNodeState.NOT_VISITED:
					self.DFSTraversal(n,level+1)
		

		
	def BFSTraversal(self,nodeName):
		queue = []
		if nodeName not in self.nodes:
			print "The node doesn't exist"
		else:
			queue.append(nodeName)
			while len(queue) > 0:
				n = self.nodes[queue.pop(0)]
				if n.state == GraphNodeState.NOT_VISITED:
					n.state = GraphNodeState.VISITED
					print n.name
					queue.extend(n.adjacentNodes)
		
"""			

def hasRoute(g,startNode,endNode):
	queue = []
		
	if startNode not in g.nodes or endNode not in g.nodes:
		print "One of the nodes doesn't exist"
		return False
	else:
		queue.append(startNode)
		while len(queue) > 0:
			n = g.nodes[queue.pop(0)]
			if n.state == GraphNodeState.NOT_VISITED:
				n.state = GraphNodeState.VISITED
				#print n.name
				if n.name == endNode:
					return True
		
				queue.extend(n.adjacentNodes)
		return False

'''
def DFSTraversal(self,nodeName,level=0):
	# nodeName is the name of the node from where we want to
	# start the traversal.
	if nodeName not in self.nodes:
		return None
	else:
		print "%s%s" % (" "*level,self.nodes[nodeName].name)
		self.nodes[nodeName].state = GraphNodeState.VISITED
		for n in self.nodes[nodeName].adjacentNodes:
			if self.nodes[n].state == GraphNodeState.NOT_VISITED:
				self.DFSTraversal(n,level+1)

'''

def DFSTraversal(nodeName,nDep,wDep):
	n = g.nodes[nodeName]
	##print "entering node:"+n.name
	if n.state is GraphNodeState.NOT_VISITED:
		n.state = GraphNodeState.VISITED
		if len(n.adjacentNodes) > 0:
			#wDep.append(n.name)	
			##print n.adjacentNodes		
			for node in n.adjacentNodes:
				##print "checking node: %s" % node
				nDep,wDep = DFSTraversal(node,nDep,wDep)
			wDep.append(n.name)
			return nDep,wDep
		else:
			##print "it is empty"
			nDep.append(n.name)
			n.status = GraphNodeState.VISITED
			##print "returning nDep:%s, wDep:%s" % (nDep,wDep)
			return nDep,wDep
	else:
		return nDep,wDep


def findBuildSequence(nDep,wDep):
	k = g.nodes.keys()
	for e in k:
		nDep,wDep = DFSTraversal(e,nDep,wDep)

	return nDep,wDep

if __name__== "__main__":

	#nodeList = [GraphNode('a',['f']),
	#GraphNode('b',['f']),
	#GraphNode('c',['d']),                 			
	#GraphNode('d',['a','b']),
	#GraphNode('e',[]),
	#GraphNode('f',[])]




	nodeList = [GraphNode('a',['e']),
	GraphNode('b',['a','e','h']),
	GraphNode('c',['a']),
	GraphNode('d',['g']),
	GraphNode('e',[]),
	GraphNode('f',['a','b','c']),
	GraphNode('g',[]),
	GraphNode('h',[])]




	g = Graph(nodeList)
	g.printGraph()

	a,b = findBuildSequence([],[])
	a.extend(b)
	print a




