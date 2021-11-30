def getNumbers(inList):
  f = open(inList, "r")
  numbers = []
  for line in f:
    numbers.append(int(line))
  f.close()
  return numbers

def findTwo(inList):
  numbers = getNumbers(inList)
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == 2020:
        print("\ni = " + str(i))
        print("j = " + str(j))
        return str(numbers[i] * numbers[j])
  return "None found"

def findThree(inList):
  numbers = getNumbers(inList)
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      for k in range(j+1, len(numbers)):
        if numbers[i] + numbers[j] + numbers[k] == 2020:
          print("\ni = " + str(i))
          print("j = " + str(j))
          print("1: {}, 2: {}, 3: {}".format(numbers[i], numbers[j], numbers[k]))
          return str(numbers[i] * numbers[j] * numbers[k])
  return "None found"

if __name__ == "__main__":
    print("Result 1: " + findTwo("input.txt") + ", Result 2: " + findThree("input.txt"))