total = 0
with open('Day02_input.txt') as f:
    for line in f:
        line = line.replace('-', ' ')
        line = line.replace(':', '')
        line = line.split()
        print(line)
        min = int(line[0])
        max = int(line[1])
        policy = line[2]
        password = line[3]

        count = (password.count(policy))
        if min <= count <= max:
            print(password + " is valid")
            total += 1
    print(total)