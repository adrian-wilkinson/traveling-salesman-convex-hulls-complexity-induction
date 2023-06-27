import numpy as np

class ReAssignHullPointsClass:
  def __init__(self, arrPlace, layer, Onion):
    self.arrPlace = arrPlace
    self.layer = layer
    self.Onion = Onion

  def consistentHullPoints(self):
    newLayer = []
    a = self.layer
    two = 2
    count = 0
    for point in a:
      temp = self.arrPlace[point][two]
      newLayer.append(temp)
      count += 1
    self.layer = newLayer

    temp = self.Onion.append(self.layer)
    self.Onion = temp
    return self.Onion
