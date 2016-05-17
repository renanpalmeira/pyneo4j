import six
from pyneo4j.core import graph
from pyneo4j.cypher.queryset import QuerySet
from pyneo4j.cypher.relationship import RelationshipQuerySet

class GraphDatabase(graph.CoreGraphDatabase):
	_default_host = 'http://localhost:7474'

class Node(six.with_metaclass(GraphDatabase, QuerySet)):
	"""
	Using six to metaclass graphdatabase and inheritance queryset
	"""
	def __init__(self, *args, **kwargs):
		QuerySet.__init__(self, *args, **kwargs)

class Relationship(six.with_metaclass(GraphDatabase, RelationshipQuerySet)):
	"""
	Using six to metaclass graphdatabase and inheritance queryset
	"""
	def __init__(self, *args, **kwargs):
		RelationshipQuerySet.__init__(self, *args, **kwargs)