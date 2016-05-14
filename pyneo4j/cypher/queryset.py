from __future__ import unicode_literals

from .node import NodeQuerySet

class QuerySet(object):
	label = None
	_graph = None
	_first_node = None
	
	def __new__(cls, label, *args, **kwargs):
		if kwargs and label:
			cls._nodes_by_labels = cls._graph.labels.get(label)
			_first_node = cls._nodes_by_labels.get(**kwargs)
			
			if len(_first_node)==1:
				NodeQuerySet.PROPERTY = list(kwargs.keys())[0]
				_first_node = _first_node[0]
				return NodeQuerySet(_first_node)

		return super(QuerySet, cls).__new__(cls)

	def __init__(self, label, *args, **kwargs):
		self.label = label

		if hasattr(self, '_nodes_by_labels') is False:
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

	def filter(self, **kwargs):
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