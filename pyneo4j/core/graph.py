from .connection import connection

class GraphDatabase(object):

	_host = None
	_default_host = 'http://localhost:7474'

	def __new__(cls, *args, **kwargs):
		if kwargs and ('user' or 'password') in list(kwargs.keys()):
			user = kwargs['user']
			password = kwargs['password']
			_url = 'http://{0}:{1}@localhost:7474'.format(user, password)
			cls.host = _url

		"""
		Return neo4j-driver ou neo4jrestclient object
		"""
		if cls.host is not None and type(cls.host) is str:
			return connection(cls.host)
		else:
			return connection(cls._default_host)

	@property
	def host(self):
		return self._host

	@host.setter
	def host(self, val):
		self._host = val