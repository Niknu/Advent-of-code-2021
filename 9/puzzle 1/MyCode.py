#!/usr/bin/env python3

from re import M
import numpy as np
import scipy.ndimage.filters as filters
import scipy.ndimage.morphology as morphology
import matplotlib.pyplot as plt


def detect_local_minima(arr):
    # https://stackoverflow.com/questions/3684484/peak-detection-in-a-2d-array/3689710#3689710
    """
    Takes an array and detects the troughs using the local maximum filter.
    Returns a boolean mask of the troughs (i.e. 1 when
    the pixel's value is the neighborhood maximum, 0 otherwise)
    """
    # define an connected neighborhood
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.morphology.html#generate_binary_structure
    #kernel = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.bool)
    neighborhood = morphology.generate_binary_structure(len(arr.shape),2)
    #neighborhood = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.bool)

    # apply the local minimum filter; all locations of minimum value 
    # in their neighborhood are set to 1
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.filters.html#minimum_filter
    local_min = (filters.minimum_filter(arr, footprint=neighborhood)==arr)
    print('local_min= ',local_min)
    # local_min is a mask that contains the peaks we are 
    # looking for, but also the background.
    # In order to isolate the peaks we must remove the background from the mask.
    # 
    # we create the mask of the background
    background = (arr==1)
    print("background= ",background)
    # 
    # a little technicality: we must erode the background in order to 
    # successfully subtract it from local_min, otherwise a line will 
    # appear along the background border (artifact of the local minimum filter)
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.morphology.html#binary_erosion
    eroded_background = morphology.binary_erosion(
        background, structure=neighborhood, border_value=1)
    print("eroded_background= ",eroded_background)
    # 
    # we obtain the final mask, containing only peaks, 
    # by removing the background from the local_min mask
    detected_minima = local_min ^ eroded_background
    return np.where(detected_minima)



def func1(matrix):

    m = np.pad(matrix, pad_width=1,mode='constant',constant_values=9)
    
    print(m)

    return ((m < np.roll(m, 1, 0)) &
            (m < np.roll(m, -1, 0)) &
            (m < np.roll(m, 1, 1)) &
            (m < np.roll(m, -1, 1)) 
            ) [1:-1, 1:-1]



def func():
    file_input = "input.txt"

    matrix = np.loadtxt(file_input, dtype=np.int)
    
    minima = func1(matrix)

    #values = np.extract(minima,matrix)

    print(matrix.shape)
    print(minima.shape)

    print("minima= \n",minima)
    print("Final = ",(matrix[minima]+1).sum() )
  







if __name__ == "__main__":

    func()