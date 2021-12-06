if __name__ == "__main__":
    lanternfish = []
    # Read points.
    with open('2021\Day06_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        days = 18
        for line in data:
            # Clean the input
            line = line.split(',')
            #print(line)
            for x in line:
                lanternfish.append(int(x))
    
    #print(f'Initial state: {lanternfish}')

    for x in range(1, days + 1, 1):
        for fish in enumerate(lanternfish):
            if lanternfish[fish[0]] == 0:
                lanternfish[fish[0]] = 6
                lanternfish.append(9)
            else:
                lanternfish[fish[0]] -= 1
        #print(f'After {x} days: {lanternfish}')
    print(f'After {days} days, there are a total of {len(lanternfish)} fish.')
        