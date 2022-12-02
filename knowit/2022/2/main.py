import re

test = "alver"
test2 = "franske høner"

print(re.search('alv', test))
print(re.search('alv', test2))

presents = []
with open('knowit/2022/2/test.txt', 'r') as f:
    for present in f:
        presents.append(present)

linecount = 0
last_presents = 0
lines_to_add = 2
for present in presents:
    if last_presents < 3:
        linecount += lines_to_add
        last_presents += 1
        if re.search('alv', present) is not None:
            last_presents -= 1
    else:
        linecount += lines_to_add
        lines_to_add += 1
        if re.search('alv', present) is not None:
            lines_to_add -=1
    print(f'Lines to add: {lines_to_add}')

print(linecount)