import numpy as np
import math

class PathSegmentClass:

    def __init__(self, LR_seg_endPts, Complex_q, Complex_r, Complex_auc):

        self.LR_endPnts = LR_seg_endPts
        self.Complex_q = Complex_q
        self.Complex_r = Complex_r
        self.Complex_auc = Complex_auc

    def SegPathCalc(self):
        # *** Segmentation is currently a manual iterative process ****
        # Segmentation = [BIG array] has been received
        # ******* custom Segmentation is best for each new run ********
        seg_break_pts = self.LR_endPnts
        seg_d_Delta = []
        seg_ci = []
        seg_auc = []
        # *********************** SEGMENT 1 ***************************
        endPt_1 = self.LR_endPnts[0]
        endPt_1_adj = endPt_1 - 1
        print("End Point 1 = ", endPt_1)
        d_L_accum_1 = self.Complex_q[endPt_1_adj]
        #print("End Point 1, accumulative delta_L = ", d_L_accum_1)
        ci_accum_1 = self.Complex_r[endPt_1_adj]
        #print("End Point 1, accumulative Complexity Induction = ", ci_accum_1)
        auc_accum_1 = self.Complex_auc[endPt_1_adj]
        #print("End Point 1, accumulative AUC = ", auc_accum_1)
        seg_d_Delta.append(d_L_accum_1)
        seg_ci.append(ci_accum_1)
        seg_auc.append(auc_accum_1)
        
        # *********************** SEGMENT 2 ***************************
        endPt_2 = self.LR_endPnts[1]
        endPt_2_adj = endPt_2 - 1
        print("End Point 2 = ", endPt_2)
        d_L_accum_2 = self.Complex_q[endPt_2_adj]
        #print("End Point 2, accumulative delta_L = ", d_L_accum_2)
        ci_accum_2 = self.Complex_r[endPt_2_adj]
        #print("End Point 2, accumulative Complexity Induction = ", ci_accum_2)
        auc_accum_2 = self.Complex_auc[endPt_2_adj]
        #print("End Point 2, accumulative AUC = ", auc_accum_2)
        seg_d_Delta.append(d_L_accum_2)
        seg_ci.append(ci_accum_2)
        seg_auc.append(auc_accum_2)
        
        # *********************** SEGMENT 3 ***************************
        endPt_3 = self.LR_endPnts[2]
        endPt_3_adj = endPt_3 - 1
        print("End Point 3 = ", endPt_3)
        d_L_accum_3 = self.Complex_q[endPt_3_adj]
        #print("End Point 3, accumulative delta_L = ", d_L_accum_3)
        ci_accum_3 = self.Complex_r[endPt_3_adj]
        #print("End Point 3, accumulative Complexity Induction = ", ci_accum_3)
        auc_accum_3 = self.Complex_auc[endPt_3_adj]
        #print("End Point 3, accumulative AUC = ", auc_accum_3)
        seg_d_Delta.append(d_L_accum_3)
        seg_ci.append(ci_accum_3)
        seg_auc.append(auc_accum_3)
        
        # *********************** SEGMENT 4 ***************************
        endPt_4 = self.LR_endPnts[3]
        endPt_4_adj = endPt_4 - 1
        print("End Point 4 = ", endPt_4)
        d_L_accum_4 = self.Complex_q[endPt_4_adj]
        #print("End Point 4, accumulative delta_L = ", d_L_accum_4)
        ci_accum_4 = self.Complex_r[endPt_4_adj]
        #print("End Point 4, accumulative Complexity Induction = ", ci_accum_4)
        auc_accum_4 = self.Complex_auc[endPt_4_adj]
        #print("End Point 4, accumulative AUC = ", auc_accum_4)
        seg_d_Delta.append(d_L_accum_4)
        seg_ci.append(ci_accum_4)
        seg_auc.append(auc_accum_4)
        
        # *********************** Appends ***************************
        Mozart = []
        Mozart.append(seg_break_pts)
        Mozart.append(seg_d_Delta)
        Mozart.append(seg_ci)
        Mozart.append(seg_auc)

        #print("Mozart = ", Mozart)
        
        return Mozart