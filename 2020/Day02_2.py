total = 0
with open('Day02_input.txt') as f:
    for line in f:
        line = line.replace('-', ' ')
        line = line.replace(':', '')
        line = line.split()
        print(line)
        firstPos = int(line[0]) - 1
        secondPos = int(line[1]) - 1
        policy = line[2]
        password = line[3]

        if password[firstPos] == policy:
            if password[secondPos] != policy:
                print(password + " is valid")
                total += 1
        elif password[secondPos] == policy:
            print(password + " is valid")
            total += 1
    print(total)