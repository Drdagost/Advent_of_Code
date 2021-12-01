import itertools

with open('Day01_input.txt') as f:
    integer_array = []
    for line in f:
        integer_array.append(int(line.rstrip('\n')))

#integer_array = [1721, 979, 366, 299, 675, 1456]

target = 2020
product = 1
for numbers in itertools.combinations(integer_array,3):
    if sum(numbers) == target:
        pair = [integer_array.index(number) for number in numbers]
        
        print("The numbers are " + str(numbers))
        for number in numbers: 
            product *= number
        print("Product = " + str(product))