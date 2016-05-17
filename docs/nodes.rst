Nodes
=====

	from pyneo4j import Node
	Node(label)

Querying
--------

* Retrieving all objects

	>>> Node('*').all() # or Node(label='*').all()
	[<Node#id: property>, <Node#id: property>, <Node#id: property>, <Node#id: property>]

* Retrieving specific objects with filters

	>>> Node('Python').filter(name='Guido')
	[<Node#id: property>,]

* Retrieving a single object with get

	>>> Node('Neo4j').get(name='Emil Eifrem')
	<Node#id: property>

	>>> Node('*').get(id=42)
	<Node#id: property>

* Retrieving specific objects with filters/conditions
  
  	>>> from pyneo4j.utils import Q


  	>>> a, b = Node('Human').filter(Q(name='Rey') | Q(name='Luke Skywalker'))
  	>>> a
  	<Node#id: property>
  	>>> b
  	<Node#id: property>

	
	>>> Node('Human', Q(id=42))
	>>> Node(Q(name='BB8'))