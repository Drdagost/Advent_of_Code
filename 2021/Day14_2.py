class Polymerization:
    def __init__(self):

        self.pairs = {}
        self.polymer_template = []
        self.current_template = []
        self.char_freq = {}        

    def add_pair(self, point: list) -> None:
        self.pairs[point[0]] = point[1]

    def insert_polymer(self, polymer: str, index: int) -> None:
        self.current_template.insert(index, polymer)

    def insert_polymers(self) -> None:
        self.current_template = self.polymer_template.copy()
        polymers_added = 0
        for i in range(len(self.polymer_template) - 1):
            polymer = self.polymer_template[i] + self.polymer_template[i + 1]
            if polymer in self.pairs:
                polymers_added += 1
                self.insert_polymer(self.pairs[polymer], i + polymers_added)
        self.polymer_template = self.current_template

    def freq(self):
        for i in self.polymer_template:
            if i in self.char_freq:
                self.char_freq[i] += 1
            else:
                self.char_freq[i] = 1

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

    for c in range(steps):
        p.insert_polymers()
    print(p.polymer_template)
    p.freq()
    max_freq = p.char_freq[max(p.char_freq, key = p.char_freq.get)]
    min_freq = p.char_freq[min(p.char_freq, key = p.char_freq.get)]
    print(f'The max frequency is: {max_freq}')
    print(f'The min frequency is: {min_freq}')
    print(f'Most common - Least common: {max_freq - min_freq}')
    

    
   
