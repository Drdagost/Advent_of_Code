from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path_count = 0

    # function to add an edge to graph going both directions
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def check_lowercase_duplicates(self, elements: list) -> bool:    
        for e in elements:
            if e.islower() and elements.count(e) > 1:
                return True
        return False

    def print_all_paths_util(self, u, d, visited, path):
        
        # Mark the current node as visited and store in path
        if u == 'start' or u == 'end':
            path.append(u)
            visited[u] = True
        # Lowercase
        elif u.islower():
            if u not in path:
                path.append(u)
                if self.check_lowercase_duplicates(path):
                    visited[u] = True
            else:
                if self.check_lowercase_duplicates(path):
                    visited[u] = True
                else:
                    path.append(u)
                    visited[u] = True
        # Uppercase
        else:
            path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            self.path_count += 1
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    if i.islower():
                        if self.check_lowercase_duplicates(path):
                            if i not in path:
                                self.print_all_paths_util(i, d, visited, path)
                        else:
                            self.print_all_paths_util(i, d, visited, path)
                    else:
                        self.print_all_paths_util(i, d, visited, path)                        
                    
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


    # Prints all paths from 's' to 'd'
    def print_all_paths(self, s, d):
        visited = {}
        # Mark all the vertices as not visited
        for x in self.graph:
            visited[x] = False

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.print_all_paths_util(s, d, visited, path)


if __name__ == "__main__":
    g = Graph()

    # Read points.
    with open('2021\Day12_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            line = line.split('-')
            g.add_edge(line[0], line[1])


s = 'start' ; d = 'end'
print (f'Following are all different paths from {s} to {d} :')
g.print_all_paths(s, d)
print(f'Path count: {g.path_count}')
        