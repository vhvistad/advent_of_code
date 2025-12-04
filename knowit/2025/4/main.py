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
    required_e = energy[c] * 5
    prev_e = (energy[prev[0]] + energy[prev[1]]) * 5

    if e < required_e:
        break

    if c == "P" and prev_e > 0:
        e += prev_e

    e -= energy[c] * 5
    d += 10
    prev.pop()
    prev.insert(0, c)

print(d)