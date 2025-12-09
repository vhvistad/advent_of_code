def is_num(c):
    return c in '1234567890'

def is_consonant(c):
    return c in 'bcdfghjklmnpqrstvwxz'

def is_lentil(substring):
    c = substring[2]

    if is_consonant(c) and is_num(substring[0]) and is_num(substring[4]):
        return False
    elif is_consonant(c) or is_num(c):
        return True
    return False

with open(f'C:/Users/vvistad/repos/advent_of_code/knowit/2025/9/input.txt', 'r') as f:
    string = f.readline().strip()

beans = ''
for i in range(2, len(string)-2):
    if not is_lentil(string[i-2:i+3]):
        beans += string[i]

print(beans)
