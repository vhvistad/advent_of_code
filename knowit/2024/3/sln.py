class Plate:
  def __init__(self):
    self.t = 0
    self.food = {
      "ris": 100,
      "erter": 100,
      "gulrøtter": 100,
      "reinsdyrkjøtt": 100,
      "julekringle": 100,
    }
    self.fill = {
      "ris": [0, 0, 1, 0, 0, 2],
      "erter": [0, 3, 0, 0],
      "gulrøtter": [0, 1, 0, 0, 0, 8],
      "reinsdyrkjøtt": [100, 80, 40, 20, 10],
      "julekringle": [0]
    }

  def tick(self):
    self.t += 1

  def eat(self):
    pass

  def fill(self):
    for key, val in self.fill.items():
      i = len(self.fill) % self.t
      amount = val[i]
      self.food[key] += amount


if __name__ == "__main__":
  pass
