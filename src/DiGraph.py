from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


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
        return self.Edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
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
        if id1 in self.Nodes and id2 in self.Nodes and id2 not in self.Edges_out[id1] and weight >= 0 and id1 != id2:
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
            self.Nodes[node_id] = NodeData(node_id, pos)
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
        if node_id in self.Nodes:
            for edge in self.all_in_edges_of_node(node_id).keys():
                self.remove_edge(edge, node_id)

            for edge in self.all_out_edges_of_node(node_id).keys():
                self.remove_edge(edge, node_id)

            self.Nodes.pop(node_id)
            self.Edges_in.pop(node_id)
            self.Edges_out.pop(node_id)
            self.__mc += 1
            self.__nodeSize -= 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id2 in self.Edges_out.get(node_id1):
            self.Edges_out.get(node_id1).pop(node_id2)
            self.Edges_in.get(node_id2).pop(node_id1)
            self.__mc += 1
            self.__edgeSize -= 1
            return True
        return False

    def get_node(self, key: int) -> NodeData:
        return self.Nodes.get(key)
