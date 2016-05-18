# PyNeo4j

Integrating Python with Neo4j.

[![Build Status](https://travis-ci.org/RenanPalmeira/pyneo4j.svg?branch=master)](https://travis-ci.org/RenanPalmeira/pyneo4j) [![PyPI](https://img.shields.io/pypi/v/pyneo4j.svg)](https://pypi.python.org/pypi/pyneo4j)

### Demo/Example

https://github.com/RenanPalmeira/neopyramid

### Downloaded and run Neo4j 
	 
http://neo4j.com/download/

### Development

	$ git clone https://github.com/renanpalmeira/pyneo4j
	$ cd pyneo4j # or other name with virtualenv (recommended)
	$ pip install -e .
	$ pip install -r requirements.txt # or tests/requirements-dev.txt
	$ $NEO4J_FOLDER/bin/neo4j-shell -c < tests/starwars.cypher  # Import sample graph's
	$ nosetests --verbose tests/ # If your Neo4j needs authentication set on tests/tests.py, but not in 'git add' with your credentials, than just run the tests

### Installation (waiting for approval)

Available in Python Package Index:

$ pip install pyneo4j

Or:

$ easy_install pyneo4j
