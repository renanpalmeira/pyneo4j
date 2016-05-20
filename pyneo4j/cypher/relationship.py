class RelationshipsProxy(object):
	_relationships = None
	_session = None

	def __init__(self, session, relationships=None):
		self._session = session

		if relationships:
			self._relationships = relationships

	def __len__(self):
		return len(self._relationships)

	def __getitem__(self, pos):
		return Relationship(self._relationships[pos])

	def all(self, types):
		match = 'MATCH (n:{0} {1})-[r:{2}]->(out) RETURN n, r, out'
		self._relationships = list(self._session.run(match))
		return RelationshipsProxy(self._session, self._relationships)

	def get(self, label):
		return RelationshipsProxy(self._session, label)

class Relationship(object):

	_nodes = None
	_label = None
	_session = None

	def __init__(self, relationship):
		self._relationship = relationship

	@property
	def end(self):
		if 'r' in self._relationship.keys():
			return Relationship(self._relationship['out'])
		return None

	@property
	def properties(self):
		return self._relationship