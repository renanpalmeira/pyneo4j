from .node import Node

class LabelProxy(object):
	_session = None

	def __init__(self, session):
		self._session = session

	def get(self, label):
		return Label(self._session, label)

class Label(object):
	_nodes = None
	_label = None
	_session = None

	def __init__(self, session, label):
		self._session = session
		self._label = label

	def __len__(self):
		return len(self._nodes)

	def get(self, **kwargs):
		_match = 'MATCH (n:{0} {1}) RETURN n'
		self._nodes = self._session.run(_match)
		return [Node(self._session, node) for node in self._nodes]