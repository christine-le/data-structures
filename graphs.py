#4.1 Route Between Nodes:  Given a directed graph, find out whether there is a route between two nodes.

#BFS
class Node:
	def __init__(self, val):
		self.val = val
		self.edges = []
		self.visited = False

class Graph:
	def __init__(self, node):
		self.root = node

	def routeExists(self, start, end):
		edges = [self.root]
		isStart = False

		for edge in edges:
			if edge == start:
				isStart = True

			if isStart == True and edge == end:
				return True

			if edge.visited == False:
				edges.extend(edge.edges)
				edge.visited = True

		return False

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n0.edges = [n1]
n1.edges = [n2]
n2.edges = [n0, n1, n3]

g = Graph(n0)

# print 'Node 3 to Node 1', g.routeExists(n3, n1)
print 'Node 0 to Node 2', g.routeExists(n0, n2)