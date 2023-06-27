import numpy as np

class CountArrayClass:

  def __init__(self, ONION):
    self.Onion = ONION


  def Question(self):
    count = 0
#ONION =  [[[-3.0980762000000004, -1.7886750000000002, 14],
            #[3.0980762000000004, -1.7886750000000002, 20],
#			[0, 4.135, 8]],
#			[[-2.57846096, -1.4886750000000002, 13],
#			[2.57846096, -1.4886750000000002, 19], [0, 3.4279999999999995, 7]],
#			[[-2.05884572, -1.1886750000000001, 12], [2.05884572, -1.1886750000000001, 18],
#			[0, 2.7209999999999996, 6]],
#			[[-1.53923048, -0.8886750000000001, 11],
#			[1.53923048, -0.8886750000000001, 17], [0, 2.014, 5]],
#			[[-1.01961524, -0.5886750000000001, 10], [1.01961524, -0.5886750000000001, 16],
#			[0, 1.307, 4]],
#			[[-0.5, -0.288675, 9], [0.5, -0.288675, 15], [0, 0.6, 3]],
#			[[-0.15, 0.0, 1], [0.15, 0.0, 2]]]




# *************************************************************************************
    numberLayers = len(self.Onion)
    print("Number of layers in this Onion = ", numberLayers)

    Layers = []

    for onion in reversed(self.Onion):
        #print("onion = ", onion)
        onionL = len(onion)
        Layers.append(onionL)
        #print("Layers = ", Layers)
        #print("Points per layer = ", Layers)

    loops = 0
    interim = []

    for layer in Layers:
        loops = layer + loops
        interim.append(loops)
        #print("Loops (merge decisions) per layer = ", interim)
    interim_L = len(interim) - 1

# *************************************************************************************

    print("*********** Total number of Merge Loops (or Merge Decisions) ***************")
    sum = 0
    i = 0
    while (i < interim_L):
        sum = sum + interim[i]
        i = i + 1
    print("Total number of loops (merge decisions) = ", sum)





