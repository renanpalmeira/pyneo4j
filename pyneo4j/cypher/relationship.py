from pyneo4j.core.graph import GraphDatabase
from pyneo4j.utils import relationship_text

class RelationshipQuerySet(object):
	"""
	_graph a instance of main class of connection in neo4j (GraphDatabase)
	"""
	_graph = None
	_relationship = None
	_relationship_name = ''

	def __init__(self, *args, **kwargs):
		self._graph = GraphDatabase()
		_nodes = []
		_properties = kwargs

		for arg in args:
			if hasattr(arg, '_nodes_by_labels'): # Node object
				_nodes.append(arg)

			elif isinstance(arg, str): # name relationship
				self._relationship_name = relationship_text(arg)

		self._create_relationship(_nodes, self._relationship_name)

	def __repr__(self):
		if self.relationship:
			_id = self.relationship.id
			_url = self.relationship.url
			return '<Relationship#{0}: {1}>'.format(_id, _url)
		else:
			return '<Relationship#{0}>'.format(self._relationship_name.title())

	def _create_relationship(self, nodes, relationship):
		if type(nodes) is not list and len(nodes)!=2:
			return False

		if type(relationship) is not str:
			return False

		# get node by neo4j-driver/neo4jrestclient
		node_first = nodes[0].node
		node_last = nodes[1].node

		# get relationship by neo4j-driver/neo4jrestclient
		relationships = node_first.relationships.all(types=[relationship])

		relationships = [relationship.end for relationship in relationships]
		if not node_last in relationships: # not have't relationship
			relationship = relationship
			self.relationship = self._graph.relationships.create(node_first, relationship, node_last)
		else:
			self.relationship = relationships[relationships.index(node_last)]

		return True

class NodeRelationshipQuerySet(object):

	def __init__(self, relationship, *args, **kwargs):
		self.relationship = relationship

	def __repr__(self):
		_id_relationship = self.relationship.id
		_display = self.relationship.url
		
		return '<Relationship#{0}: {1}>'.format(_id_relationship, _display)

	def __getattr__(self, name, *args, **kwargs):
		if name in self.relationship.end.properties:
			return self.relationship.end.properties[name]
		raise KeyError("Relationship#{0} has no property {1}. Read more: http://goo.gl/TnbmHo/".format(self.relationship.id, name))