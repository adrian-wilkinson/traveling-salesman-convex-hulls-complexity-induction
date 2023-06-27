import numpy as np

class PhylisC_Class:

    def __init__(self, genData, FeedBACK):
        self.genData = genData
        self.FeedBACK = FeedBACK
        # genData = [ pnt_2_id, pnt_4_id, pnt_5_id, L_Orig, L_new, Region, d_x, angle ]
        # L_Orig = dist_S3
        # L_new = dist_S5 + dist_S6


    def shortDist(self):
        rA =                                            self.FeedBACK[0]
        rB =                                            self.FeedBACK[1]
        rC1 =                                           self.FeedBACK[2]
        rC2 =                                           self.FeedBACK[3]     
        rC3 =                                           self.FeedBACK[4]        
        rC4 =                                           self.FeedBACK[5]          
        rD1 =                                           self.FeedBACK[6]    
        rD2 =                                           self.FeedBACK[7]
        rD3 =                                           self.FeedBACK[8] 
        rD4 =                                           self.FeedBACK[9]
        rD5 =                                           self.FeedBACK[10]
        rD_angl =                                       self.FeedBACK[11]
        
        # delta_L_Big = 11111111111111111111111111111111111111111111111111111111111111111
        merge_Big = 11111111111111111111111111111111111111111111111111111111111111111
        count = -1.0
        ticker = -1
        cur_Delta_L = []
        for i in self.genData:
            count += 1
            # print(i)   THIS WILL GENERATE LOTS OF DATA
            pnt_4_5 = i[3]                  # dist pt_4 to pt_5
            pnt_2_4_5 = i[4]                # dist after merge
            delta_L = pnt_2_4_5 - pnt_4_5
            #print("GGGGGGGGGGGG = ", delta_L)
            Where = i[5]
            d_x = i[6]
            angle = i[7]

#  *****************************************************************************
#            if (Where == "OUT_D1" or "OUT_D2" or "OUT_D3" or "OUT_D4" or "OUT_D5"):
#                if (angle > rD_angl):
#                    f_asci = 1.10   # apply a weight factor here?
#                else:
#                    f_asci = 1.00
#            else:
#                frog = "4 legs"
            f_asci = 1.0
#  *****************************************************************************            
            if (Where == "IN_A"):       # in Region IN_A
                merge = rA
#  *****************************************************************************
            elif (Where == "IN_B"):     # in Region IN_B
                merge = delta_L * rB
                r_fac = rB
#  *****************************************************************************
            elif (Where == "IN_C1"):    # in Region IN_C
                merge = delta_L * rC1
                r_fac = rC1
#  *****************************************************************************
            elif (Where == "IN_C2"):    # in Region IN_C
                merge = delta_L * rC2
                r_fac = rC2
#  *****************************************************************************
            elif (Where == "IN_C3"):    # in Region IN_C
                merge = delta_L * rC3
                r_fac = rC3
#  *****************************************************************************
            elif (Where == "IN_C4"):    # in Region IN_C
                merge = delta_L * rC4
                r_fac = rC4
#  *****************************************************************************
            elif (Where == "OUT_D1"):   # in Region IN_D1
                merge = delta_L * rD1 * f_asci
                r_fac = rD1
#  *****************************************************************************
            elif (Where == "OUT_D2"):   # in Region IN_D2
                merge = delta_L * rD2 * f_asci
                r_fac = rD2
#  *****************************************************************************
            elif (Where == "OUT_D3"):   # in Region IN_D3
                merge = delta_L * rD3 * f_asci
                r_fac = rD3
#  *****************************************************************************
            elif (Where == "OUT_D4"):   # in Region IN_D4
                merge = delta_L * rD4 * f_asci
                r_fac = rD4
#  *****************************************************************************
            else:     # Where == "OUT_D5" in Region IN_D5
                merge = delta_L * rD5 * f_asci
                r_fac = rD5
#  *****************************************************************************

            if merge <= merge_Big:
                merge_Big = merge
                cur_Delta_L = delta_L
                ticker = count
        #print("newdddddddddddd = ", delta_L)
        #print("Ticker = ", ticker)

        ticker = int(ticker)
        P2 = self.genData[ticker][0]
        #print("P22222222 = ", P2)
        P4 = self.genData[ticker][1]
        #print("P44444444 = ", P4)
        P5 = self.genData[ticker][2]
        #print("P55555555 = ", P5)
        merge = merge_Big
        #print("Smallest delta length = ", merge_Big)
        
#  ********** r_Comp_Induct ****************************************************    
        #r_Comp_Induct = 1 / r_fac
        if (Where == "OUT_D1"):
            r_Comp_Induct = 1 / r_fac
        elif (Where == "OUT_D2"):
            r_Comp_Induct = 1 / r_fac
        elif (Where == "OUT_D3"):
            r_Comp_Induct = 1 / r_fac
        elif (Where == "OUT_D4"):
            r_Comp_Induct = 1 / r_fac
        elif (Where == "OUT_D5"):
            r_Comp_Induct = 1 / r_fac
        else:
            r_Comp_Induct = r_fac
#  *****************************************************************************

        exchange = [P2, P4, P5, cur_Delta_L, r_Comp_Induct]

        return exchange

