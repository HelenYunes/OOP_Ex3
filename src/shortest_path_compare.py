import networkx as nx
import json
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time


def from_json(filename):
    G = nx.DiGraph()
    with open(filename) as f:
        data = json.load(f)

    for node in data['Nodes']:
        G.add_node(node['id'], pos=(node['pos']))

    for edge in data['Edges']:
        G.add_edge(edge['src'], edge['dest'], weight=edge['w'])
    return G


# nx.draw(G, with_labels=1)
# plt.show()

g = DiGraph()
g_a = GraphAlgo()
g_a.__init__(g)

file_name = '../data/G_10000_80000_1.json'
g_a.load_from_json(file_name)

print("this is the 10000_80000 graph shortest path comparison")

start_time = time.time()
c = nx.dijkstra_path(from_json(file_name), 226, 2797)
print("--- %s seconds --- Networkx" % (time.time() - start_time))
print(c)

start_time = time.time()
c = g_a.shortest_path(226, 2797)
print("--- %s seconds ---" % (time.time() - start_time))
print(c)
print('\n\n')

print("this is the 100_800 graph shortest path comparison")
file_name = '../data/G_100_800_1.json'
start_time = time.time()
c = nx.dijkstra_path(from_json(file_name), 7, 1)
print("--- %s seconds --- Networkx" % (time.time() - start_time))
print(c)

g_a.load_from_json(file_name)
start_time = time.time()
c = g_a.shortest_path(7, 1)
print("--- %s seconds --- " % (time.time() - start_time))
print(c)
print('\n\n')

print("this is the 1000_8000 graph shortest path comparison")
file_name = '../data/G_1000_8000_1.json'
start_time = time.time()
c = nx.dijkstra_path(from_json(file_name), 844, 416)
print("--- %s seconds --- Networkx" % (time.time() - start_time))
print(c)

g_a.load_from_json(file_name)
start_time = time.time()
c = g_a.shortest_path(844, 416)
print("--- %s seconds ---" % (time.time() - start_time))
print(c)
print('\n\n')
