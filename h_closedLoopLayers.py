import numpy as np

class ClosedLoopLayersClass:

	def __init__(self, ONION):
		self.ONION = ONION

	def LayerLoopsClosed(self):
		layersTotal = len(self.ONION)
		count = 0
		for i in range(0, layersTotal):
			individLayer = len(self.ONION[i])
			if (individLayer > 2):
				temp = self.ONION[i][count]
				self.ONION[i].append(temp)
		#print(self.ONION)

		return self.ONION




