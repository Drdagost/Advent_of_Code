import itertools
from typing import List

with open('2021\Day03_input.txt') as f:
    data = [x.rstrip() for x in f.readlines()]

gamma_rate = ''
epsilon_rate = ''
row_totals = []

def calc_row_totals(data: list) -> list:
    pos = [0 for x in data[0]]
    for line in data:
        for x in range(0, len(line)):
            pos[x] += int(line[x])
    return pos

def most_common(data: list, threshold: int) -> str:
    result = ''
    for x in range(0, len(data)):
        if data[x] >= threshold:
            result += '1'
        else:
            result += '0'
    return result

def least_common(data: list, threshold: int) -> str:
    result = ''
    for x in range(0, len(data)):
        if data[x] >= threshold:
            result += '0'
        else:
            result += '1'
    return result

row_totals = calc_row_totals(data)
gamma_rate = most_common(row_totals, (len(data) / 2))
epsilon_rate = least_common(row_totals, (len(data) / 2))

print(f'Column totals: {row_totals}')
print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {epsilon_rate}')
print(f'Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')