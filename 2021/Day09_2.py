class Smoke:
    def __init__(self):
        # Dictionary with a key = x,y coordinates and a num = number of overlaps
        # {[x,y]:"num"}
        self.positions = {}
        self.low_points = {}
        self.max_x = 0
        self.max_y = 0
        self.candidates = {}
        self.basin = {}
        
    def add_point(self, x: int, y: int, value: int) -> None:
        key = x, y
        self.positions[key] = value

    def add_candidate(self, x: int, y: int) -> None:
        key = x, y
        self.candidates[key] = self.positions[key]

    def add_low_point(self, x: int, y: int) -> None:
        key = x, y
        self.low_points[key] = self.candidates[key]

    def find_basin(self,x: int, y: int, visited: dict):
        key = x, y
        if key not in self.basin and self.positions[key] < 9:
            # Add to the basin
            self.basin[key] = 1
            # Top row
            if x == 0:
                # Check the begining
                if y == 0:
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x + 1, y, self.basin)
                # Check the end
                elif y == self.max_y:
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x + 1, y, self.basin)
                # Check the rest
                else:
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x + 1, y, self.basin)
            # Bottom row
            elif x == self.max_x:
                # Check the begining
                if y == 0:
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
                # Check the end
                elif y == self.max_y:
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
                # Check the rest
                else:
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
            # Middle
            else:
                # Check the begining
                if y == 0:
                    self.find_basin(x + 1, y, self.basin)
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
                # Check the end
                elif y == self.max_y:
                    self.find_basin(x + 1, y, self.basin)
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
                # Check the rest
                else:
                    self.find_basin(x, y - 1, self.basin)
                    self.find_basin(x, y + 1, self.basin)
                    self.find_basin(x - 1, y, self.basin)
                    self.find_basin(x + 1, y, self.basin)

    def check_possible_candidate(self) -> None:
        for position in self.positions:
            x = position[0]
            y = position[1]
            # Check the begining of the row
            if y == 0:
                if self.positions[x, y] >= self.positions[x, y + 1]:
                    # Positions is not a candidate
                    pass
                else:
                    self.add_candidate(x, y)
            # Check the end of the row
            elif y == self.max_y:
                if self.positions[x, y] >= self.positions[x, y - 1]:
                    # Positions is not a candidate
                    pass
                else:
                    self.add_candidate(x, y)
            else:
                if self.positions[x, y] >= self.positions[x, y + 1] or self.positions[x, y] >= self.positions[x, y - 1]:
                    # Positions is not a candidate
                    pass
                else:
                    self.add_candidate(x, y)
        self.set_low_points()

    def set_low_points(self) -> None:
        for position in self.candidates:
            x = position[0]
            y = position[1]
            # Top row
            if x == 0:
                # Left side
                if y == 0:
                    if self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x + 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Right side
                elif y == self.max_y:
                    if self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x + 1, y - 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Middle
                else:
                    if self.candidates[x, y] >= self.positions[x + 1, y - 1] or self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x + 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
            # Bottom row
            elif x == self.max_x:
                # Left side
                if y == 0:
                    if self.candidates[x, y] >= self.positions[x - 1, y] or self.candidates[x, y] >= self.positions[x - 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Right side
                elif y == self.max_y:
                    if self.candidates[x, y] >= self.positions[x - 1, y] or self.candidates[x, y] >= self.positions[x - 1, y - 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Middle
                else:
                    if self.candidates[x, y] >= self.positions[x - 1, y - 1] or self.candidates[x, y] >= self.positions[x - 1, y] or self.candidates[x, y] >= self.positions[x - 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
            # Middle row
            else:
                # Left side
                if y == 0:
                    if self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x + 1, y + 1] or self.candidates[x, y] >= self.positions[x - 1, y] or self.candidates[x, y] >= self.positions[x - 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Right side
                elif y == self.max_y:
                    if self.candidates[x, y] >= self.positions[x + 1, y - 1] or self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x - 1, y - 1] or self.candidates[x, y] >= self.positions[x - 1, y]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
                # Middle
                else:
                    if self.candidates[x, y] >= self.positions[x + 1, y - 1] or self.candidates[x, y] >= self.positions[x + 1, y] or self.candidates[x, y] >= self.positions[x + 1, y + 1] or self.candidates[x, y] >= self.positions[x - 1, y - 1] or self.candidates[x, y] >= self.positions[x - 1, y] or self.candidates[x, y] >= self.positions[x - 1, y + 1]:
                        # Positions is not a candidate
                        pass
                    else:
                        self.add_low_point(x, y)
        print()

if __name__ == "__main__":
    smoke = Smoke()
    basins = []
    risk_lvl = 1

    # Read points.
    with open('2021\Day09_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        smoke.max_y = len(data[0]) - 1
        smoke.max_x = len(data) - 1
        for row in enumerate(data):
            for col in enumerate(row[1]):
                # Add points and values
                smoke.add_point(row[0], col[0], int(col[1]))
    smoke.check_possible_candidate()
    for point in smoke.low_points:
        print(f'Low points: {point}')
        smoke.find_basin(point[0], point[1], smoke.basin)
        print(f'Basin: {sum(smoke.basin.values())}')
        basins.append(len(smoke.basin))
        smoke.basin = {}
    basins.sort()
    basins = basins[-3:]
    for x in basins:
        risk_lvl *= x

    print(f'Risk level: {risk_lvl}')
    
            