from .cypher.queries import Q
from .core.connection import run

PREFIX_ALL_NODES = ['*', 'n', '']

def to_nodes(label, matchs):

	if label in PREFIX_ALL_NODES:
		cypher = """MATCH (cypher) WHERE {} RETURN cypher"""
	else:
		cypher = """MATCH (cypher:{}) WHERE {} RETURN cypher"""
	
	queries = ''	
	index = 1
	last = len(matchs)
	for key, value in matchs:
		if key.upper()=='ID':
			queries += 'ID(cypher)={}'.format(value)
		else:	
			queries += 'cypher.{}="{}"'.format(key, value)
		if not index==last:
			queries += ' OR '
		index += 1
	if label in PREFIX_ALL_NODES:
		cypher = cypher.format(queries)
	else:
		cypher = cypher.format(label, queries)
	return run(cypher)