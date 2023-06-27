import numpy as np


class LR_dx_vs_dci_Class:

    def __init__(self, accum_q, accum_r):
        self.accum_q = accum_q
        self.accum_r = accum_r
        
    def Seg_b4_LR(self):

        # *** Segmentation is currently a manual iterative process ****
        Segmentation = []
        endPts = []
        BachThis = []
        # ******* custom Segmentation is best for each new run ********
        # ******************* (a painful process) *********************
        
        # ******* Populate Segmentation No 1  *************************
        end_1 = 425  # Edit by hand for new run(s) [datasets] Qatar=425
        i = 0
        Seg_1x = []
        Seg_1y = []
        Seg_1  = []
        while i < end_1:
            qNow = self.accum_q[i]
            rNow = self.accum_r[i]
            hold_x = qNow
            Seg_1x.append(hold_x)
            hold_y = rNow
            Seg_1y.append(hold_y)
            hold = 0
            i = i + 1
        Seg_1.append(Seg_1x)
        Seg_1.append(Seg_1y)
        #print("Completed seg_1 populate")
        Segmentation.append(Seg_1)
        endPts.append(end_1)
        
        # ******* Populate Segmentation No 2  *************************
        end_2 = end_1 + 350    # Edit by hand for new run(s)  Qatar=350
        i = end_1
        Seg_2x = []
        Seg_2y = []
        Seg_2  = []
        while i < end_2:
            qNow = self.accum_q[i]
            rNow = self.accum_r[i]
            hold_x = qNow
            Seg_2x.append(hold_x)
            hold_y = rNow
            Seg_2y.append(hold_y)                  
            hold = 0
            i = i + 1
        Seg_2.append(Seg_2x)
        Seg_2.append(Seg_2y)
        #print("Completed seg_2 populate")
        Segmentation.append(Seg_2)
        endPts.append(end_2)
        
        # ******* Populate Segmentation No 3  *************************
        end_3 = end_2 + 190    # Edit by hand for new run(s)  Qatar=190
        i = end_2
        Seg_3x = []
        Seg_3y = []
        Seg_3  = []
        while i < end_3:
            qNow = self.accum_q[i]
            rNow = self.accum_r[i]
            hold_x = qNow
            Seg_3x.append(hold_x)
            hold_y = rNow
            Seg_3y.append(hold_y)                  
            hold = 0
            i = i + 1
        Seg_3.append(Seg_3x)
        Seg_3.append(Seg_3y)
        #print("Completed seg_3 populate")
        Segmentation.append(Seg_3)
        endPts.append(end_3)
        
        # ******* Populate Segmentation No 4  *************************
        end_4 = end_3 + 213    # Edit by hand for new run(s)  Qatar=213
        i = end_3
        Seg_4x = []
        Seg_4y = []
        Seg_4  = []
        while i < end_4:
            qNow = self.accum_q[i]
            rNow = self.accum_r[i]
            hold_x = qNow
            Seg_4x.append(hold_x)
            hold_y = rNow
            Seg_4y.append(hold_y)                  
            hold = 0
            i = i + 1
        Seg_4.append(Seg_4x)
        Seg_4.append(Seg_4y)
        #print("Completed seg_4 populate")
        Segmentation.append(Seg_4)
        endPts.append(end_4)
        
        # ************ Segmentation Complete  *************************
        
        BachThis.append(Segmentation)
        BachThis.append(endPts)
        
        return BachThis