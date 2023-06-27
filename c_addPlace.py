import numpy as np

class AddPlaceClass:

  def __init__(self, array, arrPlace):
    self.array = array
    self.arrPlace = arrPlace

  def PlaceId(self):

      temp = []
      count = 0
      point = 1

      for i in self.array:
          hold1 = self.array[count][0]
          hold2 = self.array[count][1]
          temp = [hold1, hold2, point]   
          self.arrPlace.append(temp)
          count = count + 1
          point += 1

      return self.arrPlace