from .node import NodeProxy, Node
from .label import LabelProxy

class Cypher(object):
	_driver = None
	_session = None

	def __init__(self, driver, *args, **kwargs):
		self._driver = driver
		self._session = driver.session()

	"""
	def __del__(self):
		return self._session.close()
	"""
	
	def query(self, cypher, **kwargs):
		cypher = [[Node(self._session, node)] for node in self._session.run(cypher)]
		cypher.reverse()
		return cypher

	@property
	def nodes(self):
		return NodeProxy(self._session)

	@property
	def labels(self):
		return LabelProxy(self._session)
	
