# Alvefine setter seg ned for å nyte sitt daglige julemåltid. 
# Hun spiser såklart ris, erter, gulrøtter, reinsdyrkjøtt og hennes favoritt: julekringle. 
# Hun ELSKER julekringle, men må spise opp resten av maten før hun kan begynne på den sier Alvemor.

# Tallerkenen hennes starter med 100g av hver type mat. Hvert sekund kan hun spise 5g av én type mat 
# og 3g av en annen type mat, prioritert fra venstre i listen. Hun kan kun spise 2g kjøtt om gangen, 
# og hun liker ikke å spise det sammen med noe. Hun får kun lov til å spise 1g julekringle om gangen, 
# og det går såklart heller ikke å spise sammen med noe annet.

# Alvemor fyller på mat etterhvert som Alvefine spiser: Tallene under viser hvor mange gram av en 
# type mat som fylles på hver gang det kommer mer. Når man er gått gjennom lista en gang starter man
# på nytt i det uendelige. ris, erter og gulrøtter fylles på hvert sekund.

# I tillegg er det noen spesielle regler:

# - Gulrøtter begynner ikke med påfyll før etter 30 sekunder.
# - Reinsdyrkjøtt fylles ikke på før det er helt tomt, og etter det er tomt går det 50 sekunder før Alvemor kommer med påfyll.
# - Det er ikke mer reinsdyrkjøtt når den opprinnelige listen er ferdig.
# - Julekringle fylles ikke på.

# Order: [ ris, erter, gulrøtter, reinsdyrkjøtt, julekringle ]

class Dinner:
  def __init__(self):
    self.t = 0
    self.last_meat = 0
    self.plate = {
      "ris": 100,
      "erter": 100,
      "gulrøtter": 100,
      "reinsdyrkjøtt": 100,
      "julekringle": 100,
    }
    self.fill_amounts = {
      "ris": [0, 0, 1, 0, 0, 2],
      "erter": [0, 3, 0, 0],
      "gulrøtter": [0, 1, 0, 0, 0, 8],
      "reinsdyrkjøtt": [100, 80, 40, 20, 10, 0],
      "julekringle": []
    }

  # Hvert sekund kan hun spise 5g av én type mat og 3g av en annen type mat
  # Prioritert fra venstre: [ ris, erter, gulrøtter, reinsdyrkjøtt, julekringle ]
  def tick(self):
    self.eat()
    self.fill_plate()
    self.t += 1

  def eat(self):
    to_eat = [5, 3]
    for food, amount_left in self.plate.items():
      if len(to_eat) == 0:
        return
      if amount_left == 0:
        continue
      if food in ['reinsdyrkjøtt', 'julekringle']:
        if len(to_eat) == 1:
          continue
        portion = 2 if food == 'reinsdyrkjøtt' else 1
        to_eat = []
      else:
        portion = to_eat.pop(0)
      if portion > amount_left:
        self.plate[food] -= amount_left
      else:
        self.plate[food] -= portion

  def move_back(self, food):
    self.fill_amounts[food].append(self.fill_amounts[food].pop(0))

  def fill_plate(self):
    for food, amounts in self.fill_amounts.items():

      if len(amounts) == 0:
        continue

      # Gulrøtter begynner ikke med påfyll før etter 30 sekunder.
      if food == 'gulrøtter' and self.t < 30:
        continue

      # - Reinsdyrkjøtt fylles ikke på før det er helt tomt, og etter det er tomt går det 50 sekunder før Alvemor kommer med påfyll.
      if food == 'reinsdyrkjøtt':

        if self.plate['reinsdyrkjøtt'] > 0:
          self.last_meat = self.t
          continue

        if self.t - self.last_meat < 50:
          continue
        else:
          # Det er ikke mer reinsdyrkjøtt når den opprinnelige listen er ferdig.
          self.plate['reinsdyrkjøtt'] += self.fill_amounts[food].pop(0)

      # # - Julekringle fylles ikke på.
      # if food == 'julekringle':
      #   continue
      else:
        amount = self.fill_amounts[food].pop(0)
        self.plate[food] += amount
        self.fill_amounts[food].append(amount)
  
  def __str__(self) -> str:
    string = f't = {self.t}\n'
    for food, amount_left in self.plate.items():
      fill_amounts = self.fill_amounts[food]
      if food in ['ris', 'erter']:
        food += '\t'
      padding = ''
      if amount_left < 10:
        padding = '\t'
      string += f'{food}\tleft: {amount_left}{padding}\t{str(fill_amounts)}\n'
    return string

if __name__ == "__main__":
  dinner = Dinner()
  previous = 0
  while dinner.plate['julekringle'] > 0: # and dinner.t < 272:
    # print(str(dinner))
    dinner.tick()
    current = dinner.plate['julekringle']
    if current != previous:
      print(current)
      previous = current


  # print(str(dinner))
  print(f'Result: t = {dinner.t}')
