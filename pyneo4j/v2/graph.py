from pyneo4j.cypher.queryset import QuerySet
from pyneo4j.cypher.relationship import RelationshipQuerySet

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