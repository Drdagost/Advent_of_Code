if __name__ == "__main__":
    
    segments = []
    known_digits = []
    # Read points.
    with open('2021\Day08_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            # Clean the input
            line = line.split(' | ')
            segments += line[0].split(' ')
            known_digits += line[1].split(' ')
    
    #print(f'Segments: {segments}')
    #print(f'Known digits: {known_digits}')
    
    length = 0
    one = 0
    four = 0
    seven = 0
    eight = 0
    total = 0
    for known_digit in known_digits:
        length = len(known_digit)
        if length == 2:
            one += 1
        if length == 4:
            four += 1
        if length == 3:
            seven += 1
        if length == 7:
            eight += 1
    
    total = one + four + seven + eight
    print(f'The sum of known digits is {total}')
