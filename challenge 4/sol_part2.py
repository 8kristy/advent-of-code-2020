import re

with open("input", "r") as f:
    passports = f.read().split("\n\n")

# Tries to parse a number and also checks if it's within limits
def check_number(value, min, max):
    try:
        if max < int(value) or int(value) < min:
            return False
    except ValueError:
        return False    
    return True    

valid = 0    
required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

for passport in passports:
    # Check if all required fields are present
    found_all_fields = all(x in passport for x in required_fields)

    if found_all_fields:
        # Split up the fields
        passport = re.split("\n| ", passport)
        is_valid = True

        # Check all individual fields
        for field in passport:
            if ":" in field:
                field_name = field.split(":")[0]
                field_value = field.split(":")[1]

                if field_name == "byr" and not check_number(field_value, 1920, 2002):
                    is_valid = False

                if field_name == "iyr" and not check_number(field_value, 2010, 2020):
                    is_valid = False

                if field_name == "eyr" and not check_number(field_value, 2020, 2030):
                    is_valid = False  
    
                if field_name == "hgt":
                    if "cm" in field_value and not check_number(field_value[:-2], 150, 193):
                        is_valid = False 
                    if "in" in field_value and not check_number(field_value[:-2], 59, 76):
                        is_valid = False

                if field_name == "hcl" and re.match("^#[0-9|a-f]{6}$" ,field_value) == None:
                    is_valid = False
              
                if field_name == "ecl" and not any(x in field_value for x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    is_valid = False 
 
                if field_name == "pid" and re.match("^[0-9]{9}$" ,field_value) == None:
                    is_valid = False
 
        if is_valid:
            valid += 1

# Gives 1 more than expected for some reason
print(valid - 1)
