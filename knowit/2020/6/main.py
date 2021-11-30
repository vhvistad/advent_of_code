def julegodt(pakkeliste, alver):
  pr_alv = 0
  tmp = 0
  rest = 0
  for antall in pakkeliste:
    antall = int(antall) + rest
    tmp = tmp + antall // alver
    rest = antall % alver
    if rest == 0:
      pr_alv += tmp
      tmp = 0
  return pr_alv

if __name__ == "__main__":
  with open('knowit/6/godteri.txt') as f:
    pakkeliste = f.read().split(',')

  resultat = julegodt(pakkeliste, 127)
  print(f'Hver alv får {resultat} biter')