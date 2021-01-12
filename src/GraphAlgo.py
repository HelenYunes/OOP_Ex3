import json
from queue import PriorityQueue
import math
from typing import List
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphFrame import GraphFrame
from src.GraphInterface import GraphInterface


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
        if id1 not in nodes or id2 not in nodes:
            return math.inf, path
        if id1 == id2:
            path.append(id2)
            return 0, path
        self.reset_data(nodes)
        nodes = self.dijkstra(nodes, id1)
        distance = nodes[id2].get_tag()
        if distance == math.inf:
            return math.inf, path
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

        scc = set()
        scc1 = []
        count = 0
        cc = []
        keys = {}
        num_connected_components = {}
        nodes = self.graph.get_all_v()
        scc2 = {}
        if self.graph is None:
            return scc1
        list_visit = []
        if id1 not in nodes:
            return scc1
        scc3 = self.dfs_scc(cc, scc, nodes, count, id1, list_visit, keys, num_connected_components, scc2)
        return scc3

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        scc = set()
        scc1 = []
        count = 0
        cc = []
        num_connected_components = {}
        if self.graph is None:
            return scc1
        list_visit = []
        nodes_after_scc = {}
        scc2 = {}
        nodes = self.graph.get_all_v()
        for node in nodes:
            if node not in nodes_after_scc:
                self.dfs_scc(cc, scc, nodes, count, node, list_visit, nodes_after_scc, num_connected_components, scc2)
        return cc

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

    def dfs_scc(self, cc, from_scc, nodes, count: int, current_node, list_visit, nodes_after_scc,
                num_connected_components, scc):
        list_visit = [current_node]
        i = 0
       
        while len(list_visit) > 0:
            current_node = list_visit[len(list_visit) - 1]
            if current_node in nodes_after_scc:
                pass
            else:
                vertex = nodes.get(current_node)
                vertex_key = [vertex.get_key()]
                nodes_after_scc.update({current_node: count})
                scc.update({count: vertex_key})
                num_connected_components.update({current_node: count})
                count = count + 1

                # print(vertex_key)
            edges = self.graph.all_out_edges_of_node(current_node)
            flag_visited = 1
            iter_edge = iter(edges)
            for i in edges:
                if i not in nodes_after_scc:
                    flag_visited = 0
                    list_visit.append(i)
                    break
            if flag_visited == 1:
                list_visit.pop()
                current_cc = num_connected_components.__getitem__(current_node)
                for j in edges:
                    if j in num_connected_components and j not in from_scc:
                        a = num_connected_components.__getitem__(current_node)
                        b = num_connected_components.__getitem__(j)
                        num_min_connected = min(a, b)
                        num_connected_components.update({current_node: num_min_connected})
                a = num_connected_components.__getitem__(current_node)
                b = nodes_after_scc.__getitem__(current_node)
                if a != b:
                    if a not in scc:
                        scc.update({a: [current_node]})
                    current_list = scc.get(current_cc)
                    for i in current_list:
                        scc[a].append(i)
                        current = num_connected_components.__getitem__(current_node)
                        num_connected_components.update({i: current})
                elif a == b:
                    cc.insert(0, scc[num_connected_components.__getitem__(current_node)])
                    for component in scc[num_connected_components[current_node]]:
                        from_scc.add(component)
        return scc[num_connected_components[current_node]]
