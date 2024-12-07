
def is_safe(r, lim):
    direction = r[0] < r[1]
    bad_levels = 0
    for i, l in enumerate(r):
        last =  len(r)-2
        k = r[i+1]

        a = r[i]
        b = r[i+1]
        test = a < b

        if test != direction:
            bad_levels += 1
            if bad_levels <= lim:
                continue
            return False
        diff = abs(l-k)
        if diff < 1 or diff > 3:
            bad_levels += 1
            if bad_levels <= lim:
                continue
            return False
        if i == last:
            return True
    
    return True



if __name__ == "__main__":
    filename = 'test.txt'
    # filename = 'input.txt'
    reports = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            levels = [int(n) for n in line.strip().split(' ')]
            reports.append(levels)
    
    safe = 0
    for i, r in enumerate(reports):
        if is_safe(r, lim=0):
            safe += 1
    
    print(f'Answer part 1: {safe}')

    safe = 0
    for i, r in enumerate(reports):
        if is_safe(r, lim=1):
            safe += 1
    print(f'Answer part 2: {safe}')
