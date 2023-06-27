class PopulateOnionClass:

	def __init__(self, Onion, arrPlace, transfer):
		self.Onion = Onion
		self.arrPlace = arrPlace
		self.transfer = transfer


	def DeLayerOnion(self):

		layer = 0
		count = 0
		x_loc = 0
		y_loc = 1
		id_loc = 2
		onionLen = len(self.Onion)
		#print("Constructed ONION333 = ", self.Onion)
		#print("length of OnIOn2 = ", onionLen)
		arrPlaLen = len(self.arrPlace)
		#print("length of arrPlace = ", arrPlaLen)
		OnionGrab = []
		OnionCollector = []

		for i in range(0, onionLen):
			layer = self.Onion[i]
			layerLen = len(layer)

			for j in range(0, layerLen):
				findit = self.Onion[i][j]
				#print("findit = ", findit)

				for k in range(0, arrPlaLen):
					id_temp = self.arrPlace[k][id_loc]
					if id_temp == findit:
						#print("yes")
						x_grab = self.arrPlace[k][x_loc]
						y_grab = self.arrPlace[k][y_loc]
						grab = [x_grab, y_grab, findit]
						OnionGrab.append(grab)
						#break
					else:
						count += 1
			OnionCollector.append(OnionGrab)
			OnionGrab = []



		#print("id_temp = ", id_temp)

		#print("Onion  = ", OnionGrab)
		GrabLen = len(OnionGrab)
		#print("Onion Grab length = ", GrabLen)

		#print("Onion  = ", OnionCollector)
		collectLen = len(OnionCollector)
		#print("Onion Collector length = ", collectLen)
		self.transfer = OnionCollector
		#print("selftransfer = ", self.transfer)
		return self.transfer
