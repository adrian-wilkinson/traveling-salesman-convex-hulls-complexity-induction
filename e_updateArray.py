import numpy as np

class UpdateArrayClass:

  def __init__(self, array, arrPlace, layer):
    self.array = array
    self.arrPlace = arrPlace
    self.layer = layer


  def reduceArrays(self):
    count = 0
    a = self.layer
    for layer in a:
      index = a[count]
      self.array.pop(index)
      count += 1

    count = 0
    b = self.layer
    for layer in b:
      index = b[count]
      self.arrPlace.pop(index)
      count += 1
    thisIsNow = [self.array, self.arrPlace]
    return thisIsNow




