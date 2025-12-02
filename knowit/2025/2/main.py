a = 'abcdefghijklmnopqrstuvwxyzæøå'
with open('input.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        print(''.join([a[a.index(c)-i-1] for c in line.strip().lower()]), end='')
