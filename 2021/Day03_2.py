import itertools
from typing import List

with open('2021\Day03_input.txt') as f:
    data = [x.rstrip() for x in f.readlines()]

o2_rate = ''
co2_rate = ''
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

def filter_o2_result(data: list) -> str:
    result = data.copy()
    for x in range(0, len(data[0])):
        data = result.copy()
        filter_data = most_common(calc_row_totals(data), (len(data) / 2))
        for row in data:
            if row[x] != filter_data[x]:
                if len(result) == 1:
                    return result[0]
                if len(result) == 2:
                    if data[0][x] != data[1][x]:
                        if data[0][x] == '1':
                            return data[0]
                        else:
                            return data[1]
                result.remove(row)
    return result[0]

def filter_co2_result(data: list) -> str:
    result = data.copy()
    for x in range(0, len(data[0])):
        data = result.copy()
        filter_data = least_common(calc_row_totals(data), (len(data) / 2))
        for row in data:
            if row[x] != filter_data[x]:
                if len(result) == 1:
                    return result[0]
                if len(result) == 2:
                    if data[0][x] != data[1][x]:
                        if data[0][x] == '0':
                            return data[0]
                        else:
                            return data[1]
                result.remove(row)
    return result[0]    
            
o2_rate = filter_o2_result(data)
co2_rate = filter_co2_result(data)

print(f'O2 rate: {o2_rate}')
print(f'CO2 rate: {co2_rate}')
print(f'Life support rating: {int(o2_rate, 2) * int(co2_rate, 2)}')
