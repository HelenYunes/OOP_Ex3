import json
from queue import PriorityQueue
import math
from typing import List
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphFrame import GraphFrame
from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class GraphAlgo(GraphAlgoInterface):
    """This class represents a directed (positive) weighted graph theory algorithms."""

    def __init__(self, graph: GraphInterface = None):
        super()
        self.graph: DiGraph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name) as file:
                new_graph = DiGraph()
                json_file = json.load(file)
            for node in json_file["Nodes"]:
                key1 = node["id"]
                if "pos" not in node:
                    new_graph.add_node(key1, None)
                else:
                    pos = node["pos"]

                    pos = pos.replace("(", "").replace(")", "")

                    x, y, z = str.split(pos, ",")
                    x = float(x)
                    y = float(y)
                    z = float(z)
                    new_graph.add_node(key1, (x, y, z))
            for edge in json_file["Edges"]:
                source = edge["src"]
                destination = edge["dest"]
                weight = edge["w"]
                new_graph.add_edge(source, destination, weight)
            self.graph = new_graph
            file.close()
            return True
        except Exception as exception:
            print(exception)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        with open(file_name, 'w') as file:
            try:
                vertices = self.graph.get_all_v().values()
                in_edges = self.graph.Edges_in.keys()
                nodes = []
                edges = []
                for node in vertices:
                    key = node.get_key()
                    if node.get_location() is None:
                        nodes.append({"id": key})
                    else:
                        if node.get_location() is not None:
                            pos = node.get_location().__str__()
                            nodes.append({"pos": pos, "id": key})
                for destination in in_edges:
                    edges_in = self.graph.all_in_edges_of_node(destination)
                    for source, weight in edges_in.items():
                        edges.append({"src": source, "dest": destination, "w": weight})

                json.dump({"Edges": edges, "Nodes": nodes}, file)
                file.close()
                return True
            except Exception as exception:
                print(exception)
                return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        path = []
        nodes = self.graph.get_all_v()
        if id1 not in nodes.keys() or id2 not in nodes.keys():
            return math.inf, None
        if id1 == id2:
            path.append(id2)
            return 0, path
        self.reset_data(nodes)
        nodes = self.dijkstra(nodes, id1)
        distance = nodes[id2].get_tag()
        if distance == math.inf:
            return math.inf, None
        destination = id2
        while destination != -5:
            next_node = nodes[destination]
            destination = next_node.get_parent()
            path.insert(0, next_node.get_key())
        return nodes[id2].get_tag(), path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        node1 = self.graph.get_all_v().get(id1)
        count = 0
        scc1 = []
        scc = []
        after_dfs_scc = []
        if self.graph is None:
            return scc
        list_visit = []
        nodes = self.graph.get_all_v()
        if id1 not in nodes.keys():
            return scc
        self.reset_data(nodes)
        after_dfs_scc, scc1 = self.dfs_scc(scc, nodes, count, node1, list_visit)

        return scc1

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        scc = []
        scc1 = []
        count = 0
        after_dfs_scc = []
        if self.graph is None:
            return scc
        list_visit = []
        nodes = self.graph.get_all_v()
        self.reset_data(nodes)
        for node in nodes.values():
            if node.get_counter() is None:
                after_dfs_scc, scc1 = self.dfs_scc(scc, nodes, count, node, list_visit)

        return after_dfs_scc

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        GraphFrame(self.graph).draw_graph()

    def __eq__(self, other):
        if type(other) is not GraphAlgo:
            return False
        if self.graph.__eq__(GraphAlgo.get_graph(other)):
            return True
        return False

    def reset_data(self, nodes):
        for node in nodes.values():
            node.set_tag(math.inf)
            node.set_info("no")
            node.set_parent(None)
            node.set_counter(None)
            node.set_connected_components(None)

    def dijkstra(self, nodes: dict, id1: int) -> list:
        node1 = nodes[id1]
        node1.set_parent(-5)
        queue = PriorityQueue()
        queue.put(node1)
        node1.set_tag(0)
        while not (queue.empty()):
            vertex = queue.get()
            edges_out = self.graph.all_out_edges_of_node(vertex.get_key())
            for key, weight in edges_out.items():
                if vertex.get_tag() + weight < nodes[key].get_tag():
                    queue.put(nodes[key])
                    nodes[key].set_tag(vertex.get_tag() + weight)
                    nodes[key].set_parent(vertex.get_key())
        return nodes

    def dfs_scc(self, scc_from: [], nodes: [], count: int, current_node: NodeData, list_visit: []):

        current_key = current_node.get_key()
        out_edges = self.graph.all_out_edges_of_node(current_key)
        current_node.set_connected_components(count)
        current_node.set_counter(count)
        count += 1
        scc = []
        current_node.set_info("yes")
        list_visit.append(current_node)
        for vertex in list([nodes[destination]] for destination in out_edges):
            node = vertex.pop()
            if node.get_counter() is not None:
                if node.get_info().__eq__("yes"):
                    num = min(current_node.get_connected_components(), node.get_counter())
                    current_node.set_connected_components(num)
            else:
                if node.get_counter() is None:
                    self.dfs_scc(scc_from, nodes, count, node, list_visit)
                    num = min(current_node.get_connected_components(), node.get_connected_components())
                    current_node.set_connected_components(num)
        if current_node.get_connected_components() == current_node.get_counter():
            while list_visit.__len__() > 0:
                this_node = list_visit.pop()
                scc.insert(0, this_node.get_key())
                this_node.set_info("no")
                if this_node == current_node:
                    break
            scc_from.append(scc)
        return scc_from, scc
