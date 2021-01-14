In this project we'll be comparing runtimes for our graph related libraries.
We will be comparing what we coded with Python and previously with Java to the Python library Networkx.
The methods we're about to compare in this project are all ran on the same six Directed Weighted Graphs and these methods are:
* [shortest_path()](https://github.com/IlanShiyevich/Introduction-to-Programming-Systems/wiki/Shortest-Path-Comparison) - Finds the shortest path between two nodes(src & dest) taking into account the weight of the edges between them.
* [connected_component()](https://github.com/IlanShiyevich/Introduction-to-Programming-Systems/wiki/Connected-Component-Comparison)-Comparison) - Finds the Strongly Connected Component(SCC) that some node id1 is a part of.
* [connected_components()](https://github.com/IlanShiyevich/Introduction-to-Programming-Systems/wiki/Connected-Component(s)-Comparison) - Finds all the Strongly Connected Component(SCC) in the graph.

Each test is performed and ran with JetBrains ide's(Integrated development environment), PyCharm for python and IntelliJ for Java.  
The sizes of the graphs we're testing are(V - Veracities, E - Edges):
- 10V | 80E
- 100V | 800E
- 1,000V | 8,000E
- 10,000V | 80,000E
- 20,000V | 160,000E
- 30,000V | 240,000E

### About Networkx
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

**Open Source software for complex networks**
- Data structures for graphs, digraphs, and multigraphs
- Many standard graph algorithms
- Network structure and analysis measures
- Generators for classic graphs, random graphs, and synthetic networks
- Nodes can be "anything" (e.g., text, images, XML records)
- Edges can hold arbitrary data (e.g., weights, time-series)
- Open source 3-clause BSD license
- Well tested with over 90% code coverage
- Additional benefits from Python include fast prototyping, easy to teach, and multi-platform

[source](https://github.com/networkx/networkx.git) | [website](https://networkx.org/)

![netwrokx](https://pyviz-dev.github.io/pyviz/assets/networkx.png)
