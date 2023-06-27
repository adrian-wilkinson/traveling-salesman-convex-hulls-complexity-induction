import matplotlib.pyplot as plt
import numpy as np

class PlotFirstClass:

        def __init__(self, array):
                self.array = array

        def JustPoints(self):



                arr = np.array(self.array)
                #print(arr)
                length = len(arr)
                #print(length)

                x_arr = []
                y_arr = []

                for i in range(length):
                        x = arr[i][0]
                        x_arr.append(x)
                        y = arr[i][1]
                        y_arr.append(y)
                #print("X_arr = ", x_arr)
                #print("y_arr = ", y_arr)
                plt.figure(figsize=(12, 8)) 
                plt.scatter(x_arr, y_arr)
                plt.title('Scatter Plot of Data Points', fontsize=16)
                plt.xlabel('X-axis', fontsize=12)
                plt.ylabel('Y-axis', fontsize =12)
                plt.show()
