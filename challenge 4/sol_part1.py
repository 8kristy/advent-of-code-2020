with open("input", "r") as f:
    passports = f.read().split("\n\n")

valid = 0    
required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
for passport in passports:
    if all(x in passport for x in required_fields):
        valid += 1

print(valid)        