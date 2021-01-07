import unittest
from src.DiGraph import DiGraph

class TestDiGraph(unittest.TestCase):

    def build_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0,1,1.5)
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

    def test_add_edge(self):
        graph = TestDiGraph.build_graph(self)
        edges1 = graph.e_size()
        graph.add_edge(4,3,1)
        edges2 = graph.e_size()
        self.assertEqual(edges2,edges1+1,"edges1 + 1 should equals edges2")
        weight = graph.all_out_edges_of_node(4).get(3)
        self.assertEqual(1,weight,"weight should be 1")

    def test_add_node(self):
        graph = TestDiGraph.build_graph(self)
        graph.add_node(10)
        dict = graph.get_all_v()
        self.assertIn(10,dict)
        graph.add_node(15)
        self.assertIn(15, dict)
        self.assertNotIn(11,dict)

    def test_remove_node(self):
        graph = TestDiGraph.build_graph(self)
        graph.remove_node(3)
        self.assertEqual(5,graph.e_size())
        self.assertEqual(4,graph.v_size())
        self.assertNotIn(3,graph.get_all_v())
        self.assertIn(2,graph.get_all_v())
        graph.remove_node(2)
        self.assertEqual(3, graph.e_size())
        self.assertEqual(3, graph.v_size())
        self.assertNotIn(2, graph.get_all_v())

    def test_remove_edge(self):
        graph = TestDiGraph.build_graph(self)
        graph.remove_edge(3,4)
        self.assertEqual(6,graph.e_size())
        self.assertEqual(0, len(graph.all_out_edges_of_node(3)))
        self.assertEqual(2, len(graph.all_out_edges_of_node(0)))
        graph.remove_edge(0,4)
        self.assertEqual(1, len(graph.all_out_edges_of_node(0)))
        self.assertEqual(1, len(graph.all_in_edges_of_node(0)))

if __name__ == '__main__':
    unittest.main()

