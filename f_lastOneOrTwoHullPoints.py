import numpy as np

class LastOneOrTwoHullPointsClass:
  def __init__(self, arrPlace, Onion):
    self.arrPlace = arrPlace
    self.Onion = Onion

  def last_1_2_HullPoints(self):
    last = len(self.arrPlace)
    #print("last = ", last)
    lastOne = []
    if ( last > 1):
      last_2 = self.arrPlace[0][2]
      last_1 = self.arrPlace[1][2]
      lastTwo = [last_2, last_1]
      temp = self.Onion.append(lastTwo)
      self.Onion = temp
      return self.Onion
    if ( last > 0):
      last_1 = self.arrPlace[0][2]
      lastOne = [last_1]
      temp = self.Onion.append(lastOne)
      self.Onion = temp
      return self.Onion