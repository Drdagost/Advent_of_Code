import itertools

with open('2021\Day03_input.txt') as f:
    input = []
    for line in f:
        input.append(line.rstrip('\n'))

gamma_rate = ''
epsilon_rate = ''
pos = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in input:
    for x in range(0, len(line)):
        pos[x] += int(line[x])
print(pos)
print(len(input))

for x in range(0, len(pos)):
    if pos[x] > (len(input) / 2):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(gamma_rate)
print(epsilon_rate)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))


# def calc_pos(input):
#     hor = 0
#     ver = 0
#     for cmd in input:
#         cmd = str.split(cmd)
#         if cmd[0] == 'forward':
#             hor += int(cmd[1])
#         if cmd[0] == 'down':
#             ver += int(cmd[1])
#         if cmd[0] == 'up':
#             ver -= int(cmd[1])
#     return(hor * ver)

# pos = calc_pos(input)
        
# print(f'Position is {pos}')