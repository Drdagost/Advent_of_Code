# Check each passport for the following fields 
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)) (temporarily ignore)

required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
total = 0
with open('Day04_input.txt') as f:
    batch = f.read().split("\n\n")
    for passport in batch:
        print(passport)
        if all(x in passport for x in required):
            print("Passport is valid")
            total += 1
        print("***********")
print(total)