#Code to Impliment BFS
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        queue = [start] 
        visited = []     
        
        while queue:
            vertex = queue.pop(0) 
            if vertex not in visited:
                print(vertex, end=" ")
                visited.append(vertex)
                
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    
    print("Breadth-First Search starting from vertex 0:")
    g.bfs(0)
