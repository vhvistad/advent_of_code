concatenated = ''
count = 0

for i in range(100_000):
  if str(i) not in concatenated:
    concatenated += str(i)
    count += 1

print(f'Count = {count}')