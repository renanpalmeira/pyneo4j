from __future__ import unicode_literals

import six
from pyneo4j.core.connection import run

class Q(object):
	"""
	Queries for Neo4j MATCH's inspired by Django queries (https://goo.gl/fg0QUd)
	"""
	children = tuple()

	def __init__(self, **kwargs):
		self.children = tuple(kwargs.items())

	def __or__(self, other):
		other.children += self.children
		return other

	def __str__(self):
		queryset = ''
		
		index = 1
		last = len(self.children)
		for key, value in self.children:
			queryset += '(\'{0}\': \'{1}\')'.format(key, value)
			if not index==last:
				queryset += ', '
			index += 1

		return('<Q: (OR: {})>'.format(queryset))