import re

with open('knowit/2022/2/gaver.txt', 'r', encoding='utf-8') as f:
    presents = f.readlines()

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
        lines_to_add += 1
        linecount += lines_to_add
        if re.search('alv', present) is not None:
            lines_to_add -=1

print(linecount)