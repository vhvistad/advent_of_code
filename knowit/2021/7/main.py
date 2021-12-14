santa = 20.0
ant = 1.0
i = 0
while ant < santa:
    ant += ant * 20.0 / santa
    santa += 20.0
    ant += 1.0
    if (i % 10000000) == 0:
        print(santa-ant)
    i += 1

print(f'Result = {santa}')

# for i in range(5):
#     ant += ant * 20.0 / santa
#     santa += 20.0
#     ant += 1.0
#     print(f'Santa: {santa}, Ant: {ant}')