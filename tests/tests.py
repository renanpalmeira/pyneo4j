import sys
import logging
from unittest import TestCase
from pyneo4j import Node

class PyNeo4jTest(TestCase):
	def setUp(self):
		self.node = Node('Human', name='Rey')

	def test_node(self):
		self.assertEqual(len(self.node), 1)

	def test_relationship(self):
		lived = self.node.Lived()
		self.assertEqual(lived.name, 'Jakku') # case sensitive