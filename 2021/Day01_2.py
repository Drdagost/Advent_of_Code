import itertools

with open('2021\Day01_input.txt') as f:
    integer_array = []
    for line in f:
        integer_array.append(int(line.rstrip('\n')))

window_size = 3
i = 0
window_sum = []
while i < len(integer_array) - window_size + 1:
    this_window = integer_array[i : i + window_size]
    window_sum.append(sum(this_window))
    i += 1

total = 0
for idx in range(1, len(window_sum)):
    if window_sum[idx - 1] < window_sum[idx]:
        print(f'{window_sum[idx]} increased')
        total += 1
    else:
        print(f'{window_sum[idx]} decreased')


print(f'Total increased {total}')

