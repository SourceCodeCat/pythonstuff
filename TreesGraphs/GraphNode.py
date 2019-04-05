from enum import Enum

class GraphNodeState(Enum):
	NOT_VISITED = 1
	VISITED = 2
	WORKING_ON_IT = 3

class GraphNode:

	def __init__(self,name=None,adjacentNodes=[]):

		self.adjacentNodes = adjacentNodes
		self.state = GraphNodeState.NOT_VISITED 		
		if name is None:
			print "the Node name has to be specified..."
			return None
		self.name = name


		
		
