from .relationship import RelationshipsProxy

class NodeProxy(object):
	_session = None

	def __init__(self, session):
		self._session = session

	def get(self, node):
		return Node(self._session, node)

class Node(object):
	_node = None
	_session = None

	def __init__(self, session, node):
		self._session = session
		self._node = node

	@property
	def id(self):
		return self._node['n'].id

	@property
	def url(self):
		return 'self._url'

	@property
	def relationships(self):
		return RelationshipsProxy(self._session)

	@property
	def properties(self):
		return self._node['n']