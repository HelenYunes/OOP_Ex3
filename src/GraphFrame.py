import matplotlib.pyplot as plot_graph
from src.DiGraph import DiGraph
import random


class GraphFrame:
    def __init__(self, graph: DiGraph):
        self.graph = graph

    def set_random_nodes(self):
        list_random_location_nodes = []
        for node in self.graph.get_all_v().values():
            if node.get_location() is None:
                list_random_location_nodes.append(node)
        if list_random_location_nodes.__len__() == 0:
            return
        for node in list_random_location_nodes:
            if node.get_location() is None:
                node.set_location(random.uniform(0, 7), random.uniform(0, 7), 0)

    def draw_nodes(self, ax):
        self.set_random_nodes()
        for node in self.graph.Nodes.values():
            ax.scatter(node.get_location()[0], node.get_location()[1], color="blue", label=node.__repr__())

    def draw_edges(self, ax):
        eps = 0.0001
        for node in self.graph.Nodes.values():
            for edge in self.graph.all_out_edges_of_node(node.get_key()).keys():
                ax.arrow(node.get_location()[0], node.get_location()[1],
                         self.graph.get_node(edge).get_location()[0] - node.get_location()[0],
                         self.graph.get_node(edge).get_location()[1] - node.get_location()[1], label='Edges',
                         length_includes_head=True, width=0.00000389, head_width=0.000089999, head_length=0.000299974)

    def draw_graph(self):

        plot_graph.figure(figsize=(13, 7), facecolor="#5a7d9a")
        ax = plot_graph.axes()
        plot_graph.title("Here is a graphic presentation of the graph:", color="w")
        plot_graph.xlabel("x")
        plot_graph.ylabel("y")
        self.draw_nodes(ax)
        self.draw_edges(ax)
        plot_graph.tight_layout()
        plot_graph.show()
