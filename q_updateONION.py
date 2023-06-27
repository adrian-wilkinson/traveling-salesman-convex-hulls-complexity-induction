class UpdateOnionClass:

	def __init__(self, Quacky, decide, noMerges):
		self.Quacky = Quacky
		self.decide = decide
		self.noMerges = noMerges


	def updateOnion(self):
		layersTotalNow = len(self.Quacky)
		#print("Total Layers Now = ", layersTotalNow)
		inner = layersTotalNow - 1
		outer = layersTotalNow - 2
		INNER = self.Quacky[inner]
		OUTER = self.Quacky[outer]
		InOut = [INNER, OUTER]
		#print("INNER = ", INNER)
		#print(OUTER)

		move = self.decide[0]
		#print("MOOOOOOOOOOOVE = ", move)
		#print(move)
		loc = 2
		count = 0
		for i in INNER:
			findit = INNER[count][loc]
			if findit == move:
				#print("yes, findit = move")
				here = count
				break
			count += 1
		#print("here = ", here)

		grab = INNER[here]
		#print(grab)

		after = self.decide[2]
		#print(after)
		loc = 2
		count = 0
		for i in OUTER:
			findit = OUTER[count][loc]
			if findit == after:
				este = count
				break
			count += 1
		#print(este)

		newPosition = este + 1
		#print(newPosition)

		self.Quacky[outer].insert(newPosition, grab)
		#print(self.Quacky)

		innerLen = len(INNER)
		if (innerLen > 1):
			self.Quacky[inner].pop(here)
		else:
			self.Quacky.pop()

		#print("QQuacky is as does = ", self.Quacky)

		self.noMerges += 1

		this = [self.Quacky, self.noMerges]

		return this

