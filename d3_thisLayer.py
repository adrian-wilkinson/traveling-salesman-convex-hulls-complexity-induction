
import numpy as np

class ThisLayerClass:

  def __init__(self, array, layer):
    self.array = array
    self.layer = layer

  def descSortLayer(self):
    self.layer.sort(reverse=True)
    return self.layer
