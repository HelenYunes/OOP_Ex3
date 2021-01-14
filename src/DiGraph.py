from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    """This class represents a graph."""

    def __init__(self):
        super()
        self.Nodes = dict()
        self.Edges_out = dict()
        self.Edges_in = dict()
        self.__nodeSize = 0
        self.__edgeSize = 0
        self.__mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.Nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if id1 not in self.Nodes:
            return {}
        return self.Edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 not in self.Nodes:
            return {}
        return self.Edges_out.get(id1)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        nodes = self.get_all_v().keys()
        if id1 in nodes and id2 in nodes and id2 not in self.Edges_out[id1] and weight >= 0 and id1 != id2:
            self.Edges_in[id2][id1] = weight
            self.Edges_out[id1][id2] = weight
            self.__mc += 1
            self.__edgeSize += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.Nodes:
            self.Nodes[node_id] = NodeData(key=node_id, pos=pos)
            self.Edges_in.__setitem__(node_id, {})
            self.Edges_out.__setitem__(node_id, {})
            self.__mc += 1
            self.__nodeSize += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.Nodes:
            return False
        else:
            for edge in list(self.all_in_edges_of_node(node_id).keys()):
                self.remove_edge(edge, node_id)

            for edge in list(self.all_out_edges_of_node(node_id).keys()):
                self.remove_edge(node_id, edge)

            self.Nodes.pop(node_id)
            self.Edges_in.pop(node_id)
            self.Edges_out.pop(node_id)
            self.__mc += 1
            self.__nodeSize -= 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 not in self.Nodes or node_id2 not in self.Nodes or node_id1 == node_id2:
            return False
        if node_id2 in self.Edges_out.get(node_id1):
            self.Edges_out.get(node_id1).pop(node_id2)
            self.Edges_in.get(node_id2).pop(node_id1)
            self.__mc += 1
            self.__edgeSize -= 1
            return True
        return False

    def get_node(self, key: int) :
        return self.Nodes.get(key)

    def __eq__(self, other):
        if type(other) is not DiGraph:
            return False
        if self.e_size() != DiGraph.e_size(other):
            return False
        if self.v_size() != DiGraph.v_size(other):
            return False
        for node in self.Nodes.values():
            if NodeData.get_key(node) not in DiGraph.get_all_v(other).keys():
                return False
        return True

    def __repr__(self):
        return f"Graph: |V|={self.v_size()} , |E|={self.e_size()}"


class NodeData:
    def __init__(self, key: int, tag=0, pos: tuple = None):
        self.__key: int = key
        self.__tag = tag
        self.__info = "no"
        self.__parent = None
        self.__location = pos

    def get_location(self) -> [tuple]:
        return self.__location

    def set_location(self, x, y, z):
        self.__location = (x, y, z)

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def set_tag(self, tag: int):
        self.__tag = tag

    def get_tag(self) -> float:
        return self.__tag

    def get_parent(self) -> int:
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info: str):
        self.__info = info

    def __repr__(self):
        if self.__location is None:
            return '{ID:' + self.__key.__str__() + '}'
        else:
            return '{ID:' + self.__key.__str__() + ', Location:' + self.__location.__str__() + '}'

    def __lt__(self, other):
        return self.__tag < other.__tag

    def __gt__(self, other):
        return self.__tag > other.__tag
