#!/usr/bin/env python3

import numpy as np
from numpy.lib.function_base import percentile

def func():
    file_input = "input.txt"

    
    matrix = np.loadtxt(file_input, usecols=range(12))
    collums = matrix.shape[1]

    oxygen_rate = np.empty((0,collums),float)
    co2_rate = np.empty((0,collums),float)
    
    '''
    print(matrix)
    print(matrix[: , 0]) # lodret
    print(matrix[0 , :]) # vandret
    print("shape = ",matrix.shape)
    print("collums = ",matrix.shape[1])
    '''

    print("Data------------start")
    print(matrix)
    print("Data------------end")

    for x in range(collums):

        if x == 0:
            ones = np.count_nonzero(matrix[:, x] == 1)  
            zeros = np.count_nonzero(matrix[:, x] == 0)

            if ones > zeros:
                oxygen_rate = matrix[matrix[:, x] == 1]
            if zeros > ones:
                oxygen_rate = matrix[matrix[:, x] == 0]
            if ones < zeros:
                co2_rate = matrix[matrix[:, x] == 1]
            if zeros < ones:
                co2_rate = matrix[matrix[:, x] == 0]
            if zeros == ones:
                oxygen_rate = matrix[matrix[:, x] == 1]           # keeping the 1
                co2_rate    = matrix[matrix[:, x] == 0]           # keeping the 0
        else:

            ones_oxy = np.count_nonzero(oxygen_rate[:, x] == 1)  
            zeros_oxy = np.count_nonzero(oxygen_rate[:, x] == 0)

            ones_co2 = np.count_nonzero(co2_rate[:, x] == 1)  
            zeros_co2 = np.count_nonzero(co2_rate[:, x] == 0)

            if ones_oxy > zeros_oxy and oxygen_rate.shape[0] > 1 :
                oxygen_rate = oxygen_rate[oxygen_rate[:, x] == 1]
            if zeros_oxy > ones_oxy and oxygen_rate.shape[0] > 1 :
                oxygen_rate = oxygen_rate[oxygen_rate[:, x] == 0]
            if ones_co2 < zeros_co2 and co2_rate.shape[0] > 1 :
                co2_rate = co2_rate[co2_rate[:, x] == 1]
            if zeros_co2 < ones_co2 and co2_rate.shape[0] > 1 :
                co2_rate = co2_rate[co2_rate[:, x] == 0]
            if zeros_oxy == ones_oxy:
                oxygen_rate = oxygen_rate[oxygen_rate[:, x] == 1]     # keeping the 1
            if zeros_co2 == ones_co2:
                co2_rate    = co2_rate[co2_rate[:, x] == 0]           # keeping the 0
        
        print(oxygen_rate)
        print("-----------------")
        




    oxy_dec = oxygen_rate.dot(2**np.arange(oxygen_rate.size)[::-1])
    co2_dec = co2_rate.dot(2**np.arange(co2_rate.size)[::-1])
    print("oxygen_rate binary = ",oxygen_rate )
    print("co2_rate  binary = ",co2_rate)
    
    print("oxygen_rate decimal = ",oxy_dec)
    print("co2_rate  decimal = ",co2_dec)
    print("life support rating oxy*co2 = ", oxy_dec*co2_dec)
    

if __name__ == "__main__":

    func()
