import re

count = 0

with open('knowit/2025/7/ordliste.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    word = line.strip().lower()

    if re.search('t.{1,5}r.{1,5}o.{1,5}l.{1,5}l', word) != None:
        count += 1

    if re.search('^[^n].*n.{0,2}i.{0,2}s.{0,2}s.{0,2}e.*[^e]$', word) != None:
        count += 1

print(f'Result = {count}')
