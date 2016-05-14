import six
from pyneo4j.core import graph
from pyneo4j.cypher.queryset import QuerySet

class GraphDatabase(graph.CoreGraphDatabase):
	_default_host = 'bolt://localhost'

class Node(six.with_metaclass(GraphDatabase, QuerySet)):
	"""
	Using six to metaclass graphdatabase and inheritance queryset
	"""
	def __init__(self, *args, **kwargs):
		QuerySet.__init__(self, *args, **kwargs)