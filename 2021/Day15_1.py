from collections import defaultdict

class Grid:
    def __init__(self):
        self.grid = defaultdict(list)
        self.max_pos_x = 0
        self.max_pos_y = 0
        self.path_risk_level = 0
        self.max_known_risk_level = 0

    def add_point(self, x: int, y: int, value: int) -> None:
        key = x, y
        self.grid[key] = value

    def print_board(self) -> None:
        result = []
        for pos in self.grid:
            result.append(self.grid[pos])    
            if pos[1] == self.max_pos_y:
                print(result)
                result = []

    def print_all_paths_util(self, u: list, d: list, visited: bool, path: list) -> None:

        # Mark the current node as visited, store in path and update path_risk_level
        visited[u] = True
        path.append(u)
        if u != (0, 0):
            self.path_risk_level += self.grid[u]

        # If current point is same as destination, then print
        # current path[]
        if u == d:
            if self.max_known_risk_level > self.path_risk_level:
                self.max_known_risk_level = self.path_risk_level
            #print(path)
            print(f'Path risk level: {self.path_risk_level}')
        else:
            # If current point is not destination check adjacent points
            valid_moves = {}
            # moving down
            if self.is_move_valid((u[0] + 1, u[1]), visited):
                valid_moves[u[0] + 1, u[1]] = self.grid[u[0] + 1, u[1]]
                #self.print_all_paths_util((u[0] + 1, u[1]), d, visited, path)

            # moving right
            if self.is_move_valid((u[0], u[1] + 1), visited):
                valid_moves[u[0], u[1] + 1] = self.grid[u[0], u[1] + 1]
                #self.print_all_paths_util((u[0], u[1] + 1), d, visited, path)
                
            # moving up
            if self.is_move_valid((u[0] - 1, u[1]), visited):
                valid_moves[u[0] - 1, u[1]] = self.grid[u[0] - 1, u[1]]
                #self.print_all_paths_util((u[0] - 1, u[1]), d, visited, path)
                    
            # moving left
            if self.is_move_valid((u[0], u[1] - 1), visited):
                valid_moves[u[0], u[1] - 1] = self.grid[u[0], u[1] - 1]
                #self.print_all_paths_util((u[0], u[1] - 1), d, visited, path)

            # pick the lowest cost move
            while valid_moves:
                lowest_risk_move = min(valid_moves, key=valid_moves.get)
                self.print_all_paths_util(lowest_risk_move, d, visited, path)
                valid_moves.pop(lowest_risk_move)

        # Remove current point from path[], mark it as unvisited and update path_risk_level
        path.pop()
        visited[u]= False
        self.path_risk_level -= self.grid[u]

    # Prints all paths from 's' to 'd'
    def print_all_paths(self, s: list, d: list) -> None:
        # Sum all points to calculate the max_known_risk_level
        visited = {}
        # Mark all the points as not visited
        for x in self.grid:
            visited[x] = False

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.print_all_paths_util(s, d, visited, path)

    # checking where move is valid or not
    def is_move_valid(self, point: list, visited: bool) -> bool:
        if ((point[0] >= 0 and point[1] >= 0) and (point[0] <= self.max_pos_x and point[1] <= self.max_pos_y) and (visited[point] == False) and ((self.path_risk_level + self.grid[point]) < self.max_known_risk_level)):
            return True
        return False


if __name__ == "__main__":
    g = Grid()

    # Read points.
    with open('2021\Day15_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        g.max_pos_y = len(data[0]) - 1
        g.max_pos_x = len(data) - 1
        for row in enumerate(data):
            for col in enumerate(row[1]):
                # Calculate starting max_known_risk_level
                if row[0] == g.max_pos_x:
                    g.max_known_risk_level += int(col[1])
                if col[0] == 0:
                    g.max_known_risk_level += int(col[1])
                # Add points and values
                g.add_point(row[0], col[0], int(col[1]))

print('Before any steps:')
g.print_board()

s = (0, 0) ; d = (g.max_pos_x, g.max_pos_y)
print (f'Following are all different paths from {s} to {d} :')
g.print_all_paths(s, d)
        