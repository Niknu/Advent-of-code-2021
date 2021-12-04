#!/usr/bin/env python3

import numpy as np

def func():
    file_input = "input.txt"

    gamme_rate = '0b' # to binary format
    epsilon_rate = '0b' # to binary format
    flipping = '0b'

    matrix = np.loadtxt(file_input, usecols=range(12))
    collums = matrix.shape[1]

    '''
    print(matrix)
    print(matrix[: , 1]) # lodret
    print(matrix[0 , :]) # vandret
    print("shape = ",matrix.shape)
    print("collums = ",matrix.shape[1])
    '''
    
    
    for x in range(collums):
        ones = np.count_nonzero(matrix[:, x] == 1)  
        zeros = np.count_nonzero(matrix[:, 0] == 0)

        if ones > zeros:
            gamme_rate += '1'
        else:
            gamme_rate += '0'
        
        flipping += '1'

    gamme_rate = int(gamme_rate,2)
    flipping = int(flipping,2)
    epsilon_rate = gamme_rate ^ flipping

    print("gamme_rate = ",gamme_rate )
    print("epsilon_rate  = ",epsilon_rate)
    print("power consumption gamma*epsilon = ",gamme_rate *epsilon_rate)


if __name__ == "__main__":

    func()
