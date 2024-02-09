import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, nodes, pos, parent_index=0, x=0, y=0, layer=1):
    if parent_index >= len(nodes):
        return graph
    
    node = nodes[parent_index]
    graph.add_node(node.id, label=node.val)
    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2
    
    if left_child_index < len(nodes):
        graph.add_edge(node.id, nodes[left_child_index].id)
        l = x - 1 / 2 ** layer
        pos[nodes[left_child_index].id] = (l, y - 1)
        add_edges(graph, nodes, pos, left_child_index, l, y - 1, layer + 1)
    
    if right_child_index < len(nodes):
        graph.add_edge(node.id, nodes[right_child_index].id)
        r = x + 1 / 2 ** layer
        pos[nodes[right_child_index].id] = (r, y - 1)
        add_edges(graph, nodes, pos, right_child_index, r, y - 1, layer + 1)

    return graph

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {}
    nodes = [Node(val) for val in heap]
    
    if nodes:
        pos[nodes[0].id] = (0, 0)
        add_edges(tree, nodes, pos)
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color="skyblue", arrows=False)
    plt.show()

# Створення бінарної купи
heap = [0, 4, 5, 10, 1, 3]
heapq.heapify(heap)

# Відображення бінарної купи
draw_heap(heap)
