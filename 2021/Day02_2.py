import itertools

with open('2021\Day02_input.txt') as f:
    input = []
    for line in f:
        input.append(line.rstrip('\n'))


def calc_pos(input):
    hor = 0
    ver = 0
    aim = 0
    for cmd in input:
        cmd = str.split(cmd)
        if cmd[0] == 'forward':
            hor += int(cmd[1])
            if aim !=0:
                ver += int(cmd[1]) * aim
        if cmd[0] == 'down':
            aim += int(cmd[1])
        if cmd[0] == 'up':
            aim -= int(cmd[1])
    return(hor * ver)

pos = calc_pos(input)
        
print(f'Position is {pos}')