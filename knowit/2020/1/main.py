filename = "knowit/1/test.txt"

f = open(filename, "r")
text = f.read().split(",")
f.close()

result = []
for i in range(len(text)+1):
  result.append(None)

for num in text:
  num = int(num)
  result[num-1] = num

for i in range(len(result)):
  if result[i] == None:
    print(i + 1)