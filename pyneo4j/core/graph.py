from .connection import connection

class CoreGraphDatabase(type):
	_graph = None
	_default_host = None

	def __new__(cls, name, bases, attrs):
		cls = type.__new__(cls, name, bases, attrs)
		cls._graph = connection(cls._default_host)
		return cls