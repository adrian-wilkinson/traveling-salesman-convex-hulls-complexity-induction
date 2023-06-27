from numpy import *
import numpy as np


class PhylisClass:

    def __init__(self, inner, outer, calcsCount):
        self.inner = inner
        self.outer = outer
        self.calcsCount = calcsCount

#class PhylisClass:

    #def __init__(self, inner, outer, calcsCount):
        #self.inner = inner
        #self.outer = outer
        #self.calcsCount = calcsCount

    def experiment_xx(self):
        #print("This is inner", self.inner)
        #print("This is outer", self.outer)
        #store = [1, 2, 3, 4, 5, -1000000000000000000000000000000000000000000000000000000000000]
        store = []
        dataBack = []
        delta_L = 100000000000000000000000000000000000000000000000000000000000000000000000.0
        counter = 0

        for idx, city_i in enumerate(self.inner):
            counter += 1
            in_size = len(self.inner)
            #print("inner length = ", in_size)
            one_back = in_size - 2
            #print("inner one back = ", one_back)
            stop = in_size
            #print("inner stop = ", stop)
            step_back = self.inner[one_back]
            #print("inner step back = ", step_back)

            track_inr_c = [city_i][0][2]						# track, inner loop current point id
            pnt_2_id = track_inr_c
            inr_c_x = [city_i][0][0]							# inner loop current point, x-location
            pnt_2x = inr_c_x
            inr_c_y = [city_i][0][1]							# inner loop current point, y-location
            pnt_2y = inr_c_y
            pnt_2_arr = [[pnt_2x], [pnt_2y]]
            pnt_2_a = np.array(pnt_2_arr)

            P2 = track_inr_c

            #print("************************************************************************")

            for idx, city_o in enumerate(self.outer):

                #counter += 1

                out_size = len(self.outer)
                #print("outer length = ", out_size)
                one_back = out_size - 1   #change back to 2
                #print("outer one back = ", one_back)
                Newstop = out_size
                #print("outer stop = ", stop)
                step_back = self.outer[one_back]
                #print("outer step back = ", step_back)

                track_outr_c = [city_o][0][2]					# track, outer loop current point id
                pnt_4_id = track_outr_c
                outr_c_x = [city_o][0][0]						# outer loop current point, x-location
                pnt_4_x = outr_c_x
                outr_c_y = [city_o][0][1]						# outer loop current point, y-location
                pnt_4_y = outr_c_y
                pnt_4_arr = [[pnt_4_x], [pnt_4_y]]
                pnt_4_a = np.array(pnt_4_arr)


                before = idx - 1
                #print("before = ", before)

                if (idx < 1):		# increment down, previous = "i" minus 1 (subtract)
                    #print("zero")
                    decrease = step_back
                else:
                    decrease = self.outer[before]
                    #print("decrease = ", decrease)

                #after = idx + 1

                #if (after < Newstop):
                decrease_id = decrease[2]						# track, outer loop previous point id
                pnt_5_id = decrease_id
                decrease_x = decrease[0]						# outer loop previous point, x-location
                pnt_5_x = decrease_x
                decrease_y = decrease[1]						# outer loop previous point, y-location
                pnt_5_y = decrease_y
                pnt_5_arr = [[pnt_5_x], [pnt_5_y]]
                pnt_5_a = np.array(pnt_5_arr)
                #********************************************************************************
                # calculating Euclidean distance using linalg.norm() ****************************
                dist_S3 = np.linalg.norm(pnt_4_a - pnt_5_a)   # distance between pnt_4 and pnt_5
                dist_S5 = np.linalg.norm(pnt_2_a - pnt_5_a)   # distance between pnt_2 and pnt_5
                dist_S6 = np.linalg.norm(pnt_2_a - pnt_4_a)   # distance between pnt_2 and pnt_4

                #print("idx, outer = ", idx)
                L_Orig = dist_S3
                L_new = dist_S5 + dist_S6
                delta_L_temp = L_new - L_Orig
                #print(delta_L_temp)
                #********************************************************************************
                #   Returns projected point plus IN or OUT
                #********************************************************************************
                def ClosestPointOnLine(a, b, p):
                    ap = p-a
                    ab = b-a
                    result = a + dot(ap,ab)/dot(ab,ab) * ab
                    #print("CCCCCCCCCCCCCccccccccccccccccccccccccCCCCCCCC  Closest Point = ", result)
                    return result

                a = array([pnt_4_x, pnt_4_y])
                b = array([pnt_5_x, pnt_5_y])
                p = array([pnt_2x, pnt_2y])      
               
                projPnt = ClosestPointOnLine(a, b, p)
                NowPnt = projPnt

                # calculating Euclidean distance using linalg.norm() **************
                dist_S7 = np.linalg.norm(NowPnt - a)       # distance between projPnt and pnt_4
                dist_S8 = np.linalg.norm(NowPnt - b)       # distance between projPnt and pnt_5
                dist_S9 = dist_S7 + dist_S8                # if dist_S10 == zero, then location == IN
                dist_S10 = dist_S9 - dist_S3
                #print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM IS Build Distance zero ? = ", dist_S10)
                dist_S11 = np.linalg.norm(NowPnt - p)       # distance between projPnt and pnt_2
                
                #********************************************************************************
                #   Function which Returns angle between  newPnt, pt4 and pt 5  IF  pt2  location ==  OUT
                #********************************************************************************
                from math import atan
                # Function to find the angle between two lines
                def findAngle(M1, M2):
                    PI = 3.14159265
                    angle = abs((M2 - M1) / (1 + M1 * M2))      # Store the tan value  of the angle
   
                    ret = atan(angle)                           # Calculate tan inverse of the angle
 
                    val = (ret * 180) / PI                      # Convert the angle from radian to degree
 
                    #print (round(val, 4))                       # Print the result
                    return val
                #**************  END OF ANGLE RETURN FUNCTION ******************************************
                #**************  LOGIC:  Angle based on REGION *****************************************
                tolerance = 0.000001    # THIS might need to be changed for very small distance datasets
                dist_Half = dist_S3 / 2
                
                if (dist_S7 <= dist_S8):
                    d_x = dist_S7
                else:
                    d_x = dist_S8       

                d_fraction = d_x / dist_Half
                
                if ((-tolerance) <= dist_S10 <= (tolerance)):  # based on projPnt, IS on segment
                    # Note that the projected point of a point that resides on a line onto the same line
                    # is the point itself.
                    # then angle = irrelevant, so
                    angle = 10000.0       # and
                    #d_fraction = d_x / dist_Half
                    if ((-tolerance) <= dist_S11 <= (tolerance)): # pt_2 (and its projPnt resides on segment
                        Region = "IN_A"                        
                    elif (d_fraction >= 0.4):          # pntProj (projection of pt_2) resides on segment
                        Region = "IN_B"
                    elif (d_fraction >= 0.3):          # pntProj (projection of pt_2) resides on segment
                        Region = "IN_C1"
                    elif (d_fraction >= 0.2):          # pntProj (projection of pt_2) resides on segment
                        Region = "IN_C2"                        
                    elif (d_fraction >= 0.1):          # pntProj (projection of pt_2) resides on segment
                        Region = "IN_C3" 
                    else:                              # pntProj (projection of pt_2) resides on segment
                        Region = "IN_C4"
                else:
                    # THE FOLLOWING IS based on projPnt, IS NOT on segment (on line, but not on segment)
                    if (d_fraction <= 0.1):
                        Region = "OUT_D1"
                    elif (d_fraction <= 0.2):
                        Region = "OUT_D2"
                    elif (d_fraction <= 0.3):
                        Region = "OUT_D3"                        
                    elif (d_fraction <= 0.4):
                        Region = "OUT_D4" 
                    else:
                        Region = "OUT_D5"                    
                    #********************************************************************************
                    # Since in Region OUT, then find angle
                    #  Following returns angle between pt2 and NowPnt & pt4 or pt5 (whichever is closest)
                    #  Assigns slope of M = 1000000  if denominator = zero
                    #********************************************************************************
                    if (dist_S7 <= dist_S8):             # if dist_S7  < dist_8  then pnt_4 is closer
                        
                        # Line 1  ==  pt2 to pt4
                        denominator1 = (pnt_2x - pnt_4_x)           # m = UNDEFINED. divide by zero
                        if (-0.000001 < denominator1 < 0.000001):
                            M1 = 1000000.0
                        else:
                            M1 = (pnt_2y - pnt_4_y) / denominator1
                        #print("fffffffffffffffff m1 = ", M1)
                        
                        # Line 2  ==  pt2 to projPnt
                        denominator2 = (pnt_2x - NowPnt[0])           # m = UNDEFINED. divide by zero
                        if (-0.000001 < denominator2 < 0.000001):
                            M2 = 1000000.0
                        else:
                            M2 = (pnt_2y - NowPnt[1]) / denominator2
                        #print("fffffffffffffffff m2 = ", M2)
                        
                        angle = findAngle(M1, M2)
                        
        
                    else:                                 # else pnt_5 is closer
                        # Line 1  ==  pt2 to pt5
                        denominator1 = (pnt_2x - pnt_5_x)           # m = UNDEFINED. divide by zero
                        if (-0.000001 < denominator1 < 0.000001):
                            M1 = 1000000.0
                        else:
                            M1 = (pnt_2y - pnt_5_y) / denominator1
                        #print("fffffffffffffffff m1 = ", M1)
   
                        # Line 2  ==  pt2 to projPnt
                        denominator2 = (pnt_2x - NowPnt[0])           # m = UNDEFINED. divide by zero
                        if (-0.000001 < denominator2 < 0.000001):
                            M2 = 1000000.0
                        else:                
                            M2 = (pnt_2y - NowPnt[1]) / denominator2
                        #print("fffffffffffffffff m2 = ", M2)
                        
                        angle = findAngle(M1, M2)
                         
                #print("RRRRRRRRRRRRRRRRRRRRRRRRRR   Region = ", Region)
                #print("RRRRRRRRRRRRRRRRRRRRRRRRRR   d_x = ", d_x)
                #print("RRRRRRRRRRRRRRRRRRRRRRRRRR   angle, IN vs OUT = ", angle)

                #**************  END OF LOGIC:  Angle, REGION Determination ***********************
                #**********************************************************************************
                outr_arr_dist_angle_t = [ pnt_2_id, pnt_4_id, pnt_5_id, L_Orig, L_new, Region, d_x, angle ]

                dataBack.append(outr_arr_dist_angle_t)

        return dataBack