import itertools
import pandas as pd

with open('2021\Day01_input.txt') as f:
    integer_list = []
    for line in f:
        integer_list.append(int(line.rstrip('\n')))

def rolling_sum(int_list, window):
    rolling_sum = pd.Series(int_list).rolling(window).sum()
    return rolling_sum

rolling_sum = rolling_sum(integer_list, 3)

total = 0
for idx in range(1, len(rolling_sum)):
    if rolling_sum[idx - 1] < rolling_sum[idx]:
        print(f'{rolling_sum[idx]} increased')
        total += 1
    else:
        print(f'{rolling_sum[idx]} decreased')


print(f'Total increased {total}')