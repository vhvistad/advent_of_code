def checkPolicy(input):
    f = open(input, "r")
    count1 = 0
    count2 = 0
    for line in f:
        if isValidPassword1(line):
            #print(line)
            count1 += 1
        if isValidPassword2(line):
            #print(line)
            count2 += 1
    f.close()
    return count1, count2
        
def isValidPassword1(line):
    pp = line.split(":")
    password = pp[1].strip()
    letter = pp[0].split(" ")[1]
    numbers = pp[0].split(" ")[0].split("-")
    low = int(numbers[0])
    high = int(numbers[1])
    count = 0
    for char in password:
        if char == letter:
            count += 1
    return count >=low and count <= high

def isValidPassword2(line):
    pp = line.split(":")
    password = pp[1].strip()
    letter = pp[0].split(" ")[1]
    numbers = pp[0].split(" ")[0].split("-")
    first = int(numbers[0]) - 1
    second = int(numbers[1]) - 1
    valid = False
    if password[first] == letter:
        valid = not valid
    if password[second] == letter:
        valid = not valid
    return valid




if __name__ == "__main__":
    print(checkPolicy("input.txt"))