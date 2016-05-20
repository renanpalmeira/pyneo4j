from __future__ import unicode_literals

from .node import NodeQuerySet
from .queries import Q as Queries
from pyneo4j.core.graph import GraphDatabase
from pyneo4j.utils import PREFIX_ALL_NODES, queries_nodes

class QuerySet(object):
	label = None
	# _graph a instance of main class of connection in neo4j (GraphDatabase)
	_graph = None
	_first_node = None
	
	def __new__(cls, label, *args, **kwargs):
		obj = None

		cls._graph = GraphDatabase()

		def _create_queries(label, obj):
			_nodes = queries_nodes(label, obj.children)
			result = [NodeQuerySet(node[0]) for node in _nodes]
			result.reverse()
			return result

		if kwargs and label:
			cls._nodes_by_labels = cls._graph.labels.get(label)
			_first_node = cls._nodes_by_labels.get(**kwargs)
			
			if len(_first_node)==1:
				NodeQuerySet.PROPERTY = list(kwargs.keys())[0]
				_first_node = _first_node[0]
				return NodeQuerySet(_first_node)


		if len(args)>0 and type(args[0])==Queries and hasattr(args[0], 'children'):
			"""
			Check if user send Queries (Q(Label, id=...)) and label
			"""
			obj = args[0]

		if type(label)==Queries and hasattr(label, 'children') and obj is not None:
			"""
			Just send Queries (Q(id=...))
			"""
			obj = label
			return _create_queries('*', obj)

		elif obj and label:
			return _create_queries(label, obj)

		return super(QuerySet, cls).__new__(cls)

	def __init__(self, label, *args, **kwargs):
		self.label = label

		if self.label in PREFIX_ALL_NODES:
			# Inspired by http://neo4j.com/docs/stable/query-match.html#match-get-all-nodes
			self.label = '*'
			self._nodes_by_labels = self._graph.nodes

		elif hasattr(self, '_nodes_by_labels') is False:
			self._nodes_by_labels = self._graph.labels.get(self.label)

	def __repr__(self):
		return '<Neo4j Node: {0}>'.format(self.label)
		
	def _node_filter(self, **kwargs):
		result = [NodeQuerySet(node) for node in self._nodes_by_labels.get(**kwargs)]
		result.reverse()
		return result

	def _node_get(self, id_node):
		result = self._graph.nodes.get(id_node)
		return NodeQuerySet(result)

	def _node_all(self):
		return self._node_filter()

	def _insert(self):
		pass

	def filter(self, obj=None, **kwargs):
		if obj is not None and not kwargs and hasattr(obj, 'children'):
			_nodes = queries_nodes(self.label, obj.children)
			result = [NodeQuerySet(node[0]) for node in _nodes]
			result.reverse()
			return result
		return self._node_filter(**kwargs)

	def get(self, **kwargs):
		if 'id' in kwargs.keys():
			result = self._node_get(kwargs['id'])
		else:
			result = self._node_filter(**kwargs)
			result = result[0]

		if len(result)!=1:
			raise ValueError("None has no property. Read more: http://goo.gl/TnbmHo/")
		return result
	
	def all(self):
		return self._node_all()