import numpy as np
import math

class PathTotalClass:

    def __init__(self, ONION):
        self.ONION = ONION

    def PathCalc(self):
        layersTotal = len(self.ONION)
        #print("LAYERS = ", layersTotal)
        x_loc = 0
        y_loc = 1
        pnt_id = 2
   
        # ********* Ring 1 ****************
        if (layersTotal > 0):
            layer_1 = self.ONION[0]
            Len_1 = len(layer_1)
            x_plot_1 = []
            y_plot_1 = []
            trail = []
            for i in range(0, Len_1):
                x_temp = layer_1[i][x_loc]
                y_temp = layer_1[i][y_loc]
                pnt_temp = layer_1[i][pnt_id]
                x_plot_1.append(x_temp)
                y_plot_1.append(y_temp)
                trail.append(pnt_temp)
            x_temp = layer_1[0][0]
            y_temp = layer_1[0][1]
            pnt_temp = layer_1[0][2]
            x_plot_1.append(x_temp)
            y_plot_1.append(y_temp)
            trail.append(pnt_temp)
            thisNow = len(x_plot_1)
            #print("x_plot = ", x_plot_1)
            #print("y_plot = ", y_plot_1)
            path = [x_plot_1, y_plot_1]
            #print("PATH = ", path)
            #print("TRAIL = ", trail)
            PATH = np.array(path)

        count = 0
        SumDist = 0                             # Starting Distance
        AccrueDist = []                         # added 05/15/2023
        for i in range(thisNow):
            count += 1
            x_a = PATH[0][i]
            #print("XAAA = ", x_a)
            y_a = path[1][i]
            if count < thisNow:
                x_b = path[0][count]
                y_b = path[1][count]
            else:
                x_b = path[0][0]
                y_b = path[1][0]

            x_piece = (x_b - x_a)**2
            y_piece = (y_b - y_a)**2
            operand = (x_piece + y_piece)
            d_partial = math.sqrt(operand)
            SumDist = SumDist + d_partial
            AccrueDist.append(SumDist)
        #print("Keep track of distance growth = ", AccrueDist)
        
        PntvsDist = [trail, AccrueDist]
        #print("Point vs Accrued Distance = ", PntvsDist)

        
        # This is just for visual and is a "clean-up" that is not necessary
        # Resort "trail" to start with point "1"
        where = trail.index(1)
        #print("WHERE = ", where)
        whereYes = where + 1
        trail_front = trail[0:whereYes]
        #print("Trail Front = ", trail_front)
        trailPntsCnt = len(trail)
        trail_back = trail[where:trailPntsCnt]
        trail_back_slice = trail_back[:-1]
        #print("Trail_Back_Slice = ", trail_back_slice)
        TRAIL_at_pt1 = trail_back_slice + trail_front
        #print("Trail ========= ", TRAIL)

        silver = [SumDist, TRAIL_at_pt1, PntvsDist]

        return silver
