import unittest
from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def build_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1.5)
        graph.add_node(2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 1.1)
        graph.add_node(3)
        graph.add_edge(2, 3, 1.5)
        graph.add_node(4)
        graph.add_edge(3, 4, 2.5)
        graph.add_edge(0, 4, 0.5)
        graph.add_edge(4, 0, 0.5)
        return graph

    def test_v_size(self):
        graph = TestDiGraph.build_graph(self)
        number_nodes = graph.v_size()
        self.assertEqual(5, number_nodes)
        graph.add_node(5)
        self.assertEqual(6, graph.v_size())
        graph.remove_node(5)
        self.assertEqual(5, graph.v_size())

    def test_e_size(self):
        graph = TestDiGraph.build_graph(self)
        number_edges = graph.e_size()
        self.assertEqual(7, number_edges)
        graph.add_edge(3, 0, 7)
        self.assertEqual(8, graph.e_size())
        graph.remove_edge(1, 0)
        self.assertEqual(8, graph.e_size())
        graph.remove_edge(0, 1)
        self.assertEqual(7, graph.e_size())

    def test_get_all_v(self):
        graph = TestDiGraph.build_graph(self)
        nodes = graph.get_all_v()
        number_nodes = graph.v_size()
        for i in range(number_nodes):
            self.assertIn(i,  nodes)
        self.assertEqual(5, nodes.__len__())
        graph.add_node(5)
        self.assertTrue(5 in nodes)
        graph.remove_node(5)
        self.assertFalse(5 in nodes)

    def test_all_in_edges_of_node(self):
        graph = TestDiGraph.build_graph(self)
        self.assertIsNotNone(graph.all_in_edges_of_node(0))
        self.assertIn(4, graph.all_in_edges_of_node(0))
        graph.remove_edge(4, 0)
        self.assertEqual({}, graph.all_in_edges_of_node(0))
        self.assertIsNotNone(graph.all_in_edges_of_node(1))
        self.assertIn(0, graph.all_in_edges_of_node(1))
        self.assertIn(2, graph.all_in_edges_of_node(1))
        self.assertEqual({}, graph.all_in_edges_of_node(10))

    def test_get_mc(self):
        graph = TestDiGraph.build_graph(self)
        mode_counter = graph.get_mc()
        self.assertEqual(12, mode_counter)
        graph.add_node(5)
        mode_counter = graph.get_mc()
        self.assertEqual(13, mode_counter)
        graph.remove_node(5)
        mode_counter = graph.get_mc()
        self.assertEqual(14, mode_counter)
        graph.remove_edge(0, 4)
        new_mode_counter = graph.get_mc()
        self.assertNotEqual(mode_counter, new_mode_counter)

    def test_all_out_edges_of_node(self):
        graph = TestDiGraph.build_graph(self)
        self.assertIsNotNone(graph.all_out_edges_of_node(0))
        self.assertIn(1, graph.all_out_edges_of_node(0))
        self.assertIn(4, graph.all_out_edges_of_node(0))
        self.assertNotIn(3, graph.all_out_edges_of_node(0))
        self.assertIsNotNone(graph.all_out_edges_of_node(1))
        self.assertIn(2, graph.all_out_edges_of_node(1))
        graph.remove_edge(1, 2)
        self.assertNotIn(1, graph.all_out_edges_of_node(1))
        self.assertEqual({}, graph.all_out_edges_of_node(1))
        self.assertEqual({}, graph.all_in_edges_of_node(10))

    def test_add_edge(self):
        graph = TestDiGraph.build_graph(self)
        edges1 = graph.e_size()
        graph.add_edge(4, 3, 1)
        edges2 = graph.e_size()
        self.assertEqual(edges2, edges1 + 1, "edges1 + 1 should equals edges2")
        weight = graph.all_out_edges_of_node(4).get(3)
        self.assertEqual(1, weight, "weight should be 1")

    def test_add_node(self):
        graph = TestDiGraph.build_graph(self)
        graph.add_node(10)
        dict1 = graph.get_all_v()
        self.assertIn(10, dict1)
        graph.add_node(15)
        self.assertIn(15, dict1)
        self.assertNotIn(11, dict1)

    def test_remove_node(self):
        graph = TestDiGraph.build_graph(self)
        graph.remove_node(3)
        self.assertEqual(5, graph.e_size())
        self.assertEqual(4, graph.v_size())
        self.assertNotIn(3, graph.get_all_v())
        self.assertIn(2, graph.get_all_v())
        graph.remove_node(2)
        self.assertEqual(3, graph.e_size())
        self.assertEqual(3, graph.v_size())
        self.assertNotIn(2, graph.get_all_v())

    def test_remove_edge(self):
        graph = TestDiGraph.build_graph(self)
        graph.remove_edge(3, 4)
        self.assertEqual(6, graph.e_size())
        self.assertEqual(0, len(graph.all_out_edges_of_node(3)))
        self.assertEqual(2, len(graph.all_out_edges_of_node(0)))
        graph.remove_edge(0, 4)
        self.assertEqual(1, len(graph.all_out_edges_of_node(0)))
        self.assertEqual(1, len(graph.all_in_edges_of_node(0)))


if __name__ == '__main__':
    unittest.main()
