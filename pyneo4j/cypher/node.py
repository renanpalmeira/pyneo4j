from .relationship import NodeRelationshipQuerySet
from pyneo4j.utils import relationship_text

class NodeQuerySet(object):
	PROPERTY = None

	def __init__(self, node, *args, **kwargs):
		self.node = node
		
	def __getattr__(self, name, *args, **kwargs):
		if name in self.node.properties:
			return self.node.properties[name]
		elif name=='id':
			return self.node.id
		else:
			name = relationship_text(name)
			def wrapper(other=None, *args, **kwargs):
				relationships = self.node.relationships.all(types=[name])

				if other is not None:
					queryset = None
					relationships = [relationship.end for relationship in relationships]
					other = other.node # get node by neo4j-driver/neo4jrestclient
					if not other in relationships: # not have't relationship
						queryset = self.node.relationships.create(name, other)
					else:
						queryset = relationships[relationships.index(other)]

					if queryset:
						return NodeRelationshipQuerySet(queryset)
					return None

				if len(relationships)==1:
					return NodeRelationshipQuerySet(relationships[0])
				return [NodeRelationshipQuerySet(relationship) for relationship in relationships]
			return wrapper

	def __len__(self):
		return 1

	def __repr__(self):
		_id_node = self.node.id
		_display = self.node.url
		
		if self.PROPERTY is not None:
			_display = self.node.properties[self.PROPERTY].encode('ascii', 'ignore')
		
		return '<Node#{0}: {1}>'.format(_id_node, _display)