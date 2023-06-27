from scipy.spatial import ConvexHull
import numpy as np

class ConvexHullClass:
  def __init__(self, array, layer):
    self.array = array
    self.layer = layer

  def Around(self):
    a = np.array(self.array)
    hull = ConvexHull(a)
    n = len(hull.vertices)

    for i in range(0, n):
      this = hull.vertices[i]
      self.layer.append(this)

    return self.layer
