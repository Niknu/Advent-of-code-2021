#!/usr/bin/env python 3

import numpy as np
import collections

def func():
    file_input = 'input_test.txt'

    dataIn = np.loadtxt(file_input, usecols=range(4),dtype=np.int64)

    print(dataIn)

    rows = dataIn.shape[0]

    arrPoints = []



    for x in range(rows):

        x1 = dataIn[x,0].item() # convert it to python class
        y1 = dataIn[x,1].item()
        x2 = dataIn[x,2].item()
        y2 = dataIn[x,3].item()

        if x1 == x2:
            if y1 < y2:
                for t in range(y1,y2+1):
                    arrPoints.append([x1,t])
            else:
                for t in range(y2,y1+1):
                    arrPoints.append([x1,t])
        if y1 == y2:
            if x1 < x2:
                for t in range(x1,x2+1):
                    arrPoints.append([t,y1])
            else:
                for t in range(x2,x1+1):
                    arrPoints.append([t,y1])
        else: # we don't consider anything else that --- and | lines
            continue

    print(arrPoints)
    counted_set = collections.Counter(frozenset(k) for k in arrPoints ).values()
    
    counted_set = list(counted_set)

    print(counted_set)

    print(len(counted_set))
    '''
    for x in range(len(counted_set)):
        
        if counted_set[x] == 1:
            del counted_set[x]

    print(counted_set)
    '''

if __name__ == "__main__":

    func()