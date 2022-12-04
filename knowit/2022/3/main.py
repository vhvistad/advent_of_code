def get_circumferences(width, height, length):
    return sorted([
        2*height + 2*length,
        2*height + 2*width,
        2*width + 2*length
    ])

def paper_required(width, height, length):
    # 3 mulige:
    #
    # 1: hoyde*2 + bredde*2 -> 
    #
    # 2: hoyde*2 + lengde*2 ->
    #
    # 3: bredde*2 + lengde*2 ->
    #
    # Hvis ett av de andre alternativene er mindre enn 110,
    # blir dette svaret.
    # Hvis ikke, prøv middles omkrets. 
    # Ellers blir det største omkrets

    circs = get_circumferences(width, height, length)

    if circs[1] <= 110:
        return circs[0]//2
    else:
        return circs[1]



with open('knowit/2022/3/pakker.csv', 'r') as f:
    boxes = f.readlines()[1:]

total = 0
for box in boxes:
    width, height, length = [int(s) for s in box.split(',')]
    # print(width)
    total += paper_required(width, height, length)

print(total)