import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class PlotOnionClass:

	def __init__(self, ONION):
		self.ONION = ONION

	def PlotThisOnion(self):
		layersTotal = len(self.ONION)
		x_loc = 0
		y_loc = 1

		# ********* Ring 1 ****************
		if (layersTotal > 0):
			layer_1 = self.ONION[0]
			Len_1 = len(layer_1)
			x_plot_1 = []
			y_plot_1 = []
			for i in range(0, Len_1):
				x_temp = layer_1[i][x_loc]
				y_temp = layer_1[i][y_loc]
				x_plot_1.append(x_temp)
				y_plot_1.append(y_temp)
			x_temp = layer_1[0][0]
			y_temp = layer_1[0][1]
			x_plot_1.append(x_temp)
			y_plot_1.append(y_temp)
		# ********* Ring 2 ****************
		if (layersTotal > 1):
			layer_2 = self.ONION[1]
			Len_2 = len(layer_2)
			x_plot_2 = []
			y_plot_2 = []
			for i in range(0, Len_2):
				x_temp = layer_2[i][x_loc]
				y_temp = layer_2[i][y_loc]
				x_plot_2.append(x_temp)
				y_plot_2.append(y_temp)
			x_temp = layer_2[0][0]
			y_temp = layer_2[0][1]
			x_plot_2.append(x_temp)
			y_plot_2.append(y_temp)
		# ********* Ring 3 ****************
		if (layersTotal > 2):
			layer_3 = self.ONION[2]
			Len_3 = len(layer_3)
			x_plot_3 = []
			y_plot_3 = []
			for i in range(0, Len_3):
				x_temp = layer_3[i][x_loc]
				y_temp = layer_3[i][y_loc]
				x_plot_3.append(x_temp)
				y_plot_3.append(y_temp)
			x_temp = layer_3[0][0]
			y_temp = layer_3[0][1]
			x_plot_3.append(x_temp)
			y_plot_3.append(y_temp)
		# ********* Ring 4 ****************
		if (layersTotal > 3):
			layer_4 = self.ONION[3]
			Len_4 = len(layer_4)
			x_plot_4 = []
			y_plot_4 = []
			for i in range(0, Len_4):
				x_temp = layer_4[i][x_loc]
				y_temp = layer_4[i][y_loc]
				x_plot_4.append(x_temp)
				y_plot_4.append(y_temp)
			x_temp = layer_4[0][0]
			y_temp = layer_4[0][1]
			x_plot_4.append(x_temp)
			y_plot_4.append(y_temp)
		# ********* Ring 5 ****************
		if (layersTotal > 4):
			layer_5 = self.ONION[4]
			Len_5 = len(layer_5)
			x_plot_5 = []
			y_plot_5 = []
			for i in range(0, Len_5):
				x_temp = layer_5[i][x_loc]
				y_temp = layer_5[i][y_loc]
				x_plot_5.append(x_temp)
				y_plot_5.append(y_temp)
			x_temp = layer_5[0][0]
			y_temp = layer_5[0][1]
			x_plot_5.append(x_temp)
			y_plot_5.append(y_temp)
		# ********* Ring 6 ****************
		if (layersTotal > 5):
			layer_6 = self.ONION[5]
			Len_6 = len(layer_6)
			x_plot_6 = []
			y_plot_6 = []
			for i in range(0, Len_6):
				x_temp = layer_6[i][x_loc]
				y_temp = layer_6[i][y_loc]
				x_plot_6.append(x_temp)
				y_plot_6.append(y_temp)
			x_temp = layer_6[0][0]
			y_temp = layer_6[0][1]
			x_plot_6.append(x_temp)
			y_plot_6.append(y_temp)
		# ********* Ring 7 ****************
		if (layersTotal > 6):
			layer_7 = self.ONION[6]
			Len_7 = len(layer_7)
			x_plot_7 = []
			y_plot_7 = []
			for i in range(0, Len_7):
				x_temp = layer_7[i][x_loc]
				y_temp = layer_7[i][y_loc]
				x_plot_7.append(x_temp)
				y_plot_7.append(y_temp)
			x_temp = layer_7[0][0]
			y_temp = layer_7[0][1]
			x_plot_7.append(x_temp)
			y_plot_7.append(y_temp)
		# ********* Ring 8 ****************
		if (layersTotal > 7):
			layer_8 = self.ONION[7]
			Len_8 = len(layer_8)
			x_plot_8 = []
			y_plot_8 = []
			for i in range(0, Len_8):
				x_temp = layer_8[i][x_loc]
				y_temp = layer_8[i][y_loc]
				x_plot_8.append(x_temp)
				y_plot_8.append(y_temp)
			x_temp = layer_8[0][0]
			y_temp = layer_8[0][1]
			x_plot_8.append(x_temp)
			y_plot_8.append(y_temp)
		# ********* Ring 9 ****************
		if (layersTotal > 8):
			layer_9 = self.ONION[8]
			Len_9 = len(layer_9)
			x_plot_9 = []
			y_plot_9 = []
			for i in range(0, Len_9):
				x_temp = layer_9[i][x_loc]
				y_temp = layer_9[i][y_loc]
				x_plot_9.append(x_temp)
				y_plot_9.append(y_temp)
			x_temp = layer_9[0][0]
			y_temp = layer_9[0][1]
			x_plot_9.append(x_temp)
			y_plot_9.append(y_temp)
		# ********* Ring 10 ****************
		if (layersTotal > 9):
			layer_10 = self.ONION[9]
			Len_10 = len(layer_10)
			x_plot_10 = []
			y_plot_10 = []
			for i in range(0, Len_10):
				x_temp = layer_10[i][x_loc]
				y_temp = layer_10[i][y_loc]
				x_plot_10.append(x_temp)
				y_plot_10.append(y_temp)
			x_temp = layer_10[0][0]
			y_temp = layer_10[0][1]
			x_plot_10.append(x_temp)
			y_plot_10.append(y_temp)
		# ********* Ring 11 ****************
		if (layersTotal > 10):
			layer_11 = self.ONION[10]
			Len_11 = len(layer_11)
			x_plot_11 = []
			y_plot_11 = []
			for i in range(0, Len_11):
				x_temp = layer_11[i][x_loc]
				y_temp = layer_11[i][y_loc]
				x_plot_11.append(x_temp)
				y_plot_11.append(y_temp)
			x_temp = layer_11[0][0]
			y_temp = layer_11[0][1]
			x_plot_11.append(x_temp)
			y_plot_11.append(y_temp)
		# ********* Ring 12 ****************
		if (layersTotal > 11):
			layer_12 = self.ONION[11]
			Len_12 = len(layer_12)
			x_plot_12 = []
			y_plot_12 = []
			for i in range(0, Len_12):
				x_temp = layer_12[i][x_loc]
				y_temp = layer_12[i][y_loc]
				x_plot_12.append(x_temp)
				y_plot_12.append(y_temp)
			x_temp = layer_12[0][0]
			y_temp = layer_12[0][1]
			x_plot_12.append(x_temp)
			y_plot_12.append(y_temp)
		# ********* Ring 13 ****************
		if (layersTotal > 12):
			layer_13 = self.ONION[12]
			Len_13 = len(layer_13)
			x_plot_13 = []
			y_plot_13 = []
			for i in range(0, Len_13):
				x_temp = layer_13[i][x_loc]
				y_temp = layer_13[i][y_loc]
				x_plot_13.append(x_temp)
				y_plot_13.append(y_temp)
			x_temp = layer_13[0][0]
			y_temp = layer_13[0][1]
			x_plot_13.append(x_temp)
			y_plot_13.append(y_temp)
		# ********* Ring 14 ****************
		if (layersTotal > 13):
			layer_14 = self.ONION[13]
			Len_14 = len(layer_14)
			x_plot_14 = []
			y_plot_14 = []
			for i in range(0, Len_14):
				x_temp = layer_14[i][x_loc]
				y_temp = layer_14[i][y_loc]
				x_plot_14.append(x_temp)
				y_plot_14.append(y_temp)
			x_temp = layer_14[0][0]
			y_temp = layer_14[0][1]
			x_plot_14.append(x_temp)
			y_plot_14.append(y_temp)
		# ********* Ring 15 ****************
		if (layersTotal > 14):
			layer_15 = self.ONION[14]
			Len_15 = len(layer_15)
			#print("LLLLLLength of layer 15 = ", Len_15)
			#print("Layer 15 = ", layer_15)
			x_plot_15 = []
			y_plot_15 = []
			for i in range(0, Len_15):
				x_temp = layer_15[i][x_loc]
				y_temp = layer_15[i][y_loc]
				x_plot_15.append(x_temp)
				y_plot_15.append(y_temp)
			x_temp = layer_15[0][0]
			y_temp = layer_15[0][1]
			x_plot_15.append(x_temp)
			y_plot_15.append(y_temp)
		# ********* Ring 16 ****************
		if (layersTotal > 15):
			layer_16 = self.ONION[15]
			Len_16 = len(layer_16)
			#print("LLLLLLength of layer 16 = ", Len_16)
			#print("Layer 16 = ", layer_16)
			x_plot_16 = []
			y_plot_16 = []
			for i in range(0, Len_16):
				x_temp = layer_16[i][x_loc]
				y_temp = layer_16[i][y_loc]
				x_plot_16.append(x_temp)
				y_plot_16.append(y_temp)
			x_temp = layer_16[0][0]
			y_temp = layer_16[0][1]
			x_plot_16.append(x_temp)
			y_plot_16.append(y_temp)
		# ********* Ring 17 ****************
		if (layersTotal > 16):
			layer_17 = self.ONION[16]
			Len_17 = len(layer_17)
			x_plot_17 = []
			y_plot_17 = []
			for i in range(0, Len_17):
				x_temp = layer_17[i][x_loc]
				y_temp = layer_17[i][y_loc]
				x_plot_17.append(x_temp)
				y_plot_17.append(y_temp)
			x_temp = layer_17[0][0]
			y_temp = layer_17[0][1]
			x_plot_17.append(x_temp)
			y_plot_17.append(y_temp)
		# ********* Ring 18 ****************
		if (layersTotal > 17):
			layer_18 = self.ONION[17]
			Len_18 = len(layer_18)
			x_plot_18 = []
			y_plot_18 = []
			for i in range(0, Len_18):
				x_temp = layer_18[i][x_loc]
				y_temp = layer_18[i][y_loc]
				x_plot_18.append(x_temp)
				y_plot_18.append(y_temp)
			x_temp = layer_18[0][0]
			y_temp = layer_18[0][1]
			x_plot_18.append(x_temp)
			y_plot_18.append(y_temp)
		# ********* Ring 19 ****************
		if (layersTotal > 18):
			layer_19 = self.ONION[18]
			Len_19 = len(layer_19)
			x_plot_19 = []
			y_plot_19 = []
			for i in range(0, Len_19):
				x_temp = layer_19[i][x_loc]
				y_temp = layer_19[i][y_loc]
				x_plot_19.append(x_temp)
				y_plot_19.append(y_temp)
			x_temp = layer_19[0][0]
			y_temp = layer_19[0][1]
			x_plot_19.append(x_temp)
			y_plot_19.append(y_temp)
		# ********* Ring 20 ****************
		if (layersTotal > 19):
			layer_20 = self.ONION[20]
			Len_20 = len(layer_20)
			x_plot_20 = []
			y_plot_20 = []
			for i in range(0, Len_20):
				x_temp = layer_20[i][x_loc]
				y_temp = layer_20[i][y_loc]
				x_plot_20.append(x_temp)
				y_plot_20.append(y_temp)
			x_temp = layer_20[0][0]
			y_temp = layer_20[0][1]
			x_plot_20.append(x_temp)
			y_plot_20.append(y_temp)
		# ********* Ring 21 ****************
		if (layersTotal > 20):
			layer_21 = self.ONION[20]
			Len_21 = len(layer_21)
			x_plot_21 = []
			y_plot_21 = []
			for i in range(0, Len_21):
				x_temp = layer_21[i][x_loc]
				y_temp = layer_21[i][y_loc]
				x_plot_21.append(x_temp)
				y_plot_21.append(y_temp)
			x_temp = layer_21[0][0]
			y_temp = layer_21[0][1]
			x_plot_21.append(x_temp)
			y_plot_21.append(y_temp)
		# ********* Ring 22 ****************
		if (layersTotal > 21):
			layer_22 = self.ONION[21]
			Len_22 = len(layer_22)
			x_plot_22 = []
			y_plot_22 = []
			for i in range(0, Len_22):
				x_temp = layer_22[i][x_loc]
				y_temp = layer_22[i][y_loc]
				x_plot_22.append(x_temp)
				y_plot_22.append(y_temp)
			x_temp = layer_22[0][0]
			y_temp = layer_22[0][1]
			x_plot_22.append(x_temp)
			y_plot_22.append(y_temp)
		# ********* Ring 23 ****************
		if (layersTotal > 22):
			layer_23 = self.ONION[22]
			Len_23 = len(layer_23)
			x_plot_23 = []
			y_plot_23 = []
			for i in range(0, Len_23):
				x_temp = layer_23[i][x_loc]
				y_temp = layer_23[i][y_loc]
				x_plot_23.append(x_temp)
				y_plot_23.append(y_temp)
			x_temp = layer_23[0][0]
			y_temp = layer_23[0][1]
			x_plot_23.append(x_temp)
			y_plot_23.append(y_temp)
		# ********* Ring 24 ****************
		if (layersTotal > 23):
			layer_24 = self.ONION[23]
			Len_24 = len(layer_24)
			x_plot_24 = []
			y_plot_24 = []
			for i in range(0, Len_24):
				x_temp = layer_24[i][x_loc]
				y_temp = layer_24[i][y_loc]
				x_plot_24.append(x_temp)
				y_plot_24.append(y_temp)
			x_temp = layer_24[0][0]
			y_temp = layer_24[0][1]
			x_plot_24.append(x_temp)
			y_plot_24.append(y_temp)
		# ********* Ring 25 ****************
		if (layersTotal > 24):
			layer_25 = self.ONION[24]
			Len_25 = len(layer_25)
			x_plot_25 = []
			y_plot_25 = []
			for i in range(0, Len_25):
				x_temp = layer_25[i][x_loc]
				y_temp = layer_25[i][y_loc]
				x_plot_25.append(x_temp)
				y_plot_25.append(y_temp)
			x_temp = layer_25[0][0]
			y_temp = layer_25[0][1]
			x_plot_25.append(x_temp)
			y_plot_25.append(y_temp)
		# ********* Ring 26 ****************
		if (layersTotal > 25):
			layer_26 = self.ONION[25]
			Len_26 = len(layer_26)
			x_plot_26 = []
			y_plot_26 = []
			for i in range(0, Len_26):
				x_temp = layer_26[i][x_loc]
				y_temp = layer_26[i][y_loc]
				x_plot_26.append(x_temp)
				y_plot_26.append(y_temp)
			x_temp = layer_26[0][0]
			y_temp = layer_26[0][1]
			x_plot_26.append(x_temp)
			y_plot_26.append(y_temp)
		# ********* Ring 27 ****************
		if (layersTotal > 26):
			layer_27 = self.ONION[26]
			Len_27 = len(layer_27)
			x_plot_27 = []
			y_plot_27 = []
			for i in range(0, Len_27):
				x_temp = layer_27[i][x_loc]
				y_temp = layer_27[i][y_loc]
				x_plot_27.append(x_temp)
				y_plot_27.append(y_temp)
			x_temp = layer_27[0][0]
			y_temp = layer_27[0][1]
			x_plot_27.append(x_temp)
			y_plot_27.append(y_temp)
		# ********* Ring 28 ****************
		if (layersTotal > 27):
			layer_28 = self.ONION[27]
			Len_28 = len(layer_28)
			x_plot_28 = []
			y_plot_28 = []
			for i in range(0, Len_28):
				x_temp = layer_28[i][x_loc]
				y_temp = layer_28[i][y_loc]
				x_plot_28.append(x_temp)
				y_plot_28.append(y_temp)
			x_temp = layer_28[0][0]
			y_temp = layer_28[0][1]
			x_plot_28.append(x_temp)
			y_plot_28.append(y_temp)
		# ********* Ring 29 ****************
		if (layersTotal > 28):
			layer_29 = self.ONION[28]
			Len_29 = len(layer_29)
			x_plot_29 = []
			y_plot_29 = []
			for i in range(0, Len_29):
				x_temp = layer_29[i][x_loc]
				y_temp = layer_29[i][y_loc]
				x_plot_29.append(x_temp)
				y_plot_29.append(y_temp)
			x_temp = layer_29[0][0]
			y_temp = layer_29[0][1]
			x_plot_29.append(x_temp)
			y_plot_29.append(y_temp)
		# ********* Ring 30 ****************
		if (layersTotal > 29):
			layer_30 = self.ONION[29]
			Len_30 = len(layer_30)
			x_plot_30 = []
			y_plot_30 = []
			for i in range(0, Len_30):
				x_temp = layer_30[i][x_loc]
				y_temp = layer_30[i][y_loc]
				x_plot_30.append(x_temp)
				y_plot_30.append(y_temp)
			x_temp = layer_30[0][0]
			y_temp = layer_30[0][1]
			x_plot_30.append(x_temp)
			y_plot_30.append(y_temp)
		# ********* Ring 31 ****************
		if (layersTotal > 30):
			layer_31 = self.ONION[30]
			Len_31 = len(layer_31)
			x_plot_31 = []
			y_plot_31 = []
			for i in range(0, Len_31):
				x_temp = layer_31[i][x_loc]
				y_temp = layer_31[i][y_loc]
				x_plot_31.append(x_temp)
				y_plot_31.append(y_temp)
			x_temp = layer_31[0][0]
			y_temp = layer_31[0][1]
			x_plot_31.append(x_temp)
			y_plot_31.append(y_temp)
		# ********* Ring 32 ****************
		if (layersTotal > 31):
			layer_32 = self.ONION[31]
			Len_32 = len(layer_32)
			x_plot_32 = []
			y_plot_32 = []
			for i in range(0, Len_32):
				x_temp = layer_32[i][x_loc]
				y_temp = layer_32[i][y_loc]
				x_plot_32.append(x_temp)
				y_plot_32.append(y_temp)
			x_temp = layer_32[0][0]
			y_temp = layer_32[0][1]
			x_plot_32.append(x_temp)
			y_plot_32.append(y_temp)
		# ********* Ring 33 ****************
		if (layersTotal > 32):
			layer_33 = self.ONION[32]
			Len_33 = len(layer_33)
			x_plot_33 = []
			y_plot_33 = []
			for i in range(0, Len_33):
				x_temp = layer_33[i][x_loc]
				y_temp = layer_33[i][y_loc]
				x_plot_33.append(x_temp)
				y_plot_33.append(y_temp)
			x_temp = layer_33[0][0]
			y_temp = layer_33[0][1]
			x_plot_33.append(x_temp)
			y_plot_33.append(y_temp)
		# ********* Ring 34 ****************
		if (layersTotal > 33):
			layer_34 = self.ONION[33]
			Len_34 = len(layer_34)
			x_plot_34 = []
			y_plot_34 = []
			for i in range(0, Len_34):
				x_temp = layer_34[i][x_loc]
				y_temp = layer_34[i][y_loc]
				x_plot_34.append(x_temp)
				y_plot_34.append(y_temp)
			x_temp = layer_34[0][0]
			y_temp = layer_34[0][1]
			x_plot_34.append(x_temp)
			y_plot_34.append(y_temp)
		# ********* Ring 35 ****************
		if (layersTotal > 34):
			layer_35 = self.ONION[34]
			Len_35 = len(layer_35)
			x_plot_35 = []
			y_plot_35 = []
			for i in range(0, Len_35):
				x_temp = layer_35[i][x_loc]
				y_temp = layer_35[i][y_loc]
				x_plot_35.append(x_temp)
				y_plot_35.append(y_temp)
			x_temp = layer_35[0][0]
			y_temp = layer_35[0][1]
			x_plot_35.append(x_temp)
			y_plot_35.append(y_temp)
		# ********* Ring 36 ****************
		if (layersTotal > 35):
			layer_36 = self.ONION[35]
			Len_36 = len(layer_36)
			x_plot_36 = []
			y_plot_36 = []
			for i in range(0, Len_36):
				x_temp = layer_36[i][x_loc]
				y_temp = layer_36[i][y_loc]
				x_plot_36.append(x_temp)
				y_plot_36.append(y_temp)
			x_temp = layer_36[0][0]
			y_temp = layer_36[0][1]
			x_plot_36.append(x_temp)
			y_plot_36.append(y_temp)
		# ********* Ring 37 ****************
		if (layersTotal > 36):
			layer_37 = self.ONION[36]
			Len_37 = len(layer_37)
			x_plot_37 = []
			y_plot_37 = []
			for i in range(0, Len_37):
				x_temp = layer_37[i][x_loc]
				y_temp = layer_37[i][y_loc]
				x_plot_37.append(x_temp)
				y_plot_37.append(y_temp)
			x_temp = layer_37[0][0]
			y_temp = layer_37[0][1]
			x_plot_37.append(x_temp)
			y_plot_37.append(y_temp)
		# ********* Ring 38 ****************
		if (layersTotal > 37):
			layer_38 = self.ONION[37]
			Len_38 = len(layer_38)
			x_plot_38 = []
			y_plot_38 = []
			for i in range(0, Len_38):
				x_temp = layer_38[i][x_loc]
				y_temp = layer_38[i][y_loc]
				x_plot_38.append(x_temp)
				y_plot_38.append(y_temp)
			x_temp = layer_38[0][0]
			y_temp = layer_38[0][1]
			x_plot_38.append(x_temp)
			y_plot_38.append(y_temp)
		# ********* Ring 39 ****************
		if (layersTotal > 38):
			layer_39 = self.ONION[38]
			Len_39 = len(layer_39)
			x_plot_39 = []
			y_plot_39 = []
			for i in range(0, Len_39):
				x_temp = layer_39[i][x_loc]
				y_temp = layer_39[i][y_loc]
				x_plot_39.append(x_temp)
				y_plot_39.append(y_temp)
			x_temp = layer_39[0][0]
			y_temp = layer_39[0][1]
			x_plot_39.append(x_temp)
			y_plot_39.append(y_temp)
		# ********* Ring 40 ****************
		if (layersTotal > 39):
			layer_40 = self.ONION[39]
			Len_40 = len(layer_40)
			x_plot_40 = []
			y_plot_40 = []
			for i in range(0, Len_40):
				x_temp = layer_40[i][x_loc]
				y_temp = layer_40[i][y_loc]
				x_plot_40.append(x_temp)
				y_plot_40.append(y_temp)
			x_temp = layer_40[0][0]
			y_temp = layer_40[0][1]
			x_plot_40.append(x_temp)
			y_plot_40.append(y_temp)
		# ********* Ring 41 ****************
		if (layersTotal > 40):
			layer_41 = self.ONION[40]
			Len_41 = len(layer_41)
			x_plot_41 = []
			y_plot_41 = []
			for i in range(0, Len_41):
				x_temp = layer_41[i][x_loc]
				y_temp = layer_41[i][y_loc]
				x_plot_41.append(x_temp)
				y_plot_41.append(y_temp)
			x_temp = layer_41[0][0]
			y_temp = layer_41[0][1]
			x_plot_41.append(x_temp)
			y_plot_41.append(y_temp)
		# ********* Ring 42 ****************
		if (layersTotal > 41):
			layer_42 = self.ONION[41]
			Len_42 = len(layer_42)
			x_plot_42 = []
			y_plot_42 = []
			for i in range(0, Len_42):
				x_temp = layer_42[i][x_loc]
				y_temp = layer_42[i][y_loc]
				x_plot_42.append(x_temp)
				y_plot_42.append(y_temp)
			x_temp = layer_42[0][0]
			y_temp = layer_42[0][1]
			x_plot_42.append(x_temp)
			y_plot_42.append(y_temp)
		# ********* Ring 43 ****************
		if (layersTotal > 42):
			layer_43 = self.ONION[42]
			Len_43 = len(layer_43)
			x_plot_43 = []
			y_plot_43 = []
			for i in range(0, Len_43):
				x_temp = layer_43[i][x_loc]
				y_temp = layer_43[i][y_loc]
				x_plot_43.append(x_temp)
				y_plot_43.append(y_temp)
			x_temp = layer_43[0][0]
			y_temp = layer_43[0][1]
			x_plot_43.append(x_temp)
			y_plot_43.append(y_temp)
		# ********* Ring 44 ****************
		if (layersTotal > 43):
			layer_44 = self.ONION[43]
			Len_44 = len(layer_44)
			x_plot_44 = []
			y_plot_44 = []
			for i in range(0, Len_44):
				x_temp = layer_44[i][x_loc]
				y_temp = layer_44[i][y_loc]
				x_plot_44.append(x_temp)
				y_plot_44.append(y_temp)
			x_temp = layer_44[0][0]
			y_temp = layer_44[0][1]
			x_plot_44.append(x_temp)
			y_plot_44.append(y_temp)
		# ********* Ring 45 ****************
		if (layersTotal > 44):
			layer_45 = self.ONION[44]
			Len_45 = len(layer_45)
			x_plot_45 = []
			y_plot_45 = []
			for i in range(0, Len_45):
				x_temp = layer_45[i][x_loc]
				y_temp = layer_45[i][y_loc]
				x_plot_45.append(x_temp)
				y_plot_45.append(y_temp)
			x_temp = layer_45[0][0]
			y_temp = layer_45[0][1]
			x_plot_45.append(x_temp)
			y_plot_45.append(y_temp)
		# ********* Ring 46 ****************
		if (layersTotal > 45):
			layer_46 = self.ONION[45]
			Len_46 = len(layer_46)
			x_plot_46 = []
			y_plot_46 = []
			for i in range(0, Len_46):
				x_temp = layer_46[i][x_loc]
				y_temp = layer_46[i][y_loc]
				x_plot_46.append(x_temp)
				y_plot_46.append(y_temp)
			x_temp = layer_46[0][0]
			y_temp = layer_46[0][1]
			x_plot_46.append(x_temp)
			y_plot_46.append(y_temp)
		# ********* Ring 47 ****************
		if (layersTotal > 46):
			layer_47 = self.ONION[46]
			Len_47 = len(layer_47)
			x_plot_47 = []
			y_plot_47 = []
			for i in range(0, Len_47):
				x_temp = layer_47[i][x_loc]
				y_temp = layer_47[i][y_loc]
				x_plot_47.append(x_temp)
				y_plot_47.append(y_temp)
			x_temp = layer_47[0][0]
			y_temp = layer_47[0][1]
			x_plot_47.append(x_temp)
			y_plot_47.append(y_temp)
		# ********* Ring 48 ****************
		if (layersTotal > 47):
			layer_48 = self.ONION[47]
			Len_48 = len(layer_48)
			x_plot_48 = []
			y_plot_48 = []
			for i in range(0, Len_48):
				x_temp = layer_48[i][x_loc]
				y_temp = layer_48[i][y_loc]
				x_plot_48.append(x_temp)
				y_plot_48.append(y_temp)
			x_temp = layer_48[0][0]
			y_temp = layer_48[0][1]
			x_plot_48.append(x_temp)
			y_plot_48.append(y_temp)
		# ********* Ring 49 ****************
		if (layersTotal > 48):
			layer_49 = self.ONION[48]
			Len_49 = len(layer_49)
			x_plot_49 = []
			y_plot_49 = []
			for i in range(0, Len_49):
				x_temp = layer_49[i][x_loc]
				y_temp = layer_49[i][y_loc]
				x_plot_49.append(x_temp)
				y_plot_49.append(y_temp)
			x_temp = layer_49[0][0]
			y_temp = layer_49[0][1]
			x_plot_49.append(x_temp)
			y_plot_49.append(y_temp)
		# ********* Ring 50 ****************
		if (layersTotal > 49):
			layer_50 = self.ONION[49]
			Len_50 = len(layer_50)
			x_plot_50 = []
			y_plot_50 = []
			for i in range(0, Len_50):
				x_temp = layer_50[i][x_loc]
				y_temp = layer_50[i][y_loc]
				x_plot_50.append(x_temp)
				y_plot_50.append(y_temp)
			x_temp = layer_50[0][0]
			y_temp = layer_50[0][1]
			x_plot_50.append(x_temp)
			y_plot_50.append(y_temp)
		# ********* Ring 51 ****************
		if (layersTotal > 50):
			layer_51 = self.ONION[50]
			Len_51 = len(layer_51)
			x_plot_51 = []
			y_plot_51 = []
			for i in range(0, Len_51):
				x_temp = layer_51[i][x_loc]
				y_temp = layer_51[i][y_loc]
				x_plot_51.append(x_temp)
				y_plot_51.append(y_temp)
			x_temp = layer_51[0][0]
			y_temp = layer_51[0][1]
			x_plot_51.append(x_temp)
			y_plot_51.append(y_temp)
		# ********* Ring 52 ****************
		if (layersTotal > 51):
			layer_52 = self.ONION[51]
			Len_52 = len(layer_52)
			x_plot_52 = []
			y_plot_52 = []
			for i in range(0, Len_52):
				x_temp = layer_52[i][x_loc]
				y_temp = layer_52[i][y_loc]
				x_plot_52.append(x_temp)
				y_plot_52.append(y_temp)
			x_temp = layer_52[0][0]
			y_temp = layer_52[0][1]
			x_plot_52.append(x_temp)
			y_plot_52.append(y_temp)
		# ********* Ring 53 ****************
		if (layersTotal > 52):
			layer_53 = self.ONION[52]
			Len_53 = len(layer_53)
			x_plot_53 = []
			y_plot_53 = []
			for i in range(0, Len_53):
				x_temp = layer_53[i][x_loc]
				y_temp = layer_53[i][y_loc]
				x_plot_53.append(x_temp)
				y_plot_53.append(y_temp)
			x_temp = layer_53[0][0]
			y_temp = layer_53[0][1]
			x_plot_53.append(x_temp)
			y_plot_53.append(y_temp)
		# ********* Ring 54 ****************
		if (layersTotal > 53):
			layer_54 = self.ONION[53]
			Len_54 = len(layer_54)
			x_plot_54 = []
			y_plot_54 = []
			for i in range(0, Len_54):
				x_temp = layer_54[i][x_loc]
				y_temp = layer_54[i][y_loc]
				x_plot_54.append(x_temp)
				y_plot_54.append(y_temp)
			x_temp = layer_54[0][0]
			y_temp = layer_54[0][1]
			x_plot_54.append(x_temp)
			y_plot_54.append(y_temp)
		# ********* Ring 55 ****************
		if (layersTotal > 54):
			layer_55 = self.ONION[54]
			Len_55 = len(layer_55)
			x_plot_55 = []
			y_plot_55 = []
			for i in range(0, Len_55):
				x_temp = layer_55[i][x_loc]
				y_temp = layer_55[i][y_loc]
				x_plot_55.append(x_temp)
				y_plot_55.append(y_temp)
			x_temp = layer_55[0][0]
			y_temp = layer_55[0][1]
			x_plot_55.append(x_temp)
			y_plot_55.append(y_temp)
		# ********* Ring 56 ****************
		if (layersTotal > 55):
			layer_56 = self.ONION[55]
			Len_56 = len(layer_56)
			x_plot_56 = []
			y_plot_56 = []
			for i in range(0, Len_56):
				x_temp = layer_56[i][x_loc]
				y_temp = layer_56[i][y_loc]
				x_plot_56.append(x_temp)
				y_plot_56.append(y_temp)
			x_temp = layer_56[0][0]
			y_temp = layer_56[0][1]
			x_plot_56.append(x_temp)
			y_plot_56.append(y_temp)
		# ********* Ring 57 ****************
		if (layersTotal > 56):
			layer_57 = self.ONION[56]
			Len_57 = len(layer_57)
			x_plot_57 = []
			y_plot_57 = []
			for i in range(0, Len_57):
				x_temp = layer_57[i][x_loc]
				y_temp = layer_57[i][y_loc]
				x_plot_57.append(x_temp)
				y_plot_57.append(y_temp)
			x_temp = layer_57[0][0]
			y_temp = layer_57[0][1]
			x_plot_57.append(x_temp)
			y_plot_57.append(y_temp)
		# ********* Ring 58 ****************
		if (layersTotal > 57):
			layer_58 = self.ONION[57]
			Len_58 = len(layer_58)
			x_plot_58 = []
			y_plot_58 = []
			for i in range(0, Len_58):
				x_temp = layer_58[i][x_loc]
				y_temp = layer_58[i][y_loc]
				x_plot_58.append(x_temp)
				y_plot_58.append(y_temp)
			x_temp = layer_58[0][0]
			y_temp = layer_58[0][1]
			x_plot_58.append(x_temp)
			y_plot_58.append(y_temp)
		# ********* Ring 59 ****************
		if (layersTotal > 58):
			layer_59 = self.ONION[58]
			Len_59 = len(layer_59)
			x_plot_59 = []
			y_plot_59 = []
			for i in range(0, Len_59):
				x_temp = layer_59[i][x_loc]
				y_temp = layer_59[i][y_loc]
				x_plot_59.append(x_temp)
				y_plot_59.append(y_temp)
			x_temp = layer_59[0][0]
			y_temp = layer_59[0][1]
			x_plot_59.append(x_temp)
			y_plot_59.append(y_temp)
		# ********* Ring 60 ****************
		if (layersTotal > 59):
			layer_60 = self.ONION[59]
			Len_60 = len(layer_60)
			x_plot_60 = []
			y_plot_60 = []
			for i in range(0, Len_60):
				x_temp = layer_60[i][x_loc]
				y_temp = layer_60[i][y_loc]
				x_plot_60.append(x_temp)
				y_plot_60.append(y_temp)
			x_temp = layer_60[0][0]
			y_temp = layer_60[0][1]
			x_plot_60.append(x_temp)
			y_plot_60.append(y_temp)
		# ********* Ring 61 ****************
		if (layersTotal > 60):
			layer_61 = self.ONION[60]
			Len_61 = len(layer_61)
			x_plot_61 = []
			y_plot_61 = []
			for i in range(0, Len_61):
				x_temp = layer_61[i][x_loc]
				y_temp = layer_61[i][y_loc]
				x_plot_61.append(x_temp)
				y_plot_61.append(y_temp)
			x_temp = layer_61[0][0]
			y_temp = layer_61[0][1]
			x_plot_61.append(x_temp)
			y_plot_61.append(y_temp)
		# ********* Ring 62 ****************
		if (layersTotal > 61):
			layer_62 = self.ONION[61]
			Len_62 = len(layer_62)
			x_plot_62 = []
			y_plot_62 = []
			for i in range(0, Len_62):
				x_temp = layer_62[i][x_loc]
				y_temp = layer_62[i][y_loc]
				x_plot_62.append(x_temp)
				y_plot_62.append(y_temp)
			x_temp = layer_62[0][0]
			y_temp = layer_62[0][1]
			x_plot_62.append(x_temp)
			y_plot_62.append(y_temp)


		# ********* Plot Details *******************************************************************
		# set the figure size
		plt.figure(figsize=(15, 10))
		#plt.figure(figsize=(12, 8)) 
		# plot the connected scatterplot
		# ********* Plot Details *******************************************************************

		plt.plot(x_plot_1, y_plot_1, marker='')
		if (layersTotal > 1):
			plt.plot(x_plot_2, y_plot_2, marker='.')
		if (layersTotal > 2):
			plt.plot(x_plot_3, y_plot_3, marker='.')
		if (layersTotal > 3):
			plt.plot(x_plot_4, y_plot_4, marker='.')
		if (layersTotal > 4):
			plt.plot(x_plot_5, y_plot_5, marker='.')
		if (layersTotal > 5):
			plt.plot(x_plot_6, y_plot_6, marker='.')
		if (layersTotal > 6):
			plt.plot(x_plot_7, y_plot_7, marker='.')
		if (layersTotal > 7):
			plt.plot(x_plot_8, y_plot_8, marker='.')
		if (layersTotal > 8):
			plt.plot(x_plot_9, y_plot_9, marker='.')
		if (layersTotal > 9):
			plt.plot(x_plot_10, y_plot_10, marker='.')
		if (layersTotal > 10):
			plt.plot(x_plot_11, y_plot_11, marker='.')
		if (layersTotal > 11):
			plt.plot(x_plot_12, y_plot_12, marker='.')
		if (layersTotal > 12):
			plt.plot(x_plot_13, y_plot_13, marker='.')
		if (layersTotal > 13):
			plt.plot(x_plot_14, y_plot_14, marker='.')
		if (layersTotal > 14):
			plt.plot(x_plot_15, y_plot_15, marker='.')
		if (layersTotal > 15):
			plt.plot(x_plot_16, y_plot_16, marker='.')
		if (layersTotal > 16):
			plt.plot(x_plot_17, y_plot_17, marker='.')
		if (layersTotal > 17):
			plt.plot(x_plot_18, y_plot_18, marker='.')
		if (layersTotal > 18):
			plt.plot(x_plot_19, y_plot_19, marker='.')
		if (layersTotal > 19):
			plt.plot(x_plot_20, y_plot_20, marker='.')
		if (layersTotal > 20):
			plt.plot(x_plot_21, y_plot_21, marker='.')
		if (layersTotal > 21):
			plt.plot(x_plot_22, y_plot_22, marker='.')
		if (layersTotal > 22):
			plt.plot(x_plot_23, y_plot_23, marker='.')
		if (layersTotal > 23):
			plt.plot(x_plot_24, y_plot_24, marker='.')
		if (layersTotal > 24):
			plt.plot(x_plot_25, y_plot_25, marker='.')
		if (layersTotal > 25):
			plt.plot(x_plot_26, y_plot_26, marker='.')
		if (layersTotal > 26):
			plt.plot(x_plot_27, y_plot_27, marker='.')
		if (layersTotal > 27):
			plt.plot(x_plot_28, y_plot_28, marker='.')
		if (layersTotal > 28):
			plt.plot(x_plot_29, y_plot_29, marker='.')
		if (layersTotal > 29):
			plt.plot(x_plot_30, y_plot_30, marker='.')
		if (layersTotal > 30):
			plt.plot(x_plot_31, y_plot_31, marker='.')
		if (layersTotal > 31):
			plt.plot(x_plot_32, y_plot_32, marker='.')
		if (layersTotal > 32):
			plt.plot(x_plot_33, y_plot_33, marker='.')
		if (layersTotal > 33):
			plt.plot(x_plot_34, y_plot_34, marker='.')
		if (layersTotal > 34):
			plt.plot(x_plot_35, y_plot_35, marker='.')
		if (layersTotal > 35):
			plt.plot(x_plot_36, y_plot_36, marker='.')
		if (layersTotal > 36):
			plt.plot(x_plot_37, y_plot_37, marker='.')
		if (layersTotal > 37):
			plt.plot(x_plot_38, y_plot_38, marker='.')
		if (layersTotal > 38):
			plt.plot(x_plot_39, y_plot_39, marker='.')
		if (layersTotal > 39):
			plt.plot(x_plot_40, y_plot_40, marker='.')
		if (layersTotal > 40):
			plt.plot(x_plot_41, y_plot_41, marker='.')
		if (layersTotal > 41):
			plt.plot(x_plot_42, y_plot_42, marker='.')
		if (layersTotal > 42):
			plt.plot(x_plot_43, y_plot_43, marker='.')
		if (layersTotal > 43):
			plt.plot(x_plot_44, y_plot_44, marker='.')
		if (layersTotal > 44):
			plt.plot(x_plot_45, y_plot_45, marker='.')
		if (layersTotal > 45):
			plt.plot(x_plot_46, y_plot_46, marker='.')
		if (layersTotal > 46):
			plt.plot(x_plot_47, y_plot_47, marker='.')
		if (layersTotal > 47):
			plt.plot(x_plot_48, y_plot_48, marker='.')
		if (layersTotal > 48):
			plt.plot(x_plot_49, y_plot_49, marker='.')
		if (layersTotal > 49):
			plt.plot(x_plot_50, y_plot_50, marker='.')
		if (layersTotal > 50):
			plt.plot(x_plot_51, y_plot_51, marker='.')
		if (layersTotal > 51):
			plt.plot(x_plot_52, y_plot_52, marker='.')
		if (layersTotal > 52):
			plt.plot(x_plot_53, y_plot_53, marker='.')
		if (layersTotal > 53):
			plt.plot(x_plot_54, y_plot_54, marker='.')
		if (layersTotal > 54):
			plt.plot(x_plot_55, y_plot_55, marker='.')
		if (layersTotal > 55):
			plt.plot(x_plot_56, y_plot_56, marker='.')
		if (layersTotal > 56):
			plt.plot(x_plot_57, y_plot_57, marker='.')
		if (layersTotal > 57):
			plt.plot(x_plot_58, y_plot_58, marker='.')
		if (layersTotal > 58):
			plt.plot(x_plot_59, y_plot_59, marker='.')
		if (layersTotal > 59):
			plt.plot(x_plot_60, y_plot_60, marker='.')
		if (layersTotal > 60):
			plt.plot(x_plot_61, y_plot_61, marker='.')
		if (layersTotal > 61):
			plt.plot(x_plot_62, y_plot_62, marker='.')
            

		plt.title('Convex Nested Hulls', fontsize=16)       
		# x axis label
		plt.xlabel('X-axis', fontsize=12)
		# y axis label
		plt.ylabel('Y-axis', fontsize=12)
		# show the graph
		plt.show()