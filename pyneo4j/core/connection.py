from __future__ import unicode_literals

try:
	"""
	For Using neo4j 3 bolt http://neo4j.com/docs/developer-manual/current/#driver-manual-index
	"""
	from neo4j.v1 import GraphDatabase, basic_auth
except ImportError as e:
	from neo4jrestclient.client import GraphDatabase
	from neo4jrestclient.client import Node as Neo4jNode

gdb = None

def connection(url):
	global gdb
	gdb = GraphDatabase(url)
	return gdb

def run(cypher):
	return gdb.query(cypher, returns=(Neo4jNode))