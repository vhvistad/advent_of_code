def valid_byr(year):
  if len(year) != 4 or int(year) < 1920 or int(year) > 2002:
    return False
  return True

def valid_iyr(year):
  if len(year) != 4 or int(year) < 2010 or int(year) > 2020:
    return False
  return True

def valid_eyr(year):
  if len(year) != 4 or int(year) < 2020 or int(year) > 2030:
    return False
  return True

def valid_hgt(height):
  if height[-2:] == "cm" and len(height) == 5:
    height = int(height[0:2])
    if height >= 150 or height <= 193:
      return True
  elif height[-2:] == "in" and len(height) == 4:
    height = int(height[0:1])
    if height >= 59 or height <= 76:
      return True
  return False

def valid_hcl(color):
  if len(color) != 7 or color[0] != "#":
    return False
  for char in color[1:]:
    if char not in "0123456789abcdef":
      return False
  return True

def valid_ecl(color):
  valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  if color in valid:
    return True
  return False

def valid_pid(pid):
  try:
    int(pid)
  except:
    return False
  if len(pid) != 9:
    return False
  return True

def is_valid(field, value):
  if field == "byr":
    return valid_byr(value)
  if field == "iyr":
    return valid_iyr(value)
  if field == "eyr":
    return valid_eyr(value)
  if field == "hgt":
    return valid_hgt(value)
  if field == "hcl":
    return valid_hcl(value)
  if field == "ecl":
    return valid_ecl(value)
  if field == "pid":
    return valid_pid(value)
  
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
string = ""
with open("4/input.txt") as f:
  for line in f:
    if line == "\n":
      string = string + "$"
      continue
    string = string + line.strip() + " "

passports = string.split("$")
valid = 0

for p in passports:
  req = 0
  p = p.split(" ")
  for field in p:
    field = field.split(":")
    if field[0] in req_fields:
      if is_valid(field[0], field[1]):
        req += 1
  if req == 7:
    valid += 1
  # print(req)
print("Valid passports: " + str(valid))