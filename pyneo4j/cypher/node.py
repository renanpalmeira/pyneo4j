from .relationship import NodeRelationshipQuerySet

class NodeQuerySet(object):
	PROPERTY = None
	RELATIONSHIP_TEXT = lambda self, text: text.upper()

	def __init__(self, node, *args, **kwargs):
		self.node = node
		
	def __getattr__(self, name, *args, **kwargs):
		if name in self.node.properties:
			return self.node.properties[name]
		else:
			name = self.RELATIONSHIP_TEXT(name)
			def wrapper(*args, **kwargs):
				relationships = self.node.relationships.all(types=[name])
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

	def relationships(self):
		relationships = self.node.relationships.all()
		return [NodeRelationshipQuerySet(relationship) for relationship in relationships]