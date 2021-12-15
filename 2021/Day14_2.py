from collections import defaultdict

class Polymerization:
    def __init__(self):

        self.pairs = {}
        self.polymer_template = []
        self.current_pairs = defaultdict(int)
        self.char_freq = defaultdict(int)        

    
    def add_pair(self, point: list) -> None:
        self.pairs[point[0]] = point[1]

    def initial_pairs(self):
        for c in range(0, len(self.polymer_template) - 1):
            pair = self.polymer_template[c] + self.polymer_template[c + 1]
            self.current_pairs[pair] += 1

    def make_new_pairs(self):
        new_pairs = defaultdict(int)
        for pair in self.current_pairs:
            new_polymer = self.pairs[pair]
        
            new_pair_1 = pair[0] + new_polymer
            new_pair_2 = new_polymer + pair[1]
        
            new_pairs[new_pair_1] += self.current_pairs[pair]
            new_pairs[new_pair_2] += self.current_pairs[pair]
        
            self.char_freq[new_polymer] += self.current_pairs[pair]
        self.current_pairs = new_pairs


    def freq(self):
        for c in self.polymer_template:
            self.char_freq[c] += 1

if __name__ == "__main__":
    p = Polymerization()
    steps = 40
    max_freq = 0
    min_freq = 0

    # Read points.
    with open('2021\Day14_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            if line != '' and '->' not in line:
                for c in line:
                    p.polymer_template.append(c)
            elif line != '':
                line = line.split(' -> ')
                p.add_pair(line)

    p.freq()
    p.initial_pairs()
    for c in range(steps):
        p.make_new_pairs()
    print(p.current_pairs)

    max_freq = max(p.char_freq.values())
    min_freq = min(p.char_freq.values())
    print(f'The max frequency is: {max_freq}')
    print(f'The min frequency is: {min_freq}')
    print(f'Most common - Least common: {max_freq - min_freq}')
    

    
   
