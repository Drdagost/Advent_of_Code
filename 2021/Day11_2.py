class Octopus:
    def __init__(self):
        # Dictionary with a key = x,y coordinates and a num = energy level
        # {[x,y]:"num"}
        self.positions = {}
        self.flash = []
        self.max_x = 0
        self.max_y = 0
        

    def add_point(self, x: int, y: int, value: int) -> None:
        key = x, y
        self.positions[key] = value

    def increase_energy_lvl(self, key: list) -> None:
        self.positions[key] += 1

    def energy_cycle(self) -> None:
        self.flash = []
        for pos in self.positions:
            self.increase_energy_lvl(pos)
            self.check_for_flash(pos)

        for pos in self.positions:
            if self.positions[pos] > 9:
                self.positions[pos] = 0
        
    def check_for_flash(self, key: list) -> None:
        if self.positions[key] > 9 and key not in self.flash:
            self.flash.append(key)
            self.increment_adjacent(key)

    def increment_adjacent(self, key: list) -> None:
        for pos in self.set_burst(key):
            self.increase_energy_lvl(pos)
            self.check_for_flash(pos)

    def print_board(self) -> None:
        result = []
        for pos in self.positions:
            result.append(self.positions[pos])    
            if pos[1] == self.max_y:
                print(result)
                result = []
        print()

    def all_flash(self) -> bool:
        if len(self.positions) == len(self.flash):
            return(True)
        else:
            return(False)
  
    def set_burst(self, key: list) -> list:
        x = key[0]
        y = key[1]
        burst = []
        # Top row
        if x == 0:
            # Left side
            if y == 0:
                burst.append((x, y + 1))
                burst.append((x + 1, y))
                burst.append((x + 1, y + 1))
            # Right side
            elif y == self.max_y:
                burst.append((x, y - 1))
                burst.append((x + 1, y - 1))
                burst.append((x + 1, y))
            # Middle
            else:
                burst.append((x, y - 1))
                burst.append((x, y + 1))
                burst.append((x + 1, y - 1))
                burst.append((x + 1, y))
                burst.append((x + 1, y + 1))
        # Bottom row
        elif x == self.max_x:
            # Left side
            if y == 0:
                burst.append((x - 1, y))
                burst.append((x - 1, y + 1))
                burst.append((x, y + 1))
            # Right side
            elif y == self.max_y:
                burst.append((x - 1, y - 1))
                burst.append((x - 1, y))
                burst.append((x, y - 1))
            # Middle
            else:
                burst.append((x - 1, y - 1))
                burst.append((x - 1, y))
                burst.append((x - 1, y + 1))
                burst.append((x, y - 1))
                burst.append((x, y + 1))
        # Middle row
        else:
            # Left side
            if y == 0:
                burst.append((x + 1, y))
                burst.append((x + 1, y + 1))
                burst.append((x, y + 1))
                burst.append((x - 1, y))
                burst.append((x - 1, y + 1))
            # Right side
            elif y == self.max_y:
                burst.append((x + 1, y - 1))
                burst.append((x + 1, y))
                burst.append((x, y - 1))
                burst.append((x - 1, y - 1))
                burst.append((x - 1, y))
            # Middle
            else:
                burst.append((x - 1, y - 1))
                burst.append((x - 1, y))
                burst.append((x - 1, y + 1))
                burst.append((x, y - 1))
                burst.append((x, y + 1))
                burst.append((x + 1, y - 1))
                burst.append((x + 1, y))
                burst.append((x + 1, y + 1))
        return(burst)

    def count_flashes(self) -> int:
        return len(self.flash)

    
if __name__ == "__main__":
    octopus = Octopus()
    cycles = 0

    # Read points.
    with open('2021\Day11_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        octopus.max_y = len(data[0]) - 1
        octopus.max_x = len(data) - 1
        for row in enumerate(data):
            for col in enumerate(row[1]):
                # Add points and values
                octopus.add_point(row[0], col[0], int(col[1]))
    print('Before any steps:')
    octopus.print_board()
    
    while octopus.all_flash() == False:
        octopus.energy_cycle()
        #print(f'After step {i + 1}:')
        #print(octopus.print_board())
        cycles += 1
    print(f'First time all flash: {cycles}')