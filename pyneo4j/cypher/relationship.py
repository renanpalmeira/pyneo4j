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

	@classmethod
	def _create_relationship(cls):
		pass