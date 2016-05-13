
from pyneo4j.core import graph
from pyneo4j.cypher.node import QuerySet

class GraphDatabase(graph.CoreGraphDatabase):
	_default_host = 'bolt://localhost'

class Node(GraphDatabase, QuerySet):
	
	def __init__(self, *args, **kwargs):
	    super(Node, self).__init__(*args, **kwargs)