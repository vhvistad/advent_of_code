#Thea 4445,Eira 3855,Magnus 3445,Hugo 985,Nora 290,Sindre -875

# 170x + 13y = 4445

# 150x + 7y = 3855

# x = 25
# y = 15

scores = []

with open('knowit/2025/3/input.txt', 'r', encoding='utf-8') as f:
    f.readline()
    for line in f.readlines():
        navn, snill, slem, pepperkaker = line.split(',')
        scores.append([navn, (50*int(snill) - 25*int(slem) + 15*int(pepperkaker))])

result = sorted(scores, key=lambda x: x[1], reverse=True)

for i, _ in enumerate(result):
    result[i][1] = str(result[i][1])

print(','.join([' '.join(r) for r in result[:3]] + [' '.join(r) for r in result[-3:]]))

