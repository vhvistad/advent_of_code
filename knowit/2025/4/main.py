with open('knowit/2025/4/track.txt', 'r') as f:
    track = f.readline().strip()

e = 3000
d = 0
prev = ["I", "I"]
energy = {
    "S": 1,
    "B": 2,
    "D": 3,
    "I": 0,
    "P": 0
}

for c in track:
    if e < 5:
        break
    if c == "P" and "I" not in prev and "P" not in prev:
        e += energy[prev[0]] + energy[prev[1]]
    else:
        e -= energy[c] * 5
    d += 10
    prev.pop(1)
    prev.insert(0, c)

print(d)