import sys
import logging
import random
from unittest import TestCase
from pyneo4j import Node
from pyneo4j.utils import Q

class PyNeo4jTest(TestCase):
	def setUp(self):
		self.total = 143
		self.node = Node('Human', name='Rey')

	def test_node(self):
		self.assertEqual(len(self.node), 1)

	def test_relationship(self):
		lived = self.node.Lived()
		self.assertEqual(lived.name, 'Jakku') # case sensitive

	def test_filter_or(self):
		daughter, father = Node('Human').filter(Q(name='Rey') | Q(name='Luke Skywalker'))
		self.assertEqual(father.lived().name, 'Tatooine')
		self.assertEqual(daughter.lived().name, 'Jakku')

	def test_filter_multi_or(self):
		family = Node('*').filter(Q(id=random.randint(1, self.total)) | Q(id=5))

		querie_label = Node('Human', Q(id=random.randint(1, self.total)))
		querie_nodes = Node(Q(id=random.randint(1, self.total)))

		return True