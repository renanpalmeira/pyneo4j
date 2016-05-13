from unittest import TestCase

from pyneo4j import Node

class Pyneo4jTest(TestCase):
	def setUp(self):
		self.node = Node

	def test_node(self):
		self.assertEqual(len(self.node('Human', name='Rey')), 1)