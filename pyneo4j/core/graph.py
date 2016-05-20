from __future__ import unicode_literals

try:
	"""
	For Using neo4j 3 bolt http://neo4j.com/docs/developer-manual/current/#driver-manual-index
	"""
	from neo4j.v1 import GraphDatabase as Neo4j3
	from neo4j.v1 import basic_auth
	from pyneo4j.cypher.cypher import Cypher
	from pyneo4j.cypher.node import Node
except ImportError as e:
	from neo4jrestclient.client import GraphDatabase as Neo4j2
	from neo4jrestclient.client import Node as Neo4jNode

class GraphDatabase(object):

	_host = None
	_graph = None
	_default_host = 'http://localhost:7474'

	def __new__(cls, *args, **kwargs):
		"""
		Return neo4j-driver ou neo4jrestclient object
		"""
		_auth = None
		if kwargs and ('user' or 'password') in list(kwargs.keys()):
			user = kwargs['user']
			password = kwargs['password']
			if 'bolt://' in cls._default_host:
				_auth = basic_auth(user, password)
			else:
				_url = 'http://{0}:{1}@localhost:7474'.format(user, password)
				cls.host = _url

		if 'bolt://' in cls._default_host:
			driver = Neo4j3.driver(cls._default_host)
			if _auth:
				driver.auth = _auth

			cls._graph = Cypher(driver)
			return cls._graph

		elif cls.host is not None and type(cls.host) is str:
			cls._graph = Neo4j2(cls.host)
			return cls._graph

		else:
			cls._graph = Neo4j2(cls._default_host)
			return cls._graph

	@property
	def host(self):
		return self._host

	@host.setter
	def host(self, val):
		self._host = val

	@classmethod
	def neo4j_version(cls, release):
		if release==3:
			cls._default_host = 'bolt://localhost'

	@classmethod
	def run(cls, cypher):
		if ('Node' and 'Cypher') in globals():
			return cls._graph.query(cypher)
		else:
			return cls._graph.query(cypher, returns=(Neo4jNode)) # Node class by neo4jrestclient