import numpy as np

class ParamsClass:

    def __init__(self, paramsIN):
        self.paramsIN = paramsIN
        self.rA =  paramsIN[0]                                        # Region A
        self.rB =  paramsIN[1]                                        # Region B
        self.rC1 = paramsIN[2]                                        # Region C
        self.rC2 = paramsIN[3]
        self.rC3 = paramsIN[4]
        self.rC4 = paramsIN[5]
        self.rD1 = paramsIN[6]                                        # Region D
        self.rD2 = paramsIN[7]
        self.rD3 = paramsIN[8]
        self.rD4 = paramsIN[9]
        self.rD5 = paramsIN[10]
        self.rD_angl = paramsIN[11]
        self.FB_cnt = paramsIN[12]
        

    def updateParams(self):
        if (self.FB_cnt < 1):
            FB_cntUp = self.FB_cnt
            FB_cntUp += 1
            FBparams = self.paramsIN
            FBparams[12] = FB_cntUp

        else:
            # INSERT FEEDBACK LOGIC here
            rA  = 0.00
            rB  = 1.00
            rC1 = 1.00
            rC2 = 1.00
            rC3 = 1.00
            rC4 = 1.00
            rD1 = 0.90
            rD2 = 1.00
            rD3 = 1.00
            rD4 = 0.90
            rD5 = 0.90
            rD_angl = 65.0
            FB_cntUp = self.FB_cnt
            FB_cntUp += 1
    
            FBparams = [rA, rB,
                rC1, rC2, rC3, rC4,
                rD1, rD2, rD3, rD4, rD5,
                rD_angl,
                FB_cntUp]

        return FBparams

