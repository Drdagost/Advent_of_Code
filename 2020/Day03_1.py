with open('Day03_input.txt') as f:
    array2d = []
    r = 0
    c = 0
    r_move = 1
    c_move = 3
    tree = 0
    input = f.readlines()

    puzzle_input = [line.strip() for line in input]

    for line in puzzle_input:
        array2d.append([char for char in line])
    
    while r < len(array2d):
        # map pattern repeats
        if c >= len(array2d[r]) :
            c -= len(array2d[r])
        
        #print(array2d[r][c])
        if array2d[r][c] == '#':
            print("Tree")
            tree += 1
        else:
            print("Clear")
        r += r_move
        c += c_move
print("Total trees hit ", tree )