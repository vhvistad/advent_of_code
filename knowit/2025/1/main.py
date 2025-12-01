key = ''
queue = []

with open('knowit/2025/1/input.txt', 'r') as file:
    log = file.read()

for line in log.splitlines():
    commands = line.split(' ')
    
    command = commands[0]

    if len(commands) > 1:
        gift = commands[1]

    if command == 'PROCESS':
        if len(queue) > 0:
            key += queue.pop(0)[0]
        else:
            key += 'X'
    elif command == 'COUNT':
        key += str(len(queue))[-1]
    elif command == 'ADD':
        queue.append(gift)
    
    print()
    

print(f'Final key: {key}')