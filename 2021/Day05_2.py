class Intersection:
    def __init__(self):
        # Dictionary with a key = x,y coordinates and a num = number of overlaps
        # {[x,y]:"num"}
        self.positions = {}
        
    def line(self, x0: int, y0: int, x1: int, y1: int):
        self.deltax = x1-x0
        try:
            self.dxsign = int(abs(self.deltax)/self.deltax)
        except ZeroDivisionError as e:
            self.dxsign = 1
        self.deltay = y1-y0
        try:
            self.dysign = int(abs(self.deltay)/self.deltay)
        except ZeroDivisionError as e:
            self.dysign = 1
        
        # Vertical line
        if y0 == y1:
            self.y = y0
            for x in range(x0, x1, self.dxsign):
                yield x, self.y
            yield x1, y1
        # Horizontal line
        elif x0 == x1:
            self.x = x0
            for y in range(y0, y1, self.dysign):
                yield self.x, y
            yield x1, y1
        # Diagonal line
        elif x0 != x1 and y0 != y1:
            y = y0
            for x in range(x0, x1, self.dxsign):
                y = y0
                y0 += self.dysign
                yield x, y
            yield x1, y1

    def add_point(self, x: int, y: int):
        self.key = x, y
        if self.key not in self.positions:
            self.positions[self.key] = 1
        else:
            self.positions[self.key] += 1
        
    def multiple_points(self):
        result = {}
        for key, value in self.positions.items():
            if value > 1:
                result[key] = value
        return(result)

    def find_points(self, x0: int, y0: int, x1: int, y1: int):
        self.points = self.line(x0, y0, x1, y1)
        for point in self.points:
            #print(point)
            self.add_point(point[0], point[1])
        
if __name__ == "__main__":
    inter = Intersection()

    # Read points.
    with open('2021\Day05_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            # Clean the input
            line = line.replace(' -> ', ',')
            line = line.split(',')
            #print(line)
            inter.find_points(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
print(f'At least 2 points: {len(inter.multiple_points())}')
            