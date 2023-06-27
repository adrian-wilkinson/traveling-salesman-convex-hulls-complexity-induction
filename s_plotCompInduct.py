import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt

class dx_vs_dci_Class:

    def __init__(self, accumDelta_L, accumComp_Induct):
        self.accumDelta_L = accumDelta_L
        self.accumComp_Induct = accumComp_Induct
        
    def compInduct(self):

        # ************ Calculate delta_L  accumulative ************

        delta_L_Accum = [0]    
        arr_delta_L_length = len(self.accumDelta_L)
        #range_delta_L = arr_delta_L_length - 1
        for i in range(arr_delta_L_length):
            hold = self.accumDelta_L[i] + delta_L_Accum[i]
            delta_L_Accum.append(hold)
        delta_L_Accum.pop(0)       
        #print("delta_L = ", self.accumDelta_L)             
        #print("delta_L_Accum = ", delta_L_Accum)
        print("Delta_L_Length Accumulation Total = ", delta_L_Accum[arr_delta_L_length-1])
        
        # ***** Calculate Complexity Induction  accumulative ****** 
        #init_accumComp = self.accumComp_Induct[0]
        compInduct_Accum = [0] 
        arr_CI_length = len(self.accumComp_Induct)
        #range_compInduct = arr_CI_length - 1
        for i in range(arr_CI_length):
            hold = self.accumComp_Induct[i] + compInduct_Accum[i]
            compInduct_Accum.append(hold)
        compInduct_Accum.pop(0)
        #print("compInduct = ", self.accumComp_Induct)  
        #print("compInduct_Accum = ", compInduct_Accum)
        print("Complexity Induction Accumulation Total = ", compInduct_Accum[arr_CI_length-1])
        
        # ***** plot x = compInduct_Accum  vs  delta_L_Accum ****** 
        x = np.array(delta_L_Accum)
        y = np.array(compInduct_Accum)
        
        know = len(delta_L_Accum)
        #print("Length of delta__Accum = ", know)
        
        #*** print  Comp_Induct  Accumulative  vs  delta_L Accumulative ********
        #***                        No Markers                          ********
        #plt.plot(x,y, 2, marker = 'o', label='line with select markers')
        plt.plot(x,y, 2)
        plt.title('Comp_Induct vs Delta_L (Accumulations)', fontsize=16)
        plt.xlabel('delta_L Accumulative', fontsize=12)
        plt.ylabel('Comp_Induct  Accumulative', fontsize=12)
        plt.show()
        #plt.plot(x,y, 2)  # plot
        #************************************************************************
        numPoints = 1178    # 57 for 6 nested triangles, 96 for 48 USA cities
        i = 0             # 1178 for Qatar,   746 for XQF131,  6000 for Canada so far
        mergeCount = []
        hold = 0
        while i < numPoints:
            hold_2 = hold + 1
            mergeCount.append(hold_2)
            hold = hold + 1
            i = i +1
        #print("MergeCount = ", mergeCount)
        #************************************************************************                    
        #********* print  Comp_Induct  Accumulative  vs  data Points ************
        u = mergeCount
        v = np.array(compInduct_Accum)

        plt.plot(u, y, 2)
        plt.title('Comp_Induct vs Points', fontsize=16)
        plt.xlabel('Points', fontsize=12)
        plt.ylabel('Comp_Induct  Accumulative', fontsize=12)
        plt.show()        
        #************************************************************************           
        #**** print  Comp_Induct  Accumulative  vs  delta_L Accumulative ********
        #**** print  Comp_Induct  Accumulative  vs  delta_L Accumulative ********
        #***                        With Markers                          *******
        plt.plot(x,y, 2, marker = 'o', label='line with select markers')
        plt.title('Comp_Induct vs Delta_L (Accumulations)', fontsize=16)
        plt.xlabel('delta_L Accumulative', fontsize=12)
        plt.ylabel('Comp_Induct Accumulative', fontsize=12)
        plt.show()
        #plt.plot(x,y, 2)  # plot
        
        # ********* Calculate Area Under the Curve  (AUC) ********* 
        aucBuild = []
        
        for i in range(arr_CI_length):
            prev = 0
            if (i < 1):
                hold_x1  = delta_L_Accum[prev]
                hold_x2 =  delta_L_Accum[i]
                d_x = hold_x2 - hold_x1
                hold_y1 =  compInduct_Accum[prev]
                hold_y2 =  compInduct_Accum[i]            
                d_y = hold_y2 -  hold_y1                     
                thisArea = d_x * d_y
                aucBuild.append(thisArea)
            else:
                hold_x1  = delta_L_Accum[i-1]
                hold_x2 =  delta_L_Accum[i]
                d_x = hold_x2 - hold_x1
                hold_y1 =  compInduct_Accum[prev]
                hold_y2 =  compInduct_Accum[i]            
                d_y = hold_y2 -  hold_y1                     
                thisArea = d_x * d_y                     
                thisArea = d_x * d_y
                aucBuild.append(thisArea)
                
        #print("aucBuild = ", aucBuild)
                
        AUC_Accum = [0]          
        auc_length = len(aucBuild)
        for i in range(auc_length):
            hold = AUC_Accum[i] + aucBuild[i]
            AUC_Accum.append(hold)
        AUC_Accum.pop(0)
        #print("AUC_Accum = ", AUC_Accum)
        last = len(AUC_Accum)
        AUC_tot_Accum = AUC_Accum[last - 1]
        print("AUC Total = ", AUC_tot_Accum)

        # **************************** Plots *************************** 
        q = np.array(delta_L_Accum)
        r = np.array(AUC_Accum)
       
        plt.plot(q,r, 2)  # plot
        plt.title('Linear', fontsize=16)
        plt.xlabel('delta_L Accumulative', fontsize=12)
        plt.ylabel('AUC  Accumulative', fontsize=12)
        plt.grid(True)
        plt.show()
        
        plt.plot(q,r, 2)  # plot
        plt.title('y-axis log, x-axis linear', fontsize=16)
        plt.xlabel('delta_L Accumulative', fontsize=12)
        plt.ylabel('log,  AUC  Accumulative', fontsize=12)
        plt.grid(True)
        plt.yscale('log')
        plt.show()
        
        plt.plot(q,r, 2)  # plot
        plt.title('y-axis log, x-axis log', fontsize=16)
        plt.xlabel('log,  delta_L Accumulative', fontsize=12)
        plt.ylabel('log,  AUC  Accumulative', fontsize=12)
        plt.grid(True)
        plt.xscale('log')
        plt.yscale('log')
        plt.show()
        
        # ******************* Return Data ****************************
        retThis = [x, y, AUC_Accum]

        return retThis
        