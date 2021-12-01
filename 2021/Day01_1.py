import itertools

with open('2021\Day01_input.txt') as f:
    integer_array = []
    for line in f:
        integer_array.append(int(line.rstrip('\n')))

total = 0
for idx in range(1, len(integer_array)):
    if integer_array[idx - 1] < integer_array[idx]:
        print(f'{integer_array[idx]} increased')
        total += 1
    else:
        print(f'{integer_array[idx]} decreased')


print(f'Total increased {total}')