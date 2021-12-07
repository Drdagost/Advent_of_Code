import statistics

if __name__ == "__main__":
    
    # Read points.
    with open('2021\Day07_input.txt') as f:
        data = [x.rstrip() for x in f.readlines()]
        for line in data:
            # Clean the input
            line = line.split(',')
            integer_map = map(int, line)
            crab_list = list(integer_map)
            #print(crab_list)

    median = statistics.median(crab_list)

    print(f'Median of crab distance: {median}')
    total_fuel = 0
    fuel = 0
    for crab in crab_list:
        fuel = abs(crab - median)
        total_fuel += fuel
        #print(f'Move from {crab} to {median}: {fuel} fuel')
    print(f'Total fuel cost: {total_fuel}')