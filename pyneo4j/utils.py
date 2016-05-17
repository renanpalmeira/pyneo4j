from .cypher.queries import Q
from .core.connection import run

PREFIX_ALL_NODES = ['*', 'n', '']

def relationship_text(text, lookup='upper'):
	return getattr(text, lookup)()

def queries_nodes(label, matchs):

	if label in PREFIX_ALL_NODES:
		cypher = """MATCH (cypher) WHERE {0} RETURN cypher"""
	else:
		cypher = """MATCH (cypher:{0}) WHERE {1} RETURN cypher"""

	queries = ''	
	index = 1
	last = len(matchs)
	for key, value in matchs:
		if key.upper()=='ID':
			queries += 'ID(cypher)={0}'.format(value)
		else:	
			queries += 'cypher.{0}="{1}"'.format(key, value)
		if not index==last:
			queries += ' OR '
		index += 1
	if label in PREFIX_ALL_NODES:
		cypher = cypher.format(queries)
	else:
		cypher = cypher.format(label, queries)

	return run(cypher)