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



if __name__== "__main__":

	nodeList = [GraphNode(0,[1,4,5]),
	GraphNode(1,[3,4]),
	GraphNode(2,[1]),                 			
	GraphNode(3,[2,4]),
	GraphNode(4,[]),
	GraphNode(5,[])]

	g = Graph(nodeList)
	g.printGraph()
	startNode = 4
	endNode = 2
	print "Is there a route between node %s and node %s??" % (startNode,endNode)
	print hasRoute(g,startNode,endNode)

