import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#1296F0"):  # ініціалізуємо колір, що буде оновлятись 
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def generate_color_spectrum(n):
    # будуємо спектр кольорів від світлого до темного
    spectrum = []
    for i in range(n):
        intensity = 255 - int((i / n) * 155) 
        color = "#{:02X}{:02X}F0".format(intensity, intensity)  # відтінки блакитного
        spectrum.append(color)
    return spectrum

def update_node_colors(nodes, spectrum):
   # Оновлюєм кольори вузлів на основі їх порядку в обході
    for node, color in zip(nodes, spectrum):
        node.color = color

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def dfs(node, visited=None, color_update=False):
    if visited is None:
        visited = []
    if node:
        visited.append(node)
        if node.left:
            dfs(node.left, visited, color_update)
        if node.right:
            dfs(node.right, visited, color_update)
    if color_update:
        color_spectrum = generate_color_spectrum(len(visited))
        update_node_colors(visited, color_spectrum)
    return [node.val for node in visited]

def bfs(root, color_update=False):
    if root is None:
        return []
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    if color_update:
        color_spectrum = generate_color_spectrum(len(visited))
        update_node_colors(visited, color_spectrum)
    return [node.val for node in visited]

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

root = Node(0)  
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_result = dfs(root, color_update=True)  # відображення обходу через дфс
print("DFS обхід:", dfs_result)

bfs_result = bfs(root, color_update=True)  
print("BFS обхід:", bfs_result)

# відображення дерева з кольорами
draw_tree(root)
