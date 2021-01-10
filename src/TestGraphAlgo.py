import unittest
import math
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData

class TestGraphAlgo(unittest.TestCase):

    def build_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0,1,1.5)
        graph.add_node(2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 1.6)
        graph.add_node(3)
        graph.add_edge(2, 3, 1.5)
        graph.add_node(4)
        graph.add_edge(3, 4, 2.5)
        graph.add_edge(0, 4, 0.5)
        graph.add_edge(4, 0, 0.5)
        graph.add_edge(1,0,5)
        return graph

    def build_empty_graph(self):
        graph = DiGraph()
        return graph

    def test_json(self):
        graph = self.build_graph()
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a, graph)
        self.assertTrue(graph_a.save_to_json('saved.txt'))
        self.assertTrue(graph_a.load_from_json('saved.txt'))
        self.assertEqual(graph, graph_a.get_graph())

        graph = self.build_empty_graph()
        GraphAlgo.__init__(graph_a, graph)
        self.assertTrue(graph_a.save_to_json('saved.txt'))
        self.assertTrue(graph_a.load_from_json('saved.txt'))
        self.assertEqual(graph, graph_a.get_graph())

    def test_shortest_path(self):
        graph = self.build_graph()
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a,graph)

        path_len = graph_a.shortest_path(2,4).__getitem__(0)
        path_list = graph_a.shortest_path(2,4).__getitem__(1)
        expected_list = [NodeData(2), NodeData(3), NodeData(4)]
        self.assertEqual(4,path_len)
        self.assertEqual(3, len(path_list))
        self.assertEqual(expected_list.__str__(), path_list.__str__())

        path_len = graph_a.shortest_path(1, 4).__getitem__(0)
        path_list = graph_a.shortest_path(1, 4).__getitem__(1)
        expected_list = [NodeData(1), NodeData(0), NodeData(4)]
        self.assertEqual(5.5, path_len)
        self.assertEqual(3, len(path_list))
        self.assertEqual(expected_list.__str__(), path_list.__str__())

        graph = self.build_empty_graph()
        graph_a.__init__(graph)
        path_len = graph_a.shortest_path(1, 50).__getitem__(0)
        path_list = graph_a.shortest_path(1, 50).__getitem__(1)
        self.assertEqual(math.inf, path_len)
        assert path_list is None


    def test_connected_component(self):
        graph = self.build_graph()
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a, graph)

        is_connected = graph_a.connected_component(3).__getitem__(0)
        self.assertEqual(5,len(is_connected))

        graph.remove_edge(2,3)
        GraphAlgo.__init__(graph_a, graph)

        is_connected = graph_a.connected_component(3).__getitem__(0)
        self.assertEqual(5, len(is_connected))

        graph.remove_edge(3, 4)
        graph.add_edge(2,4,10)
        GraphAlgo.__init__(graph_a, graph)

        is_connected = graph_a.connected_component(3).__getitem__(0)
        self.assertEqual(1, len(is_connected))

        graph = self.build_empty_graph()
        GraphAlgo.__init__(graph_a, graph)
        self.assertEqual(0, len(graph_a.connected_components()))

    def test_connected_components(self):
        graph = self.build_graph()
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a, graph)
        connected = graph_a.connected_components().__getitem__(0)
        self.assertEqual(5, len(connected))

        graph.remove_edge(3, 4)
        graph.remove_edge(2, 3)
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a, graph)
        connected = graph_a.connected_components().__getitem__(0)
        self.assertEqual(4,len(connected))

        graph = self.build_empty_graph()
        GraphAlgo.__init__(graph_a, graph)
        self.assertEqual(0, len(graph_a.connected_components()))








