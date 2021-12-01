import itertools

with open('2021\Day01_input.txt') as f:
    integer_list = []
    for line in f:
        integer_list.append(int(line.rstrip('\n')))

total = 0
for idx in range(1, len(integer_list)):
    if integer_list[idx - 1] < integer_list[idx]:
        print(f'{integer_list[idx]} increased')
        total += 1
    else:
        print(f'{integer_list[idx]} decreased')


print(f'Total increased {total}')