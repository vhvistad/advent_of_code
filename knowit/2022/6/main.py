naughty_actions = {}
count = {
    'julenissen': 0,
    'alvekongen': 0,
    'sneglulf': 0
}

with open('knowit/2022/6/slemmehandlinger.txt', 'r', encoding='utf-8') as f:
    for line in f:
        action, weight = line.split(':')
        naughty_actions[action] = float(weight.strip())

with open('knowit/2022/6/stemmer.txt', 'r', encoding='utf-8') as f:
    for line in f:
        actions, vote = line.strip().split(':')
        weights = []

        for a in actions.split(','):
            if a not in naughty_actions:
                weights.append(1.0)
            else:
                weights.append(naughty_actions[a])

        count[vote] += min(weights)

print(f'Result: {round(max(count.values()) - sorted(list(count.values()))[1])}')