import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name):
        self.vertices[name] = []
    
    def add_edge(self, src, dest, weight):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[src].append((dest, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
            
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    

g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 10)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'D', 2)
g.add_edge('C', 'E', 1)
g.add_edge('D', 'E', 4)

shortest_path = g.dijkstra('A')

print("Найкоротші шляхи від вершини А:")
for vertex, distance in shortest_path.items():
    print(f"До {vertex}: {distance}")

