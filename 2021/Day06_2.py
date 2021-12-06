if __name__ == "__main__":
    lanternfish = [0,0,0,0,0,0,0,0,0,0]
    # Read points.
    with open('2021\Day06_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        days = 256
        for line in data:
            # Clean the input
            line = line.split(',')
            #print(line)
            for x in line:
                lanternfish[int(x)] += 1
    
    #print(f'Initial state: {lanternfish}')

    for x in range(1, days + 1, 1):
        for fish in enumerate(lanternfish):
            # Zero day fish reset and make more
            if fish[0] == 0:
                if fish[1] > 0:
                    lanternfish[7] += fish[1]
                    lanternfish[9] += fish[1]
                    lanternfish[0] = 0
            else:
                lanternfish[fish[0] - 1] += fish[1]
                lanternfish[fish[0]] = 0
        #print(f'After {x} days: {lanternfish}')
    print(f'After {days} days, there are a total of {sum(lanternfish)} fish.')
        