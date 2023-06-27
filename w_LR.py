import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt

class LR_continuousClass:

    def __init__(self, LR_seg, LR_seg_d_ci_auc):
        self.LR_segmnts = LR_seg[0]
        self.LR_endPnts = LR_seg[1]
        self.LR_seg_d_ci_auc = LR_seg_d_ci_auc
        
    def LR_plot(self):

        # *** Segmentation is currently a manual iterative process ****
        # Segmentation = [BIG array] has been received
        # ******* custom Segmentation is best for each new run ********
        
        # *********************** SEGMENT 1 ***************************
        x1 = self.LR_segmnts[0][0]
        y1 = self.LR_segmnts[0][1]
        
        # Importing linear regression
        from sklearn.linear_model import LinearRegression

        # pass the list to the 'np.array()'
        x1 = np.array(x1)
        y1 = np.array(y1)

        # Training model
        lrm = LinearRegression()
        lrm.fit(x1.reshape(-1, 1), y1.reshape(-1, 1))

        # Make predictions using linear regression model
        y1_pred = lrm.predict(x1.reshape(-1, 1))
        
        m1 = lrm.coef_
        #print("Slope_1 = ", m1)
        c1 = lrm.intercept_
        #print("y-intercept_1= ", c1)
        
        # *********************** SEGMENT 2 ***************************
        x2 = self.LR_segmnts[1][0]
        y2 = self.LR_segmnts[1][1]
        
        # Importing linear regression
        from sklearn.linear_model import LinearRegression

        # pass the list to the 'np.array()'
        x2 = np.array(x2)
        y2 = np.array(y2)

        # Training model
        lrm = LinearRegression()
        lrm.fit(x2.reshape(-1, 1), y2.reshape(-1, 1))

        # Make predictions using linear regression model
        y2_pred = lrm.predict(x2.reshape(-1, 1))
        
        m2 = lrm.coef_
        c2 = lrm.intercept_
        
        # *********************** SEGMENT 3 ***************************
        x3 = self.LR_segmnts[2][0]
        y3 = self.LR_segmnts[2][1]
        
        # Importing linear regression
        from sklearn.linear_model import LinearRegression

        # pass the list to the 'np.array()'
        x3 = np.array(x3)
        y3 = np.array(y3)

        # Training model
        lrm = LinearRegression()
        lrm.fit(x3.reshape(-1, 1), y3.reshape(-1, 1))

        # Make predictions using linear regression model
        y3_pred = lrm.predict(x3.reshape(-1, 1))
        
        m3 = lrm.coef_
        c3 = lrm.intercept_
        
        # *********************** SEGMENT 4 ***************************
        x4 = self.LR_segmnts[3][0]
        y4 = self.LR_segmnts[3][1]
        
        # Importing linear regression
        from sklearn.linear_model import LinearRegression

        # pass the list to the 'np.array()'
        x4 = np.array(x4)
        y4 = np.array(y4)

        # Training model
        lrm = LinearRegression()
        lrm.fit(x4.reshape(-1, 1), y4.reshape(-1, 1))

        # Make predictions using linear regression model
        y4_pred = lrm.predict(x4.reshape(-1, 1))
        
        m4 = lrm.coef_
        c4 = lrm.intercept_

        # ************** PLOT Linear Regression Lines *****************        
        plt.figure(figsize=(10, 5))
        plt.scatter(x1, y1, s=10, color='y')
        plt.scatter(x2, y2, s=10, color='y')
        plt.scatter(x3, y3, s=10, color='y')
        plt.scatter(x4, y4, s=10, color='y')
        plt.plot(x1, y1_pred, color='r')
        plt.plot(x2, y2_pred, color='b')
        plt.plot(x3, y3_pred, color='r')
        plt.plot(x4, y4_pred, color='b')
        plt.title('Comp_Induct vs Delta_L (Accumulations) Linear Regression Curve Fit', fontsize=16)
        plt.xlabel('Delta_L Accumulative', fontsize=16)
        plt.ylabel('Comp_Induct Accumulative', fontsize=16)
        plt.grid(True)
        plt.show()
        
        # ******************* Print "endpoints" **********************
        endPnt_1 = self.LR_endPnts[0]  
        endPnt_2 = self.LR_endPnts[1]          
        endPnt_3 = self.LR_endPnts[2]          
        endPnt_4 = self.LR_endPnts[3]
        print("endPnt_1 = ", endPnt_1)
        print("endPnt_2 = ", endPnt_2)        
        print("endPnt_3 = ", endPnt_3)        
        print("endPnt_4 = ", endPnt_4)
        
        # ************* Print Equations (y = m*x + b) ****************    
        print("Equation 1:   y = ", m1[0][0], "*x +", c1[0])
        print("Equation 2:   y = ", m2[0][0], "*x +", c2[0])
        print("Equation 3:   y = ", m3[0][0], "*x +", c3[0])
        print("Equation 4:   y = ", m4[0][0], "*x +", c4[0])
        
        # ********************** Mozart  *****************************    
        Mozart = self.LR_seg_d_ci_auc
        print("Mozart = ", Mozart)
        # ******************* Mozart Points **************************    
        Pnts_1 = Mozart[0][0]
        Pnts_2 = Mozart[0][1] - Pnts_1
        Pnts_3 = Mozart[0][2] - Pnts_2 - Pnts_1
        Pnts_4 = Mozart[0][3] - Pnts_3 - Pnts_2 - Pnts_1
        Pnts_base = Mozart[0][3]
        Pnts_1_f = Pnts_1/Pnts_base
        Pnts_2_f = Pnts_2/Pnts_base
        Pnts_3_f = Pnts_3/Pnts_base
        Pnts_4_f = Pnts_4/Pnts_base
        # **************** Mozart Delta_D Accum *********************    
        DD_1 = Mozart[1][0]
        DD_2 = Mozart[1][1] - DD_1
        DD_3 = Mozart[1][2] - DD_2 - DD_1
        DD_4 = Mozart[1][3] - DD_3 - DD_2 - DD_1
        DD_base = Mozart[1][3]
        DD_1_f = DD_1/DD_base
        DD_2_f = DD_2/DD_base
        DD_3_f = DD_3/DD_base
        DD_4_f = DD_4/DD_base     
        # ********* Mozart Complexity Induction Accum ***************    
        ci_1 = Mozart[2][0]
        ci_2 = Mozart[2][1] - ci_1
        ci_3 = Mozart[2][2] - ci_2 - ci_1
        ci_4 = Mozart[2][3] - ci_3 - ci_2 - ci_1
        ci_base = Mozart[2][3]
        ci_1_f = ci_1/ci_base
        ci_2_f = ci_2/ci_base
        ci_3_f = ci_3/ci_base
        ci_4_f = ci_4/ci_base        
        # ******************* Mozart AUC Accum **********************    
        auc_1 = Mozart[3][0]
        auc_2 = Mozart[3][1] - auc_1
        auc_3 = Mozart[3][2] - auc_2 - auc_1
        auc_4 = Mozart[3][3] - auc_3 - auc_2 - auc_1
        auc_base = Mozart[3][3]
        auc_1_f = auc_1/auc_base
        auc_2_f = auc_2/auc_base
        auc_3_f = auc_3/auc_base
        auc_4_f = auc_4/auc_base
        # ******************* Mozart (base) ****************************
        print("Total Number of Points = ", Pnts_base)
        print("Total Delta_D Accumulation = ", DD_base)        
        print("Total Complexity Induction Accumulation = ", ci_base)    
        print("Total Area Under the Curve = ", auc_base)           
        # ****************** Mozart Region 1 ***************************
        print("Region 1, No of Points = ", Pnts_1)
        print("Region 1, Points fraction = ", Pnts_1_f)
        print("Region 1, Delta_D Accumulation = ", DD_1)
        print("Region 1, Delta_D Accumulation, fraction = ", DD_1_f)
        print("Region 1, Complexity Induction Accumulation = ", ci_1)
        print("Region 1, Complexity Induction Accumulation, fraction = ", ci_1_f)        
        print("Region 1, AUC Accumulation = ", auc_1)
        print("Region 1, AUC Accumulation, fraction = ", auc_1_f)
        # ****************** Mozart Region 2 ***************************
        print("Region 2, No of Points = ", Pnts_2)
        print("Region 2, Points fraction = ", Pnts_2_f)
        print("Region 2, Delta_D Accumulation = ", DD_2)
        print("Region 2, Delta_D Accumulation, fraction = ", DD_2_f)
        print("Region 2, Complexity Induction Accumulation = ", ci_2)
        print("Region 2, Complexity Induction Accumulation, fraction = ", ci_2_f)        
        print("Region 2, AUC Accumulation = ", auc_2)
        print("Region 2, AUC Accumulation, fraction = ", auc_2_f)        
        
        
        
        
        
        
        
        
        