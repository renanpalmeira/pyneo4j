from .queryset.queries import Q
from .core.graph import GraphDatabase

PREFIX_ALL_NODES = ['*', 'n', '']

def relationship_text(text, lookup='upper'):
	return getattr(text, lookup)()

def queries_nodes(label, matchs):

	if label in PREFIX_ALL_NODES:
		cypher = """MATCH (n) WHERE {0} RETURN n"""
	else:
		cypher = """MATCH (n:{0}) WHERE {1} RETURN n"""

	queries = ''	
	index = 1
	last = len(matchs)
	for key, value in matchs:
		if key.upper()=='ID':
			queries += 'ID(n)={0}'.format(value)
		else:	
			queries += 'n.{0}="{1}"'.format(key, value)
		if not index==last:
			queries += ' OR '
		index += 1
	if label in PREFIX_ALL_NODES:
		cypher = cypher.format(queries)
	else:
		cypher = cypher.format(label, queries)

	return GraphDatabase.run(cypher)