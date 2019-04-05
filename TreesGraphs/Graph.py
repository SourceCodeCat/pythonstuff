from GraphNode import *

class Graph:
	
	def __init__(self,nodes=[]):
		self.nodes = {}
		if len(nodes) > 0:
			for e in nodes:
				if e is not None:
					self.nodes[e.name]=e


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
		
			
 			
	def printGraph(self):
		for e in  self.nodes:
			print "%s: %s: %s" % (self.nodes[e].state,e,self.nodes[e].adjacentNodes)


###############################
#nodeList = [GraphNode(0,[1]),
#GraphNode(1,[2]),
#GraphNode(2,[0,3]),
#GraphNode(3,[2]),
#GraphNode(4,[6]),
#GraphNode(5,[4]),
#GraphNode(6,[5])]

##############################

#nodeList = [GraphNode(0,[1,4,5]),
#GraphNode(1,[3,4]),
#GraphNode(2,[1]),
#GraphNode(3,[2,4]),
#GraphNode(4,[]),
#GraphNode(5,[])]

##############################

#g = Graph(nodeList)
#g.BFSTraversal(0)
