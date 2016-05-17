from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES=[]

setup(
    name='pyneo4j',
    version='0.0.0',
    author='Renan Palmeira',
    author_email='renanpalmeira1@hotmail.com',
    description='A Python client library for Neo4j',
    license='GPL',
    url='https://pyneo4j.readthedocs.org/en/latest/',
    keywords='neo4j pyramid flask django neo4j graph graphdb graphdatabase database rest client driver',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=[
        'requests',
        'six',
    ],
    tests_require=[
        'nose>=1.0',
        'requests>=0.4.1',
        'nose-regression>=1.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5 ',
    ],
)