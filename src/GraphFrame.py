import matplotlib.pyplot as plot_graph
from src.DiGraph import DiGraph
import random


class GraphFrame:
    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.list_random_location_nodes = []
        self.set_random_nodes()

    def set_random_nodes(self):
        eps = 0.0002
        for node in self.graph.get_all_v().values():
            if node.get_location() is None:
                self.list_random_location_nodes.append(node)
        if self.list_random_location_nodes.__len__() == 0:
            return
        for node in self.list_random_location_nodes:
            if node.get_location() is None:
                node.set_location(random.uniform(0, 7), random.uniform(0, 7), 0)

    def draw_nodes(self, ax):
        for node in self.graph.Nodes.values():
            ax.scatter(node.get_location()[0], node.get_location()[1], color="blue", s=50, label=node.__repr__())

    def draw_edges(self, ax):
        for node in self.graph.Nodes.values():
            for edge in self.graph.all_out_edges_of_node(node.get_key()).keys():
                destination = self.graph.get_node(edge)
                ax.arrow(node.get_location()[0], node.get_location()[1],
                         destination.get_location()[0] - node.get_location()[0],
                         destination.get_location()[1] - node.get_location()[1], label='Edges',
                         length_includes_head=True, head_width=0.025, head_length=0.18)

    def draw_graph(self):

        plot_graph.figure(figsize=(13, 7), facecolor="#5a7d9a")
        ax = plot_graph.axes()
        plot_graph.title("Here is a graphic presentation of the graph:", color="w")
        plot_graph.xlabel("x")
        plot_graph.ylabel("y")
        self.draw_edges(ax)
        self.draw_nodes(ax)
        plot_graph.tight_layout()
        plot_graph.show()
