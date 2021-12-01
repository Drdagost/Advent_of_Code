with open('Day03_input.txt') as f:
    array2d = []
    input = f.readlines()

    puzzle_input = [line.strip() for line in input]

    for line in puzzle_input:
        array2d.append([char for char in line])
    
def countTrees(move_in_row, move_in_column):
        
    r = 0
    c = 0
    r_move = move_in_row
    c_move = move_in_column
    tree = 0
    
    while r < len(array2d):
        # map pattern repeats
        if c >= len(array2d[r]) :
            c -= len(array2d[r])
        
        #print(array2d[r][c])
        if array2d[r][c] == '#':
            #print("Tree")
            tree += 1
        else:
            #print("Clear")
            pass
        r += r_move
        c += c_move
    return tree

totalTrees = 1
run1 = countTrees(1,1)
totalTrees *= run1
print("Total trees hit Right 1, down 1 ", run1 )
run2 = countTrees(1,3)
totalTrees *= run2
print("Total trees hit Right 3, down 1 ", run2 )
run3 = countTrees(1,5)
totalTrees *= run3
print("Total trees hit Right 5, down 1 ", run3 )
run4 = countTrees(1,7)
totalTrees *= run4
print("Total trees hit Right 7, down 1 ", run4 )
run5 = countTrees(2,1)
totalTrees *= run5
print("Total trees hit Right 1, down 2 ", run5 )
print("Product of all runs ", totalTrees)