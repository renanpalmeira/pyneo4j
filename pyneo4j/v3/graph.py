from pyneo4j.core.graph import GraphDatabase
from pyneo4j.queryset.queryset import QuerySet
from pyneo4j.queryset.relationship import RelationshipQuerySet

GraphDatabase.neo4j_version(3)

class Node(QuerySet):
	"""
	Using six to metaclass graphdatabase and inheritance queryset
	"""
	def __init__(self, *args, **kwargs):
		super(Node, self).__init__(*args, **kwargs)

class Relationship(RelationshipQuerySet):
	"""
	Using six to metaclass graphdatabase and inheritance queryset
	"""
	def __init__(self, *args, **kwargs):
		RelationshipQuerySet.__init__(self, *args, **kwargs)