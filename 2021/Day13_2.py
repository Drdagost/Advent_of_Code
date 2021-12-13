class Transparency:
    def __init__(self):
        # x, increases to the right (col)
        # y, increases downward (row)
        # points{x, y}
        self.points = {}
        self.folds = []

    def add_point(self, point: list) -> None:
        key = (int(point[0]), int(point[1]))
        if key in self.points:
            self.points[key] += 1
        else:
            self.points[key] = 1
    
    def add_fold(self, fold_axis: str, digit: int) -> None:
        self.folds.append((fold_axis, digit))

    # Fold along y
    def fold_up(self, digit: int) -> None:
        for point in self.points.copy():
            if point[1] > digit:
                new_point = [point[0], (2 * digit) - point[1]]
                self.add_point(new_point)
                self.points.pop(point)

    # Fold along x
    def fold_left(self, digit: int) -> None:
        for point in self.points.copy():
            if point[0] > digit:
                new_point = [(2 * digit) - point[0], point[1]]
                self.add_point(new_point)
                self.points.pop(point)


if __name__ == "__main__":
    t = Transparency()

    # Read points.
    with open('2021\Day13_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            if 'fold along' in line:
                line = line.split()
                line = line[2]
                line = line.split('=')
                t.add_fold(line[0], int(line[1]))
            elif line != '':
                line = line.split(',')
                t.add_point(line)

    fold = t.folds[0]
    if fold[0] == 'y':
        t.fold_up(fold[1])
    if fold[0] == 'x':
        t.fold_left(fold[1])

    print(f'Visible dots: {len(t.points)}')
