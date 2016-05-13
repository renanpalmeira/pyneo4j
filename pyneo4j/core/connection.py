from __future__ import unicode_literals

try:
	"""
	For Using neo4j 3 bolt http://neo4j.com/docs/developer-manual/current/#driver
	"""
	from neo4j.v1 import GraphDatabase, basic_auth
except ImportError as e:
	from neo4jrestclient.client import GraphDatabase

def connection(url):
	return GraphDatabase(url)