
def get_matrix(filename):
    m = []
    with open(filename, 'r') as t:
        for line in t.readlines():
            if '\n' not in line:
                line = line + '\n'
            m.append(line[:-1])

    width_t = max([len(l) for l in m])

    for i, line in enumerate(m):
        if len(line) < width_t:
            diff = width_t-len(line)
            m[i] = list(line + ' '*diff)
        else:
            m[i] = list(line)
    
    return m

def total_k(alv_pos, alv, teppe):
    koselighet = 0
    limit_x = len(alv[0]) - alv_pos[1]
    limit_y = len(alv) - alv_pos[0]

    limit_y = len(teppe) if limit_y > len(teppe) else limit_y
    for i, line_t in enumerate(teppe[:limit_y]):
        limit_x = len(line_t) if limit_x > len(line_t) else limit_x
        for j, c in enumerate(line_t[:limit_x]):
            teppe_pos = (i, j)
            x = alv_pos[0] + teppe_pos[0]
            y = alv_pos[1] + teppe_pos[1]
            if c == 'x' and alv[x][y] != ' ':
                koselighet += int(alv[x][y])

    return koselighet

def find_max_k(alv, teppe):
    max_k = 0
    for i, line in enumerate(alv):
        for j, c in enumerate(line):
            pos = (i, j)
            koselighet = total_k(pos, alv, teppe)
            if koselighet > max_k:
                max_k = koselighet

    return max_k

alv = get_matrix('joe.txt')
teppe = get_matrix('teppe.txt')

max_k = find_max_k(alv, teppe)
teppe = list(zip(*teppe))
max_k = max(max_k, find_max_k(alv, teppe))

print(max_k)

