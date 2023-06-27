class InnerOuterOnionClass:

	def __init__(self, ONION):
		self.ONION = ONION

	def InnerOuterOnion(self):
		#print("Quacky = ", self.ONION)
		layersTotal = len(self.ONION)
		inner = layersTotal - 1
		outer = layersTotal - 2
		INNER = self.ONION[inner]
		OUTER = self.ONION[outer]
		InOut = [INNER, OUTER]
		#print(INNER)
		#print(OUTER)
		return InOut

