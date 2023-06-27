import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
# THIS Is steeeuuu000ooopid. write an algo to automate!   embarassing
# I say that everytime i go to update THIS

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
		# ********* Ring 63 *****************
		if (layersTotal > 62):
			layer_63 = self.ONION[62]
			Len_63 = len(layer_40)
			x_plot_63 = []
			y_plot_63 = []
			for i in range(0, Len_63):
				x_temp = layer_63[i][x_loc]
				y_temp = layer_63[i][y_loc]
				x_plot_63.append(x_temp)
				y_plot_63.append(y_temp)
			x_temp = layer_63[0][0]
			y_temp = layer_63[0][1]
			x_plot_63.append(x_temp)
			y_plot_63.append(y_temp)
		# ********* Ring 64 ****************
		if (layersTotal > 63):
			layer_64 = self.ONION[63]
			Len_64 = len(layer_64)
			x_plot_64 = []
			y_plot_64 = []
			for i in range(0, Len_64):
				x_temp = layer_64[i][x_loc]
				y_temp = layer_64[i][y_loc]
				x_plot_64.append(x_temp)
				y_plot_64.append(y_temp)
			x_temp = layer_64[0][0]
			y_temp = layer_64[0][1]
			x_plot_64.append(x_temp)
			y_plot_64.append(y_temp)
		# ********* Ring 65 ****************
		if (layersTotal > 64):
			layer_65 = self.ONION[64]
			Len_65 = len(layer_65)
			x_plot_65 = []
			y_plot_65 = []
			for i in range(0, Len_65):
				x_temp = layer_65[i][x_loc]
				y_temp = layer_65[i][y_loc]
				x_plot_65.append(x_temp)
				y_plot_65.append(y_temp)
			x_temp = layer_65[0][0]
			y_temp = layer_65[0][1]
			x_plot_65.append(x_temp)
			y_plot_65.append(y_temp)
		# ********* Ring 66 ****************
		if (layersTotal > 65):
			layer_66 = self.ONION[65]
			Len_66 = len(layer_66)
			x_plot_66 = []
			y_plot_66 = []
			for i in range(0, Len_66):
				x_temp = layer_66[i][x_loc]
				y_temp = layer_66[i][y_loc]
				x_plot_66.append(x_temp)
				y_plot_66.append(y_temp)
			x_temp = layer_66[0][0]
			y_temp = layer_66[0][1]
			x_plot_66.append(x_temp)
			y_plot_66.append(y_temp)
		# ********* Ring 67 ****************
		if (layersTotal > 66):
			layer_67 = self.ONION[66]
			Len_67 = len(layer_67)
			x_plot_67 = []
			y_plot_67 = []
			for i in range(0, Len_67):
				x_temp = layer_67[i][x_loc]
				y_temp = layer_67[i][y_loc]
				x_plot_67.append(x_temp)
				y_plot_67.append(y_temp)
			x_temp = layer_67[0][0]
			y_temp = layer_67[0][1]
			x_plot_67.append(x_temp)
			y_plot_67.append(y_temp)
		# ********* Ring 68 ****************
		if (layersTotal > 67):
			layer_68 = self.ONION[67]
			Len_68 = len(layer_68)
			x_plot_68 = []
			y_plot_68 = []
			for i in range(0, Len_68):
				x_temp = layer_68[i][x_loc]
				y_temp = layer_68[i][y_loc]
				x_plot_68.append(x_temp)
				y_plot_68.append(y_temp)
			x_temp = layer_68[0][0]
			y_temp = layer_68[0][1]
			x_plot_68.append(x_temp)
			y_plot_68.append(y_temp)
		# ********* Ring 69 ****************
		if (layersTotal > 68):
			layer_69 = self.ONION[68]
			Len_69 = len(layer_69)
			x_plot_69 = []
			y_plot_69 = []
			for i in range(0, Len_69):
				x_temp = layer_69[i][x_loc]
				y_temp = layer_69[i][y_loc]
				x_plot_69.append(x_temp)
				y_plot_69.append(y_temp)
			x_temp = layer_69[0][0]
			y_temp = layer_69[0][1]
			x_plot_69.append(x_temp)
			y_plot_69.append(y_temp)
		# ********* Ring 70 ****************
		if (layersTotal > 69):
			layer_70 = self.ONION[70]
			Len_70 = len(layer_47)
			x_plot_70 = []
			y_plot_70 = []
			for i in range(0, Len_70):
				x_temp = layer_70[i][x_loc]
				y_temp = layer_70[i][y_loc]
				x_plot_70.append(x_temp)
				y_plot_70.append(y_temp)
			x_temp = layer_70[0][0]
			y_temp = layer_70[0][1]
			x_plot_70.append(x_temp)
			y_plot_70.append(y_temp)
		# ********* Ring 71 ****************
		if (layersTotal > 70):
			layer_71 = self.ONION[70]
			Len_71 = len(layer_71)
			x_plot_71 = []
			y_plot_71 = []
			for i in range(0, Len_71):
				x_temp = layer_71[i][x_loc]
				y_temp = layer_71[i][y_loc]
				x_plot_71.append(x_temp)
				y_plot_71.append(y_temp)
			x_temp = layer_71[0][0]
			y_temp = layer_71[0][1]
			x_plot_71.append(x_temp)
			y_plot_71.append(y_temp)
		# ********* Ring 72 ****************
		if (layersTotal > 71):
			layer_72 = self.ONION[71]
			Len_72 = len(layer_72)
			x_plot_72 = []
			y_plot_72 = []
			for i in range(0, Len_72):
				x_temp = layer_72[i][x_loc]
				y_temp = layer_72[i][y_loc]
				x_plot_72.append(x_temp)
				y_plot_72.append(y_temp)
			x_temp = layer_72[0][0]
			y_temp = layer_72[0][1]
			x_plot_72.append(x_temp)
			y_plot_72.append(y_temp)
		# ********* Ring 73 ****************
		if (layersTotal > 72):
			layer_73 = self.ONION[72]
			Len_73 = len(layer_73)
			x_plot_73 = []
			y_plot_73 = []
			for i in range(0, Len_73):
				x_temp = layer_73[i][x_loc]
				y_temp = layer_73[i][y_loc]
				x_plot_73.append(x_temp)
				y_plot_73.append(y_temp)
			x_temp = layer_73[0][0]
			y_temp = layer_73[0][1]
			x_plot_73.append(x_temp)
			y_plot_73.append(y_temp)
		# ********* Ring 74 ****************
		if (layersTotal > 73):
			layer_74 = self.ONION[73]
			Len_74 = len(layer_74)
			x_plot_74 = []
			y_plot_74 = []
			for i in range(0, Len_74):
				x_temp = layer_74[i][x_loc]
				y_temp = layer_74[i][y_loc]
				x_plot_74.append(x_temp)
				y_plot_74.append(y_temp)
			x_temp = layer_74[0][0]
			y_temp = layer_74[0][1]
			x_plot_74.append(x_temp)
			y_plot_74.append(y_temp)
		# ********* Ring 75 ****************
		if (layersTotal > 74):
			layer_75 = self.ONION[74]
			Len_75 = len(layer_75)
			x_plot_75 = []
			y_plot_75 = []
			for i in range(0, Len_75):
				x_temp = layer_75[i][x_loc]
				y_temp = layer_75[i][y_loc]
				x_plot_75.append(x_temp)
				y_plot_75.append(y_temp)
			x_temp = layer_75[0][0]
			y_temp = layer_75[0][1]
			x_plot_75.append(x_temp)
			y_plot_75.append(y_temp)
		# ********* Ring 76 ****************
		if (layersTotal > 75):
			layer_76 = self.ONION[75]
			Len_76 = len(layer_76)
			x_plot_76 = []
			y_plot_76 = []
			for i in range(0, Len_76):
				x_temp = layer_76[i][x_loc]
				y_temp = layer_76[i][y_loc]
				x_plot_76.append(x_temp)
				y_plot_76.append(y_temp)
			x_temp = layer_76[0][0]
			y_temp = layer_76[0][1]
			x_plot_76.append(x_temp)
			y_plot_76.append(y_temp)
		# ********* Ring 77 ****************
		if (layersTotal > 76):
			layer_77 = self.ONION[76]
			Len_77 = len(layer_77)
			x_plot_77 = []
			y_plot_77 = []
			for i in range(0, Len_54):
				x_temp = layer_54[i][x_loc]
				y_temp = layer_54[i][y_loc]
				x_plot_54.append(x_temp)
				y_plot_54.append(y_temp)
			x_temp = layer_54[0][0]
			y_temp = layer_54[0][1]
			x_plot_54.append(x_temp)
			y_plot_54.append(y_temp)
		# ********* Ring 78 ****************
		if (layersTotal > 77):
			layer_78 = self.ONION[77]
			Len_78 = len(layer_78)
			x_plot_78 = []
			y_plot_78 = []
			for i in range(0, Len_78):
				x_temp = layer_78[i][x_loc]
				y_temp = layer_78[i][y_loc]
				x_plot_78.append(x_temp)
				y_plot_78.append(y_temp)
			x_temp = layer_78[0][0]
			y_temp = layer_78[0][1]
			x_plot_78.append(x_temp)
			y_plot_78.append(y_temp)
		# ********* Ring 79 ****************
		if (layersTotal > 78):
			layer_79 = self.ONION[78]
			Len_79 = len(layer_79)
			x_plot_79 = []
			y_plot_79 = []
			for i in range(0, Len_79):
				x_temp = layer_79[i][x_loc]
				y_temp = layer_79[i][y_loc]
				x_plot_79.append(x_temp)
				y_plot_79.append(y_temp)
			x_temp = layer_79[0][0]
			y_temp = layer_79[0][1]
			x_plot_79.append(x_temp)
			y_plot_79.append(y_temp)
		# ********* Ring 80 ****************
		if (layersTotal > 79):
			layer_80 = self.ONION[79]
			Len_80 = len(layer_80)
			x_plot_80 = []
			y_plot_80 = []
			for i in range(0, Len_80):
				x_temp = layer_80[i][x_loc]
				y_temp = layer_80[i][y_loc]
				x_plot_80.append(x_temp)
				y_plot_80.append(y_temp)
			x_temp = layer_80[0][0]
			y_temp = layer_80[0][1]
			x_plot_80.append(x_temp)
			y_plot_80.append(y_temp)
		# ********* Ring 81 ****************
		if (layersTotal > 80):
			layer_81 = self.ONION[80]
			Len_81 = len(layer_81)
			x_plot_81 = []
			y_plot_81 = []
			for i in range(0, Len_81):
				x_temp = layer_81[i][x_loc]
				y_temp = layer_81[i][y_loc]
				x_plot_81.append(x_temp)
				y_plot_81.append(y_temp)
			x_temp = layer_81[0][0]
			y_temp = layer_81[0][1]
			x_plot_81.append(x_temp)
			y_plot_81.append(y_temp)
		# ********* Ring 82 ****************
		if (layersTotal > 81):
			layer_82 = self.ONION[81]
			Len_82 = len(layer_82)
			x_plot_82 = []
			y_plot_82 = []
			for i in range(0, Len_82):
				x_temp = layer_82[i][x_loc]
				y_temp = layer_82[i][y_loc]
				x_plot_82.append(x_temp)
				y_plot_82.append(y_temp)
			x_temp = layer_82[0][0]
			y_temp = layer_82[0][1]
			x_plot_82.append(x_temp)
			y_plot_82.append(y_temp)
		# ********* Ring 83 ****************
		if (layersTotal > 82):
			layer_83 = self.ONION[82]
			Len_83 = len(layer_83)
			x_plot_83 = []
			y_plot_83 = []
			for i in range(0, Len_83):
				x_temp = layer_83[i][x_loc]
				y_temp = layer_83[i][y_loc]
				x_plot_83.append(x_temp)
				y_plot_83.append(y_temp)
			x_temp = layer_83[0][0]
			y_temp = layer_83[0][1]
			x_plot_83.append(x_temp)
			y_plot_83.append(y_temp)
		# ********* Ring 84 ****************
		if (layersTotal > 83):
			layer_84 = self.ONION[83]
			Len_84 = len(layer_84)
			x_plot_84 = []
			y_plot_84 = []
			for i in range(0, Len_84):
				x_temp = layer_84[i][x_loc]
				y_temp = layer_84[i][y_loc]
				x_plot_84.append(x_temp)
				y_plot_84.append(y_temp)
			x_temp = layer_84[0][0]
			y_temp = layer_84[0][1]
			x_plot_84.append(x_temp)
			y_plot_84.append(y_temp)
		# ********* Ring 85 ****************
		if (layersTotal > 84):
			layer_85 = self.ONION[84]
			Len_85 = len(layer_85)
			x_plot_85 = []
			y_plot_85 = []
			for i in range(0, Len_85):
				x_temp = layer_85[i][x_loc]
				y_temp = layer_85[i][y_loc]
				x_plot_85.append(x_temp)
				y_plot_85.append(y_temp)
			x_temp = layer_85[0][0]
			y_temp = layer_85[0][1]
			x_plot_85.append(x_temp)
			y_plot_85.append(y_temp)
		# ********* Ring 86 ******************
		if (layersTotal > 85):
			layer_86 = self.ONION[85]
			Len_86 = len(layer_86)
			x_plot_86 = []
			y_plot_86 = []
			for i in range(0, Len_86):
				x_temp = layer_86[i][x_loc]
				y_temp = layer_86[i][y_loc]
				x_plot_86.append(x_temp)
				y_plot_86.append(y_temp)
			x_temp = layer_86[0][0]
			y_temp = layer_86[0][1]
			x_plot_86.append(x_temp)
			y_plot_86.append(y_temp)
		# ********* Ring 87 ****************
		if (layersTotal > 86):
			layer_87 = self.ONION[86]
			Len_87 = len(layer_87)
			x_plot_87 = []
			y_plot_87 = []
			for i in range(0, Len_87):
				x_temp = layer_87[i][x_loc]
				y_temp = layer_87[i][y_loc]
				x_plot_87.append(x_temp)
				y_plot_87.append(y_temp)
			x_temp = layer_87[0][0]
			y_temp = layer_87[0][1]
			x_plot_87.append(x_temp)
			y_plot_87.append(y_temp)
		# ********* Ring 88 ****************
		if (layersTotal > 87):
			layer_88 = self.ONION[87]
			Len_88 = len(layer_88)
			x_plot_88 = []
			y_plot_88 = []
			for i in range(0, Len_88):
				x_temp = layer_88[i][x_loc]
				y_temp = layer_88[i][y_loc]
				x_plot_88.append(x_temp)
				y_plot_88.append(y_temp)
			x_temp = layer_88[0][0]
			y_temp = layer_88[0][1]
			x_plot_88.append(x_temp)
			y_plot_88.append(y_temp)
		# ********* Ring 89 ****************
		if (layersTotal > 88):
			layer_89 = self.ONION[88]
			Len_89 = len(layer_89)
			x_plot_89 = []
			y_plot_89 = []
			for i in range(0, Len_89):
				x_temp = layer_89[i][x_loc]
				y_temp = layer_89[i][y_loc]
				x_plot_89.append(x_temp)
				y_plot_89.append(y_temp)
			x_temp = layer_89[0][0]
			y_temp = layer_89[0][1]
			x_plot_89.append(x_temp)
			y_plot_89.append(y_temp)
		# ********* Ring 90 ****************
		if (layersTotal > 89):
			layer_90 = self.ONION[89]
			Len_90 = len(layer_90)
			x_plot_90 = []
			y_plot_90 = []
			for i in range(0, Len_90):
				x_temp = layer_90[i][x_loc]
				y_temp = layer_90[i][y_loc]
				x_plot_90.append(x_temp)
				y_plot_90.append(y_temp)
			x_temp = layer_90[0][0]
			y_temp = layer_90[0][1]
			x_plot_90.append(x_temp)
			y_plot_90.append(y_temp)
		# ********* Ring 91 ****************
		if (layersTotal > 90):
			layer_91 = self.ONION[90]
			Len_91 = len(layer_91)
			x_plot_91 = []
			y_plot_91 = []
			for i in range(0, Len_91):
				x_temp = layer_91[i][x_loc]
				y_temp = layer_91[i][y_loc]
				x_plot_91.append(x_temp)
				y_plot_91.append(y_temp)
			x_temp = layer_91[0][0]
			y_temp = layer_91[0][1]
			x_plot_91.append(x_temp)
			y_plot_91.append(y_temp)
		# ********* Ring 92 ****************
		if (layersTotal > 91):
			layer_92 = self.ONION[91]
			Len_92 = len(layer_92)
			x_plot_92 = []
			y_plot_92 = []
			for i in range(0, Len_92):
				x_temp = layer_92[i][x_loc]
				y_temp = layer_92[i][y_loc]
				x_plot_92.append(x_temp)
				y_plot_92.append(y_temp)
			x_temp = layer_92[0][0]
			y_temp = layer_92[0][1]
			x_plot_92.append(x_temp)
			y_plot_92.append(y_temp)
		# ********* Ring 93 ****************
		if (layersTotal > 92):
			layer_93 = self.ONION[92]
			Len_93 = len(layer_93)
			x_plot_93 = []
			y_plot_93 = []
			for i in range(0, Len_93):
				x_temp = layer_93[i][x_loc]
				y_temp = layer_93[i][y_loc]
				x_plot_93.append(x_temp)
				y_plot_93.append(y_temp)
			x_temp = layer_93[0][0]
			y_temp = layer_93[0][1]
			x_plot_93.append(x_temp)
			y_plot_93.append(y_temp)
		# ********* Ring 94 ****************
		if (layersTotal > 93):
			layer_94 = self.ONION[93]
			Len_94 = len(layer_94)
			x_plot_94 = []
			y_plot_94 = []
			for i in range(0, Len_94):
				x_temp = layer_94[i][x_loc]
				y_temp = layer_94[i][y_loc]
				x_plot_94.append(x_temp)
				y_plot_94.append(y_temp)
			x_temp = layer_94[0][0]
			y_temp = layer_94[0][1]
			x_plot_94.append(x_temp)
			y_plot_94.append(y_temp)
		# ********* Ring 95 ****************
		if (layersTotal > 94):
			layer_95 = self.ONION[94]
			Len_95 = len(layer_95)
			x_plot_95 = []
			y_plot_95 = []
			for i in range(0, Len_95):
				x_temp = layer_95[i][x_loc]
				y_temp = layer_95[i][y_loc]
				x_plot_95.append(x_temp)
				y_plot_95.append(y_temp)
			x_temp = layer_95[0][0]
			y_temp = layer_95[0][1]
			x_plot_95.append(x_temp)
			y_plot_95.append(y_temp)
		# ********* Ring 96 ****************
		if (layersTotal > 95):
			layer_96 = self.ONION[95]
			Len_96 = len(layer_96)
			x_plot_96 = []
			y_plot_96 = []
			for i in range(0, Len_96):
				x_temp = layer_96[i][x_loc]
				y_temp = layer_96[i][y_loc]
				x_plot_96.append(x_temp)
				y_plot_96.append(y_temp)
			x_temp = layer_96[0][0]
			y_temp = layer_96[0][1]
			x_plot_96.append(x_temp)
			y_plot_96.append(y_temp)
		# ********* Ring 97 ****************
		if (layersTotal > 96):
			layer_97 = self.ONION[96]
			Len_97 = len(layer_97)
			x_plot_97 = []
			y_plot_97 = []
			for i in range(0, Len_97):
				x_temp = layer_97[i][x_loc]
				y_temp = layer_97[i][y_loc]
				x_plot_97.append(x_temp)
				y_plot_97.append(y_temp)
			x_temp = layer_97[0][0]
			y_temp = layer_97[0][1]
			x_plot_97.append(x_temp)
			y_plot_97.append(y_temp)
		# ********* Ring 98 ****************
		if (layersTotal > 97):
			layer_98 = self.ONION[97]
			Len_98 = len(layer_98)
			x_plot_98 = []
			y_plot_98 = []
			for i in range(0, Len_98):
				x_temp = layer_98[i][x_loc]
				y_temp = layer_98[i][y_loc]
				x_plot_98.append(x_temp)
				y_plot_98.append(y_temp)
			x_temp = layer_98[0][0]
			y_temp = layer_98[0][1]
			x_plot_98.append(x_temp)
			y_plot_98.append(y_temp)
		# ********* Ring 99 ****************
		if (layersTotal > 98):
			layer_99 = self.ONION[98]
			Len_99 = len(layer_99)
			x_plot_99 = []
			y_plot_99 = []
			for i in range(0, Len_99):
				x_temp = layer_99[i][x_loc]
				y_temp = layer_99[i][y_loc]
				x_plot_99.append(x_temp)
				y_plot_99.append(y_temp)
			x_temp = layer_99[0][0]
			y_temp = layer_99[0][1]
			x_plot_99.append(x_temp)
			y_plot_99.append(y_temp)
		# ********* Ring 100 ****************
		if (layersTotal > 99):
			layer_100 = self.ONION[99]
			Len_100 = len(layer_100)
			x_plot_100 = []
			y_plot_100 = []
			for i in range(0, Len_100):
				x_temp = layer_100[i][x_loc]
				y_temp = layer_100[i][y_loc]
				x_plot_100.append(x_temp)
				y_plot_100.append(y_temp)
			x_temp = layer_100[0][0]
			y_temp = layer_100[0][1]
			x_plot_100.append(x_temp)
			y_plot_100.append(y_temp)
		# ********* Ring 101 ****************
		if (layersTotal > 100):
			layer_101 = self.ONION[100]
			Len_101 = len(layer_101)
			x_plot_101 = []
			y_plot_101 = []
			for i in range(0, Len_101):
				x_temp = layer_101[i][x_loc]
				y_temp = layer_101[i][y_loc]
				x_plot_101.append(x_temp)
				y_plot_101.append(y_temp)
			x_temp = layer_101[0][0]
			y_temp = layer_101[0][1]
			x_plot_101.append(x_temp)
			y_plot_101.append(y_temp)
		# ********* Ring 102 ****************
		if (layersTotal > 101):
			layer_102 = self.ONION[101]
			Len_102 = len(layer_102)
			x_plot_102 = []
			y_plot_102 = []
			for i in range(0, Len_102):
				x_temp = layer_102[i][x_loc]
				y_temp = layer_102[i][y_loc]
				x_plot_102.append(x_temp)
				y_plot_102.append(y_temp)
			x_temp = layer_102[0][0]
			y_temp = layer_102[0][1]
			x_plot_102.append(x_temp)
			y_plot_102.append(y_temp)
		# ********* Ring 103 ****************
		if (layersTotal > 102):
			layer_103 = self.ONION[102]
			Len_103 = len(layer_103)
			x_plot_103 = []
			y_plot_103 = []
			for i in range(0, Len_103):
				x_temp = layer_103[i][x_loc]
				y_temp = layer_103[i][y_loc]
				x_plot_103.append(x_temp)
				y_plot_103.append(y_temp)
			x_temp = layer_103[0][0]
			y_temp = layer_103[0][1]
			x_plot_103.append(x_temp)
			y_plot_103.append(y_temp)
		# ********* Ring 104 ****************
		if (layersTotal > 103):
			layer_104 = self.ONION[103]
			Len_104 = len(layer_104)
			x_plot_104 = []
			y_plot_104 = []
			for i in range(0, Len_104):
				x_temp = layer_104[i][x_loc]
				y_temp = layer_104[i][y_loc]
				x_plot_104.append(x_temp)
				y_plot_104.append(y_temp)
			x_temp = layer_104[0][0]
			y_temp = layer_104[0][1]
			x_plot_104.append(x_temp)
			y_plot_104.append(y_temp)
		# ********* Ring 105 ****************
		if (layersTotal > 104):
			layer_105 = self.ONION[104]
			Len_105 = len(layer_105)
			x_plot_105 = []
			y_plot_105 = []
			for i in range(0, Len_105):
				x_temp = layer_105[i][x_loc]
				y_temp = layer_105[i][y_loc]
				x_plot_105.append(x_temp)
				y_plot_105.append(y_temp)
			x_temp = layer_105[0][0]
			y_temp = layer_105[0][1]
			x_plot_105.append(x_temp)
			y_plot_105.append(y_temp)
		# ********* Ring 106 ****************
		if (layersTotal > 105):
			layer_106 = self.ONION[105]
			Len_106 = len(layer_106)
			x_plot_106 = []
			y_plot_106 = []
			for i in range(0, Len_106):
				x_temp = layer_106[i][x_loc]
				y_temp = layer_106[i][y_loc]
				x_plot_106.append(x_temp)
				y_plot_106.append(y_temp)
			x_temp = layer_106[0][0]
			y_temp = layer_106[0][1]
			x_plot_106.append(x_temp)
			y_plot_106.append(y_temp)
		# ********* Ring 107 ****************
		if (layersTotal > 106):
			layer_107 = self.ONION[106]
			Len_107 = len(layer_107)
			x_plot_107 = []
			y_plot_107 = []
			for i in range(0, Len_107):
				x_temp = layer_107[i][x_loc]
				y_temp = layer_107[i][y_loc]
				x_plot_107.append(x_temp)
				y_plot_107.append(y_temp)
			x_temp = layer_107[0][0]
			y_temp = layer_107[0][1]
			x_plot_107.append(x_temp)
			y_plot_107.append(y_temp)
		# ********* Ring 108 ****************
		if (layersTotal > 107):
			layer_108 = self.ONION[107]
			Len_108 = len(layer_62)
			x_plot_108 = []
			y_plot_108 = []
			for i in range(0, Len_108):
				x_temp = layer_108[i][x_loc]
				y_temp = layer_108[i][y_loc]
				x_plot_108.append(x_temp)
				y_plot_108.append(y_temp)
			x_temp = layer_108[0][0]
			y_temp = layer_108[0][1]
			x_plot_108.append(x_temp)
			y_plot_108.append(y_temp)
		# ********* Ring 109 ******************
		if (layersTotal > 108):
			layer_109 = self.ONION[108]
			Len_109 = len(layer_109)
			x_plot_109 = []
			y_plot_109 = []
			for i in range(0, Len_109):
				x_temp = layer_109[i][x_loc]
				y_temp = layer_109[i][y_loc]
				x_plot_109.append(x_temp)
				y_plot_109.append(y_temp)
			x_temp = layer_109[0][0]
			y_temp = layer_109[0][1]
			x_plot_109.append(x_temp)
			y_plot_109.append(y_temp)
		# ********* Ring 110 ****************
		if (layersTotal > 109):
			layer_110 = self.ONION[109]
			Len_110 = len(layer_110)
			x_plot_110 = []
			y_plot_110 = []
			for i in range(0, Len_110):
				x_temp = layer_110[i][x_loc]
				y_temp = layer_110[i][y_loc]
				x_plot_110.append(x_temp)
				y_plot_110.append(y_temp)
			x_temp = layer_110[0][0]
			y_temp = layer_110[0][1]
			x_plot_110.append(x_temp)
			y_plot_110.append(y_temp)
		# ********* Ring 111 ****************
		if (layersTotal > 110):
			layer_111 = self.ONION[110]
			Len_111 = len(layer_111)
			x_plot_111 = []
			y_plot_111 = []
			for i in range(0, Len_111):
				x_temp = layer_111[i][x_loc]
				y_temp = layer_111[i][y_loc]
				x_plot_111.append(x_temp)
				y_plot_111.append(y_temp)
			x_temp = layer_111[0][0]
			y_temp = layer_111[0][1]
			x_plot_111.append(x_temp)
			y_plot_111.append(y_temp)
		# ********* Ring 112 ****************
		if (layersTotal > 111):
			layer_112 = self.ONION[111]
			Len_112 = len(layer_112)
			x_plot_112 = []
			y_plot_112 = []
			for i in range(0, Len_112):
				x_temp = layer_112[i][x_loc]
				y_temp = layer_112[i][y_loc]
				x_plot_112.append(x_temp)
				y_plot_112.append(y_temp)
			x_temp = layer_112[0][0]
			y_temp = layer_112[0][1]
			x_plot_112.append(x_temp)
			y_plot_112.append(y_temp)
		# ********* Ring 113 ****************
		if (layersTotal > 112):
			layer_113 = self.ONION[112]
			Len_113 = len(layer_113)
			x_plot_113 = []
			y_plot_113 = []
			for i in range(0, Len_113):
				x_temp = layer_113[i][x_loc]
				y_temp = layer_113[i][y_loc]
				x_plot_113.append(x_temp)
				y_plot_113.append(y_temp)
			x_temp = layer_113[0][0]
			y_temp = layer_113[0][1]
			x_plot_113.append(x_temp)
			y_plot_113.append(y_temp)
		# ********* Ring 114 ****************
		if (layersTotal > 113):
			layer_114 = self.ONION[113]
			Len_114 = len(layer_114)
			x_plot_114 = []
			y_plot_114 = []
			for i in range(0, Len_114):
				x_temp = layer_114[i][x_loc]
				y_temp = layer_114[i][y_loc]
				x_plot_114.append(x_temp)
				y_plot_114.append(y_temp)
			x_temp = layer_114[0][0]
			y_temp = layer_114[0][1]
			x_plot_114.append(x_temp)
			y_plot_114.append(y_temp)
		# ********* Ring 115 ****************
		if (layersTotal > 114):
			layer_115 = self.ONION[114]
			Len_115 = len(layer_115)
			x_plot_115 = []
			y_plot_115 = []
			for i in range(0, Len_115):
				x_temp = layer_115[i][x_loc]
				y_temp = layer_115[i][y_loc]
				x_plot_115.append(x_temp)
				y_plot_115.append(y_temp)
			x_temp = layer_115[0][0]
			y_temp = layer_115[0][1]
			x_plot_115.append(x_temp)
			y_plot_115.append(y_temp)
		# ********* Ring 116 ****************
		if (layersTotal > 115):
			layer_116 = self.ONION[115]
			Len_116 = len(layer_116)
			x_plot_116 = []
			y_plot_116 = []
			for i in range(0, Len_116):
				x_temp = layer_116[i][x_loc]
				y_temp = layer_116[i][y_loc]
				x_plot_116.append(x_temp)
				y_plot_116.append(y_temp)
			x_temp = layer_116[0][0]
			y_temp = layer_116[0][1]
			x_plot_116.append(x_temp)
			y_plot_116.append(y_temp)
		# ********* Ring 117 ****************
		if (layersTotal > 116):
			layer_117 = self.ONION[116]
			Len_117 = len(layer_117)
			x_plot_117 = []
			y_plot_117 = []
			for i in range(0, Len_117):
				x_temp = layer_117[i][x_loc]
				y_temp = layer_117[i][y_loc]
				x_plot_117.append(x_temp)
				y_plot_117.append(y_temp)
			x_temp = layer_117[0][0]
			y_temp = layer_117[0][1]
			x_plot_117.append(x_temp)
			y_plot_117.append(y_temp)
		# ********* Ring 118 ****************
		if (layersTotal > 117):
			layer_118 = self.ONION[117]
			Len_118 = len(layer_118)
			x_plot_118 = []
			y_plot_118 = []
			for i in range(0, Len_118):
				x_temp = layer_118[i][x_loc]
				y_temp = layer_118[i][y_loc]
				x_plot_118.append(x_temp)
				y_plot_118.append(y_temp)
			x_temp = layer_118[0][0]
			y_temp = layer_118[0][1]
			x_plot_118.append(x_temp)
			y_plot_118.append(y_temp)
		# ********* Ring 119 ****************
		if (layersTotal > 118):
			layer_119 = self.ONION[118]
			Len_119 = len(layer_119)
			x_plot_119 = []
			y_plot_119 = []
			for i in range(0, Len_119):
				x_temp = layer_119[i][x_loc]
				y_temp = layer_119[i][y_loc]
				x_plot_119.append(x_temp)
				y_plot_119.append(y_temp)
			x_temp = layer_119[0][0]
			y_temp = layer_119[0][1]
			x_plot_119.append(x_temp)
			y_plot_119.append(y_temp)
		# ********* Ring 120 ****************
		if (layersTotal > 119):
			layer_120 = self.ONION[119]
			Len_120 = len(layer_120)
			x_plot_120 = []
			y_plot_120 = []
			for i in range(0, Len_120):
				x_temp = layer_120[i][x_loc]
				y_temp = layer_120[i][y_loc]
				x_plot_120.append(x_temp)
				y_plot_120.append(y_temp)
			x_temp = layer_120[0][0]
			y_temp = layer_120[0][1]
			x_plot_120.append(x_temp)
			y_plot_120.append(y_temp)
		# ********* Ring 121 ****************
		if (layersTotal > 120):
			layer_121 = self.ONION[120]
			Len_121 = len(layer_121)
			x_plot_121 = []
			y_plot_121 = []
			for i in range(0, Len_121):
				x_temp = layer_121[i][x_loc]
				y_temp = layer_121[i][y_loc]
				x_plot_121.append(x_temp)
				y_plot_121.append(y_temp)
			x_temp = layer_121[0][0]
			y_temp = layer_121[0][1]
			x_plot_121.append(x_temp)
			y_plot_121.append(y_temp)
		# ********* Ring 122 ****************
		if (layersTotal > 121):
			layer_122 = self.ONION[121]
			Len_122 = len(layer_122)
			x_plot_122 = []
			y_plot_122 = []
			for i in range(0, Len_122):
				x_temp = layer_122[i][x_loc]
				y_temp = layer_122[i][y_loc]
				x_plot_122.append(x_temp)
				y_plot_122.append(y_temp)
			x_temp = layer_122[0][0]
			y_temp = layer_122[0][1]
			x_plot_122.append(x_temp)
			y_plot_122.append(y_temp)
		# ********* Ring 123 ****************
		if (layersTotal > 122):
			layer_123 = self.ONION[122]
			Len_123 = len(layer_123)
			x_plot_123 = []
			y_plot_123 = []
			for i in range(0, Len_123):
				x_temp = layer_123[i][x_loc]
				y_temp = layer_123[i][y_loc]
				x_plot_123.append(x_temp)
				y_plot_123.append(y_temp)
			x_temp = layer_123[0][0]
			y_temp = layer_123[0][1]
			x_plot_123.append(x_temp)
			y_plot_123.append(y_temp)
		# ********* Ring 124 ****************
		if (layersTotal > 123):
			layer_124 = self.ONION[123]
			Len_124 = len(layer_124)
			x_plot_124 = []
			y_plot_124 = []
			for i in range(0, Len_124):
				x_temp = layer_124[i][x_loc]
				y_temp = layer_124[i][y_loc]
				x_plot_124.append(x_temp)
				y_plot_124.append(y_temp)
			x_temp = layer_124[0][0]
			y_temp = layer_124[0][1]
			x_plot_124.append(x_temp)
			y_plot_124.append(y_temp)
		# ********* Ring 125 ****************
		if (layersTotal > 124):
			layer_125 = self.ONION[24]
			Len_125 = len(layer_125)
			x_plot_125 = []
			y_plot_125 = []
			for i in range(0, Len_125):
				x_temp = layer_125[i][x_loc]
				y_temp = layer_125[i][y_loc]
				x_plot_125.append(x_temp)
				y_plot_125.append(y_temp)
			x_temp = layer_125[0][0]
			y_temp = layer_125[0][1]
			x_plot_125.append(x_temp)
			y_plot_125.append(y_temp)
		# ********* Ring 126 ****************
		if (layersTotal > 125):
			layer_126 = self.ONION[125]
			Len_126 = len(layer_126)
			x_plot_126 = []
			y_plot_126 = []
			for i in range(0, Len_126):
				x_temp = layer_126[i][x_loc]
				y_temp = layer_126[i][y_loc]
				x_plot_126.append(x_temp)
				y_plot_126.append(y_temp)
			x_temp = layer_126[0][0]
			y_temp = layer_126[0][1]
			x_plot_126.append(x_temp)
			y_plot_126.append(y_temp)
		# ********* Ring 127 ****************
		if (layersTotal > 126):
			layer_127 = self.ONION[126]
			Len_127 = len(layer_127)
			x_plot_127 = []
			y_plot_127 = []
			for i in range(0, Len_127):
				x_temp = layer_127[i][x_loc]
				y_temp = layer_127[i][y_loc]
				x_plot_127.append(x_temp)
				y_plot_127.append(y_temp)
			x_temp = layer_127[0][0]
			y_temp = layer_127[0][1]
			x_plot_127.append(x_temp)
			y_plot_127.append(y_temp)
		# ********* Ring 128 ****************
		if (layersTotal > 127):
			layer_128 = self.ONION[127]
			Len_128 = len(layer_10)
			x_plot_128 = []
			y_plot_128 = []
			for i in range(0, Len_128):
				x_temp = layer_128[i][x_loc]
				y_temp = layer_128[i][y_loc]
				x_plot_128.append(x_temp)
				y_plot_128.append(y_temp)
			x_temp = layer_128[0][0]
			y_temp = layer_128[0][1]
			x_plot_128.append(x_temp)
			y_plot_128.append(y_temp)
		# ********* Ring 129 ****************
		if (layersTotal > 128):
			layer_129 = self.ONION[128]
			Len_129 = len(layer_129)
			x_plot_129 = []
			y_plot_129 = []
			for i in range(0, Len_129):
				x_temp = layer_129[i][x_loc]
				y_temp = layer_129[i][y_loc]
				x_plot_129.append(x_temp)
				y_plot_129.append(y_temp)
			x_temp = layer_129[0][0]
			y_temp = layer_129[0][1]
			x_plot_129.append(x_temp)
			y_plot_129.append(y_temp)
		# ********* Ring 130 ****************
		if (layersTotal > 29):
			layer_130 = self.ONION[129]
			Len_130 = len(layer_130)
			x_plot_130 = []
			y_plot_130 = []
			for i in range(0, Len_130):
				x_temp = layer_130[i][x_loc]
				y_temp = layer_130[i][y_loc]
				x_plot_130.append(x_temp)
				y_plot_130.append(y_temp)
			x_temp = layer_130[0][0]
			y_temp = layer_130[0][1]
			x_plot_130.append(x_temp)
			y_plot_130.append(y_temp)
		# ********* Ring 131 ****************
		if (layersTotal > 130):
			layer_131 = self.ONION[130]
			Len_131 = len(layer_131)
			x_plot_131 = []
			y_plot_131 = []
			for i in range(0, Len_131):
				x_temp = layer_131[i][x_loc]
				y_temp = layer_131[i][y_loc]
				x_plot_131.append(x_temp)
				y_plot_131.append(y_temp)
			x_temp = layer_131[0][0]
			y_temp = layer_131[0][1]
			x_plot_131.append(x_temp)
			y_plot_131.append(y_temp)
		# ********* Ring 132 ****************
		if (layersTotal > 131):
			layer_132 = self.ONION[131]
			Len_132 = len(layer_132)
			x_plot_132 = []
			y_plot_132 = []
			for i in range(0, Len_132):
				x_temp = layer_132[i][x_loc]
				y_temp = layer_132[i][y_loc]
				x_plot_132.append(x_temp)
				y_plot_132.append(y_temp)
			x_temp = layer_132[0][0]
			y_temp = layer_132[0][1]
			x_plot_132.append(x_temp)
			y_plot_132.append(y_temp)
		# ********* Ring 133 ****************
		if (layersTotal > 132):
			layer_133 = self.ONION[132]
			Len_133 = len(layer_133)
			x_plot_133 = []
			y_plot_133 = []
			for i in range(0, Len_133):
				x_temp = layer_133[i][x_loc]
				y_temp = layer_133[i][y_loc]
				x_plot_133.append(x_temp)
				y_plot_133.append(y_temp)
			x_temp = layer_133[0][0]
			y_temp = layer_133[0][1]
			x_plot_133.append(x_temp)
			y_plot_133.append(y_temp)
		# ********* Ring 134 ****************
		if (layersTotal > 133):
			layer_134 = self.ONION[133]
			Len_134 = len(layer_16)
			x_plot_134 = []
			y_plot_134 = []
			for i in range(0, Len_134):
				x_temp = layer_134[i][x_loc]
				y_temp = layer_134[i][y_loc]
				x_plot_134.append(x_temp)
				y_plot_134.append(y_temp)
			x_temp = layer_134[0][0]
			y_temp = layer_134[0][1]
			x_plot_134.append(x_temp)
			y_plot_134.append(y_temp)
		# ********* Ring 135 ****************
		if (layersTotal > 134):
			layer_135 = self.ONION[134]
			Len_135 = len(layer_135)
			x_plot_135 = []
			y_plot_135 = []
			for i in range(0, Len_135):
				x_temp = layer_135[i][x_loc]
				y_temp = layer_135[i][y_loc]
				x_plot_135.append(x_temp)
				y_plot_135.append(y_temp)
			x_temp = layer_135[0][0]
			y_temp = layer_135[0][1]
			x_plot_135.append(x_temp)
			y_plot_135.append(y_temp)
		# ********* Ring 136 ****************
		if (layersTotal > 135):
			layer_136 = self.ONION[135]
			Len_136 = len(layer_136)
			x_plot_136 = []
			y_plot_136 = []
			for i in range(0, Len_136):
				x_temp = layer_136[i][x_loc]
				y_temp = layer_136[i][y_loc]
				x_plot_136.append(x_temp)
				y_plot_136.append(y_temp)
			x_temp = layer_136[0][0]
			y_temp = layer_136[0][1]
			x_plot_136.append(x_temp)
			y_plot_136.append(y_temp)
		# ********* Ring 137 ****************
		if (layersTotal > 136):
			layer_137 = self.ONION[136]
			Len_137 = len(layer_137)
			x_plot_137 = []
			y_plot_137 = []
			for i in range(0, Len_137):
				x_temp = layer_137[i][x_loc]
				y_temp = layer_137[i][y_loc]
				x_plot_137.append(x_temp)
				y_plot_137.append(y_temp)
			x_temp = layer_137[0][0]
			y_temp = layer_137[0][1]
			x_plot_137.append(x_temp)
			y_plot_137.append(y_temp)
		# ********* Ring 138 ****************
		if (layersTotal > 137):
			layer_138 = self.ONION[137]
			Len_138 = len(layer_138)
			x_plot_138 = []
			y_plot_138 = []
			for i in range(0, Len_138):
				x_temp = layer_138[i][x_loc]
				y_temp = layer_138[i][y_loc]
				x_plot_138.append(x_temp)
				y_plot_138.append(y_temp)
			x_temp = layer_138[0][0]
			y_temp = layer_138[0][1]
			x_plot_138.append(x_temp)
			y_plot_138.append(y_temp)
		# ********* Ring 139 ****************
		if (layersTotal > 138):
			layer_139 = self.ONION[138]
			Len_139 = len(layer_139)
			x_plot_139 = []
			y_plot_139 = []
			for i in range(0, Len_139):
				x_temp = layer_139[i][x_loc]
				y_temp = layer_139[i][y_loc]
				x_plot_139.append(x_temp)
				y_plot_139.append(y_temp)
			x_temp = layer_139[0][0]
			y_temp = layer_139[0][1]
			x_plot_139.append(x_temp)
			y_plot_139.append(y_temp)
		# ********* Ring 140 ****************
		if (layersTotal > 139):
			layer_140 = self.ONION[139]
			Len_140 = len(layer_140)
			x_plot_140 = []
			y_plot_140 = []
			for i in range(0, Len_140):
				x_temp = layer_140[i][x_loc]
				y_temp = layer_140[i][y_loc]
				x_plot_140.append(x_temp)
				y_plot_140.append(y_temp)
			x_temp = layer_140[0][0]
			y_temp = layer_140[0][1]
			x_plot_140.append(x_temp)
			y_plot_140.append(y_temp)
		# ********* Ring 141 ****************
		if (layersTotal > 140):
			layer_141 = self.ONION[140]
			Len_141 = len(layer_141)
			x_plot_141 = []
			y_plot_141 = []
			for i in range(0, Len_141):
				x_temp = layer_141[i][x_loc]
				y_temp = layer_141[i][y_loc]
				x_plot_141.append(x_temp)
				y_plot_141.append(y_temp)
			x_temp = layer_141[0][0]
			y_temp = layer_141[0][1]
			x_plot_141.append(x_temp)
			y_plot_141.append(y_temp)
		# ********* Ring 142 ****************
		if (layersTotal > 141):
			layer_142 = self.ONION[141]
			Len_142 = len(layer_142)
			x_plot_142 = []
			y_plot_142 = []
			for i in range(0, Len_142):
				x_temp = layer_142[i][x_loc]
				y_temp = layer_142[i][y_loc]
				x_plot_142.append(x_temp)
				y_plot_142.append(y_temp)
			x_temp = layer_142[0][0]
			y_temp = layer_142[0][1]
			x_plot_142.append(x_temp)
			y_plot_142.append(y_temp)
		# ********* Ring 143 ****************
		if (layersTotal > 142):
			layer_143 = self.ONION[142]
			Len_143 = len(layer_143)
			x_plot_143 = []
			y_plot_143 = []
			for i in range(0, Len_143):
				x_temp = layer_143[i][x_loc]
				y_temp = layer_143[i][y_loc]
				x_plot_143.append(x_temp)
				y_plot_143.append(y_temp)
			x_temp = layer_143[0][0]
			y_temp = layer_143[0][1]
			x_plot_143.append(x_temp)
			y_plot_143.append(y_temp)
		# ********* Ring 144 ****************
		if (layersTotal > 143):
			layer_144 = self.ONION[143]
			Len_144 = len(layer_144)
			x_plot_144 = []
			y_plot_144 = []
			for i in range(0, Len_144):
				x_temp = layer_144[i][x_loc]
				y_temp = layer_144[i][y_loc]
				x_plot_144.append(x_temp)
				y_plot_144.append(y_temp)
			x_temp = layer_144[0][0]
			y_temp = layer_144[0][1]
			x_plot_144.append(x_temp)
			y_plot_144.append(y_temp)
		# ********* Ring 145 ****************
		if (layersTotal > 144):
			layer_145 = self.ONION[144]
			Len_145 = len(layer_145)
			x_plot_145 = []
			y_plot_145 = []
			for i in range(0, Len_145):
				x_temp = layer_145[i][x_loc]
				y_temp = layer_145[i][y_loc]
				x_plot_145.append(x_temp)
				y_plot_145.append(y_temp)
			x_temp = layer_145[0][0]
			y_temp = layer_145[0][1]
			x_plot_145.append(x_temp)
			y_plot_145.append(y_temp)
		# ********* Ring 146 ****************
		if (layersTotal > 145):
			layer_146 = self.ONION[145]
			Len_146 = len(layer_146)
			x_plot_146 = []
			y_plot_146 = []
			for i in range(0, Len_146):
				x_temp = layer_146[i][x_loc]
				y_temp = layer_146[i][y_loc]
				x_plot_146.append(x_temp)
				y_plot_146.append(y_temp)
			x_temp = layer_146[0][0]
			y_temp = layer_146[0][1]
			x_plot_146.append(x_temp)
			y_plot_146.append(y_temp)
		# ********* Ring 147 ****************
		if (layersTotal > 146):
			layer_147 = self.ONION[146]
			Len_147 = len(layer_147)
			x_plot_147 = []
			y_plot_147 = []
			for i in range(0, Len_147):
				x_temp = layer_147[i][x_loc]
				y_temp = layer_147[i][y_loc]
				x_plot_147.append(x_temp)
				y_plot_147.append(y_temp)
			x_temp = layer_147[0][0]
			y_temp = layer_147[0][1]
			x_plot_147.append(x_temp)
			y_plot_147.append(y_temp)
		# ********* Ring 148 ****************
		if (layersTotal > 147):
			layer_148 = self.ONION[147]
			Len_148 = len(layer_148)
			x_plot_148 = []
			y_plot_148 = []
			for i in range(0, Len_148):
				x_temp = layer_148[i][x_loc]
				y_temp = layer_148[i][y_loc]
				x_plot_148.append(x_temp)
				y_plot_148.append(y_temp)
			x_temp = layer_148[0][0]
			y_temp = layer_148[0][1]
			x_plot_148.append(x_temp)
			y_plot_148.append(y_temp)
		# ********* Ring 149 ****************
		if (layersTotal > 148):
			layer_149 = self.ONION[148]
			Len_149 = len(layer_149)
			x_plot_149 = []
			y_plot_149 = []
			for i in range(0, Len_149):
				x_temp = layer_149[i][x_loc]
				y_temp = layer_149[i][y_loc]
				x_plot_149.append(x_temp)
				y_plot_149.append(y_temp)
			x_temp = layer_149[0][0]
			y_temp = layer_149[0][1]
			x_plot_149.append(x_temp)
			y_plot_149.append(y_temp)
		# ********* Ring 150 ****************
		if (layersTotal > 149):
			layer_150 = self.ONION[149]
			Len_150 = len(layer_150)
			x_plot_150 = []
			y_plot_150 = []
			for i in range(0, Len_150):
				x_temp = layer_150[i][x_loc]
				y_temp = layer_150[i][y_loc]
				x_plot_150.append(x_temp)
				y_plot_150.append(y_temp)
			x_temp = layer_150[0][0]
			y_temp = layer_150[0][1]
			x_plot_150.append(x_temp)
			y_plot_150.append(y_temp)            
		# ********* Ring 151 ****************
		if (layersTotal > 150):
			layer_151 = self.ONION[150]
			Len_151 = len(layer_151)
			x_plot_151 = []
			y_plot_151 = []
			for i in range(0, Len_151):
				x_temp = layer_151[i][x_loc]
				y_temp = layer_151[i][y_loc]
				x_plot_151.append(x_temp)
				y_plot_151.append(y_temp)
			x_temp = layer_151[0][0]
			y_temp = layer_151[0][1]
			x_plot_151.append(x_temp)
			y_plot_151.append(y_temp)
		# ********* Ring 152 ****************
		if (layersTotal > 151):
			layer_152 = self.ONION[151]
			Len_152 = len(layer_152)
			x_plot_152 = []
			y_plot_152 = []
			for i in range(0, Len_152):
				x_temp = layer_152[i][x_loc]
				y_temp = layer_152[i][y_loc]
				x_plot_152.append(x_temp)
				y_plot_152.append(y_temp)
			x_temp = layer_152[0][0]
			y_temp = layer_152[0][1]
			x_plot_152.append(x_temp)
			y_plot_152.append(y_temp)
		# ********* Ring 153 ****************
		if (layersTotal > 152):
			layer_153 = self.ONION[152]
			Len_153 = len(layer_153)
			x_plot_153 = []
			y_plot_153 = []
			for i in range(0, Len_153):
				x_temp = layer_153[i][x_loc]
				y_temp = layer_153[i][y_loc]
				x_plot_153.append(x_temp)
				y_plot_153.append(y_temp)
			x_temp = layer_153[0][0]
			y_temp = layer_153[0][1]
			x_plot_153.append(x_temp)
			y_plot_153.append(y_temp)
		# ********* Ring 154 ****************
		if (layersTotal > 153):
			layer_154 = self.ONION[153]
			Len_154 = len(layer_154)
			x_plot_154 = []
			y_plot_154 = []
			for i in range(0, Len_154):
				x_temp = layer_154[i][x_loc]
				y_temp = layer_154[i][y_loc]
				x_plot_154.append(x_temp)
				y_plot_154.append(y_temp)
			x_temp = layer_154[0][0]
			y_temp = layer_154[0][1]
			x_plot_154.append(x_temp)
			y_plot_154.append(y_temp)
		# ********* Ring 155 ****************
		if (layersTotal > 154):
			layer_155 = self.ONION[154]
			Len_155 = len(layer_155)
			x_plot_155 = []
			y_plot_155 = []
			for i in range(0, Len_155):
				x_temp = layer_155[i][x_loc]
				y_temp = layer_155[i][y_loc]
				x_plot_155.append(x_temp)
				y_plot_155.append(y_temp)
			x_temp = layer_155[0][0]
			y_temp = layer_155[0][1]
			x_plot_155.append(x_temp)
			y_plot_155.append(y_temp)
		# ********* Ring 156 ****************
		if (layersTotal > 155):
			layer_156 = self.ONION[155]
			Len_156 = len(layer_156)
			x_plot_156 = []
			y_plot_156 = []
			for i in range(0, Len_156):
				x_temp = layer_156[i][x_loc]
				y_temp = layer_156[i][y_loc]
				x_plot_156.append(x_temp)
				y_plot_156.append(y_temp)
			x_temp = layer_156[0][0]
			y_temp = layer_156[0][1]
			x_plot_156.append(x_temp)
			y_plot_156.append(y_temp)
		# ********* Ring 157 ****************
		if (layersTotal > 156):
			layer_157 = self.ONION[156]
			Len_157 = len(layer_157)
			x_plot_157 = []
			y_plot_157 = []
			for i in range(0, Len_157):
				x_temp = layer_157[i][x_loc]
				y_temp = layer_157[i][y_loc]
				x_plot_157.append(x_temp)
				y_plot_157.append(y_temp)
			x_temp = layer_157[0][0]
			y_temp = layer_157[0][1]
			x_plot_157.append(x_temp)
			y_plot_157.append(y_temp)
		# ********* Ring 158 ****************
		if (layersTotal > 157):
			layer_158 = self.ONION[157]
			Len_158 = len(layer_158)
			x_plot_158 = []
			y_plot_158 = []
			for i in range(0, Len_158):
				x_temp = layer_158[i][x_loc]
				y_temp = layer_158[i][y_loc]
				x_plot_158.append(x_temp)
				y_plot_158.append(y_temp)
			x_temp = layer_158[0][0]
			y_temp = layer_158[0][1]
			x_plot_158.append(x_temp)
			y_plot_158.append(y_temp)
		# ********* Ring 159 ****************
		if (layersTotal > 158):
			layer_159 = self.ONION[158]
			Len_159 = len(layer_159)
			x_plot_159 = []
			y_plot_159 = []
			for i in range(0, Len_159):
				x_temp = layer_159[i][x_loc]
				y_temp = layer_159[i][y_loc]
				x_plot_159.append(x_temp)
				y_plot_159.append(y_temp)
			x_temp = layer_159[0][0]
			y_temp = layer_159[0][1]
			x_plot_159.append(x_temp)
			y_plot_159.append(y_temp)
		# ********* Ring 160 ****************
		if (layersTotal > 159):
			layer_160 = self.ONION[159]
			Len_160 = len(layer_160)
			x_plot_160 = []
			y_plot_160 = []
			for i in range(0, Len_160):
				x_temp = layer_160[i][x_loc]
				y_temp = layer_160[i][y_loc]
				x_plot_160.append(x_temp)
				y_plot_160.append(y_temp)
			x_temp = layer_160[0][0]
			y_temp = layer_160[0][1]
			x_plot_160.append(x_temp)
			y_plot_160.append(y_temp)  
		# ********* Ring 161 ****************
		if (layersTotal > 160):
			layer_161 = self.ONION[160]
			Len_161 = len(layer_161)
			x_plot_161 = []
			y_plot_161 = []
			for i in range(0, Len_161):
				x_temp = layer_161[i][x_loc]
				y_temp = layer_161[i][y_loc]
				x_plot_161.append(x_temp)
				y_plot_161.append(y_temp)
			x_temp = layer_161[0][0]
			y_temp = layer_161[0][1]
			x_plot_161.append(x_temp)
			y_plot_161.append(y_temp)
		# ********* Ring 162 ****************
		if (layersTotal > 161):
			layer_162 = self.ONION[161]
			Len_162 = len(layer_162)
			x_plot_162 = []
			y_plot_162 = []
			for i in range(0, Len_162):
				x_temp = layer_162[i][x_loc]
				y_temp = layer_162[i][y_loc]
				x_plot_162.append(x_temp)
				y_plot_162.append(y_temp)
			x_temp = layer_162[0][0]
			y_temp = layer_162[0][1]
			x_plot_162.append(x_temp)
			y_plot_162.append(y_temp)
		# ********* Ring 163 ****************
		if (layersTotal > 162):
			layer_163 = self.ONION[162]
			Len_163 = len(layer_163)
			x_plot_163 = []
			y_plot_163 = []
			for i in range(0, Len_163):
				x_temp = layer_163[i][x_loc]
				y_temp = layer_163[i][y_loc]
				x_plot_163.append(x_temp)
				y_plot_163.append(y_temp)
			x_temp = layer_163[0][0]
			y_temp = layer_163[0][1]
			x_plot_163.append(x_temp)
			y_plot_163.append(y_temp)
		# ********* Ring 164 ****************
		if (layersTotal > 163):
			layer_164 = self.ONION[163]
			Len_164 = len(layer_164)
			x_plot_164 = []
			y_plot_164 = []
			for i in range(0, Len_164):
				x_temp = layer_164[i][x_loc]
				y_temp = layer_164[i][y_loc]
				x_plot_164.append(x_temp)
				y_plot_164.append(y_temp)
			x_temp = layer_164[0][0]
			y_temp = layer_164[0][1]
			x_plot_164.append(x_temp)
			y_plot_164.append(y_temp)
		# ********* Ring 165 ****************
		if (layersTotal > 164):
			layer_165 = self.ONION[164]
			Len_165 = len(layer_165)
			x_plot_165 = []
			y_plot_165 = []
			for i in range(0, Len_165):
				x_temp = layer_165[i][x_loc]
				y_temp = layer_165[i][y_loc]
				x_plot_165.append(x_temp)
				y_plot_165.append(y_temp)
			x_temp = layer_165[0][0]
			y_temp = layer_165[0][1]
			x_plot_165.append(x_temp)
			y_plot_165.append(y_temp)
		# ********* Ring 166 ****************
		if (layersTotal > 165):
			layer_166 = self.ONION[165]
			Len_166 = len(layer_166)
			x_plot_166 = []
			y_plot_166 = []
			for i in range(0, Len_166):
				x_temp = layer_166[i][x_loc]
				y_temp = layer_166[i][y_loc]
				x_plot_166.append(x_temp)
				y_plot_166.append(y_temp)
			x_temp = layer_166[0][0]
			y_temp = layer_166[0][1]
			x_plot_166.append(x_temp)
			y_plot_166.append(y_temp)
		# ********* Ring 167 ****************
		if (layersTotal > 166):
			layer_167 = self.ONION[166]
			Len_167 = len(layer_167)
			x_plot_167 = []
			y_plot_167 = []
			for i in range(0, Len_167):
				x_temp = layer_167[i][x_loc]
				y_temp = layer_167[i][y_loc]
				x_plot_167.append(x_temp)
				y_plot_167.append(y_temp)
			x_temp = layer_167[0][0]
			y_temp = layer_167[0][1]
			x_plot_167.append(x_temp)
			y_plot_167.append(y_temp)
		# ********* Ring 168 ****************
		if (layersTotal > 167):
			layer_168 = self.ONION[167]
			Len_168 = len(layer_168)
			x_plot_168 = []
			y_plot_168 = []
			for i in range(0, Len_168):
				x_temp = layer_168[i][x_loc]
				y_temp = layer_168[i][y_loc]
				x_plot_168.append(x_temp)
				y_plot_168.append(y_temp)
			x_temp = layer_168[0][0]
			y_temp = layer_168[0][1]
			x_plot_168.append(x_temp)
			y_plot_168.append(y_temp)
		# ********* Ring 169 ****************
		if (layersTotal > 168):
			layer_169 = self.ONION[168]
			Len_169 = len(layer_169)
			x_plot_169 = []
			y_plot_169 = []
			for i in range(0, Len_169):
				x_temp = layer_169[i][x_loc]
				y_temp = layer_169[i][y_loc]
				x_plot_169.append(x_temp)
				y_plot_169.append(y_temp)
			x_temp = layer_169[0][0]
			y_temp = layer_169[0][1]
			x_plot_169.append(x_temp)
			y_plot_169.append(y_temp)
		# ********* Ring 170 ****************
		if (layersTotal > 169):
			layer_170 = self.ONION[169]
			Len_170 = len(layer_170)
			x_plot_170 = []
			y_plot_170 = []
			for i in range(0, Len_170):
				x_temp = layer_170[i][x_loc]
				y_temp = layer_170[i][y_loc]
				x_plot_170.append(x_temp)
				y_plot_170.append(y_temp)
			x_temp = layer_170[0][0]
			y_temp = layer_170[0][1]
			x_plot_170.append(x_temp)
			y_plot_170.append(y_temp)
		# ********* Ring 171 ****************
		if (layersTotal > 170):
			layer_171 = self.ONION[170]
			Len_171 = len(layer_171)
			x_plot_171 = []
			y_plot_171 = []
			for i in range(0, Len_171):
				x_temp = layer_171[i][x_loc]
				y_temp = layer_171[i][y_loc]
				x_plot_171.append(x_temp)
				y_plot_171.append(y_temp)
			x_temp = layer_171[0][0]
			y_temp = layer_171[0][1]
			x_plot_171.append(x_temp)
			y_plot_171.append(y_temp)  
           
            
            
            
            


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
		if (layersTotal > 62):
			plt.plot(x_plot_63, y_plot_63, marker='.')
		if (layersTotal > 63):
			plt.plot(x_plot_64, y_plot_64, marker='.')
		if (layersTotal > 64):
			plt.plot(x_plot_65, y_plot_65, marker='.')
		if (layersTotal > 65):
			plt.plot(x_plot_66, y_plot_66, marker='.')
		if (layersTotal > 66):
			plt.plot(x_plot_67, y_plot_67, marker='.')
		if (layersTotal > 67):
			plt.plot(x_plot_68, y_plot_68, marker='.')
		if (layersTotal > 68):
			plt.plot(x_plot_69, y_plot_69, marker='.')
		if (layersTotal > 69):
			plt.plot(x_plot_70, y_plot_70, marker='.')
		if (layersTotal > 70):
			plt.plot(x_plot_71, y_plot_71, marker='.')
		if (layersTotal > 71):
			plt.plot(x_plot_72, y_plot_72, marker='.')
		if (layersTotal > 72):
			plt.plot(x_plot_73, y_plot_73, marker='.')
		if (layersTotal > 73):
			plt.plot(x_plot_74, y_plot_74, marker='.')
		if (layersTotal > 74):
			plt.plot(x_plot_75, y_plot_75, marker='.')
		if (layersTotal > 75):
			plt.plot(x_plot_76, y_plot_76, marker='.')
		if (layersTotal > 76):
			plt.plot(x_plot_77, y_plot_77, marker='.')
		if (layersTotal > 77):
			plt.plot(x_plot_78, y_plot_78, marker='.')
		if (layersTotal > 78):
			plt.plot(x_plot_79, y_plot_79, marker='.')
		if (layersTotal > 79):
			plt.plot(x_plot_80, y_plot_80, marker='.')
		if (layersTotal > 80):
			plt.plot(x_plot_81, y_plot_81, marker='.')
		if (layersTotal > 81):
			plt.plot(x_plot_82, y_plot_82, marker='.')
		if (layersTotal > 82):
			plt.plot(x_plot_83, y_plot_83, marker='.')
		if (layersTotal > 83):
			plt.plot(x_plot_84, y_plot_84, marker='.')            
		if (layersTotal > 84):
			plt.plot(x_plot_85, y_plot_85, marker='.')
		if (layersTotal > 85):
			plt.plot(x_plot_86, y_plot_86, marker='.')
		if (layersTotal > 86):
			plt.plot(x_plot_87, y_plot_87, marker='.')
		if (layersTotal > 87):
			plt.plot(x_plot_88, y_plot_88, marker='.')
		if (layersTotal > 88):
			plt.plot(x_plot_89, y_plot_89, marker='.')
		if (layersTotal > 89):
			plt.plot(x_plot_90, y_plot_90, marker='.')            
		if (layersTotal > 90):
			plt.plot(x_plot_91, y_plot_91, marker='.')
		if (layersTotal > 91):
			plt.plot(x_plot_92, y_plot_92, marker='.')
		if (layersTotal > 92):
			plt.plot(x_plot_93, y_plot_93, marker='.')
		if (layersTotal > 93):
			plt.plot(x_plot_94, y_plot_94, marker='.')
		if (layersTotal > 94):
			plt.plot(x_plot_95, y_plot_95, marker='.')
		if (layersTotal > 95):
			plt.plot(x_plot_96, y_plot_96, marker='.')            
		if (layersTotal > 96):
			plt.plot(x_plot_97, y_plot_97, marker='.')
		if (layersTotal > 97):
			plt.plot(x_plot_98, y_plot_98, marker='.')
		if (layersTotal > 98):
			plt.plot(x_plot_99, y_plot_99, marker='.')
		if (layersTotal > 99):
			plt.plot(x_plot_100, y_plot_100, marker='.')
		if (layersTotal > 100):
			plt.plot(x_plot_101, y_plot_101, marker='.')      
		if (layersTotal > 101):
			plt.plot(x_plot_102, y_plot_102, marker='.')            
		if (layersTotal > 102):
			plt.plot(x_plot_103, y_plot_103, marker='.')
		if (layersTotal > 103):
			plt.plot(x_plot_104, y_plot_104, marker='.')
		if (layersTotal > 104):
			plt.plot(x_plot_105, y_plot_105, marker='.')
		if (layersTotal > 105):
			plt.plot(x_plot_106, y_plot_106, marker='.')
		if (layersTotal > 106):
			plt.plot(x_plot_107, y_plot_107, marker='.')            
		if (layersTotal > 107):
			plt.plot(x_plot_108, y_plot_108, marker='.')
		if (layersTotal > 108):
			plt.plot(x_plot_109, y_plot_109, marker='.')
		if (layersTotal > 109):
			plt.plot(x_plot_110, y_plot_110, marker='.')
		if (layersTotal > 110):
			plt.plot(x_plot_111, y_plot_111, marker='.')
		if (layersTotal > 111):
			plt.plot(x_plot_112, y_plot_112, marker='.')
		if (layersTotal > 112):
			plt.plot(x_plot_113, y_plot_113, marker='.')
		if (layersTotal > 113):
			plt.plot(x_plot_114, y_plot_114, marker='.')
		if (layersTotal > 114):
			plt.plot(x_plot_115, y_plot_115, marker='.')
		if (layersTotal > 115):
			plt.plot(x_plot_116, y_plot_116, marker='.')
		if (layersTotal > 116):
			plt.plot(x_plot_117, y_plot_117, marker='.')
		if (layersTotal > 117):
			plt.plot(x_plot_118, y_plot_118, marker='.')
		if (layersTotal > 118):
			plt.plot(x_plot_119, y_plot_119, marker='.')
		if (layersTotal > 119):
			plt.plot(x_plot_120, y_plot_120, marker='.')
		if (layersTotal > 120):
			plt.plot(x_plot_121, y_plot_121, marker='.')
		if (layersTotal > 121):
			plt.plot(x_plot_122, y_plot_122, marker='.')
		if (layersTotal > 122):
			plt.plot(x_plot_123, y_plot_123, marker='.')
		if (layersTotal > 123):
			plt.plot(x_plot_124, y_plot_124, marker='.')
		if (layersTotal > 124):
			plt.plot(x_plot_125, y_plot_125, marker='.')
		if (layersTotal > 125):
			plt.plot(x_plot_126, y_plot_126, marker='.')
		if (layersTotal > 126):
			plt.plot(x_plot_127, y_plot_127, marker='.')
		if (layersTotal > 127):
			plt.plot(x_plot_128, y_plot_128, marker='.')
		if (layersTotal > 128):
			plt.plot(x_plot_129, y_plot_129, marker='.')
		if (layersTotal > 129):
			plt.plot(x_plot_130, y_plot_130, marker='.')
		if (layersTotal > 130):
			plt.plot(x_plot_131, y_plot_131, marker='.')
		if (layersTotal > 131):
			plt.plot(x_plot_132, y_plot_132, marker='.')
		if (layersTotal > 132):
			plt.plot(x_plot_133, y_plot_133, marker='.')
		if (layersTotal > 133):
			plt.plot(x_plot_134, y_plot_134, marker='.')
		if (layersTotal > 134):
			plt.plot(x_plot_135, y_plot_135, marker='.')
		if (layersTotal > 135):
			plt.plot(x_plot_136, y_plot_136, marker='.')
		if (layersTotal > 136):
			plt.plot(x_plot_137, y_plot_137, marker='.')
		if (layersTotal > 137):
			plt.plot(x_plot_138, y_plot_138, marker='.')
		if (layersTotal > 138):
			plt.plot(x_plot_139, y_plot_139, marker='.')
		if (layersTotal > 139):
			plt.plot(x_plot_140, y_plot_140, marker='.')
		if (layersTotal > 140):
			plt.plot(x_plot_141, y_plot_141, marker='.')          
		if (layersTotal > 141):
			plt.plot(x_plot_142, y_plot_142, marker='.')
		if (layersTotal > 142):
			plt.plot(x_plot_143, y_plot_143, marker='.')           
		if (layersTotal > 143):
			plt.plot(x_plot_144, y_plot_144, marker='.')
		if (layersTotal > 144):
			plt.plot(x_plot_145, y_plot_145, marker='.')
		if (layersTotal > 145):
			plt.plot(x_plot_146, y_plot_146, marker='.')
		if (layersTotal > 146):
			plt.plot(x_plot_147, y_plot_147, marker='.')
		if (layersTotal > 147):
			plt.plot(x_plot_148, y_plot_148, marker='.')
		if (layersTotal > 148):
			plt.plot(x_plot_149, y_plot_149, marker='.')
		if (layersTotal > 149):
			plt.plot(x_plot_150, y_plot_150, marker='.')
		if (layersTotal > 150):
			plt.plot(x_plot_151, y_plot_151, marker='.')            
		if (layersTotal > 151):
			plt.plot(x_plot_152, y_plot_152, marker='.')
		if (layersTotal > 152):
			plt.plot(x_plot_153, y_plot_153, marker='.')           
		if (layersTotal > 153):
			plt.plot(x_plot_154, y_plot_154, marker='.')
		if (layersTotal > 154):
			plt.plot(x_plot_155, y_plot_155, marker='.')
		if (layersTotal > 155):
			plt.plot(x_plot_156, y_plot_156, marker='.')
		if (layersTotal > 156):
			plt.plot(x_plot_157, y_plot_157, marker='.')
		if (layersTotal > 157):
			plt.plot(x_plot_158, y_plot_158, marker='.')
		if (layersTotal > 158):
			plt.plot(x_plot_159, y_plot_159, marker='.')
		if (layersTotal > 159):
			plt.plot(x_plot_160, y_plot_160, marker='.')           
		if (layersTotal > 160):
			plt.plot(x_plot_161, y_plot_161, marker='.')            
		if (layersTotal > 161):
			plt.plot(x_plot_162, y_plot_162, marker='.')
		if (layersTotal > 162):
			plt.plot(x_plot_163, y_plot_163, marker='.')           
		if (layersTotal > 163):
			plt.plot(x_plot_164, y_plot_164, marker='.')
		if (layersTotal > 164):
			plt.plot(x_plot_165, y_plot_165, marker='.')
		if (layersTotal > 165):
			plt.plot(x_plot_166, y_plot_166, marker='.')
		if (layersTotal > 166):
			plt.plot(x_plot_167, y_plot_167, marker='.')
		if (layersTotal > 167):
			plt.plot(x_plot_168, y_plot_168, marker='.')
		if (layersTotal > 168):
			plt.plot(x_plot_169, y_plot_169, marker='.')            
		if (layersTotal > 170):
			plt.plot(x_plot_171, y_plot_171, marker='.')              
		if (layersTotal > 171):
			plt.plot(x_plot_172, y_plot_172, marker='.')            
		if (layersTotal > 172):
			plt.plot(x_plot_173, y_plot_173, marker='.')            
            

		#plt.title('Convex Nested Hulls', fontsize=16)       
		# x axis label
		plt.xlabel('X-axis', fontsize=12)
		# y axis label
		plt.ylabel('Y-axis', fontsize=12)
		# show the graph
		plt.show()