#!/usr/bin/env python 3

#import sys




def func():
    file_input = "input.txt"

    counter = 0
    counter_test = 0

    f = open(file_input,'r')


    dataList = f.readlines()

    for x in range(len(dataList)):
        
        if x+3 > len(dataList)-1:
            break
        
        data_window_0 = int(dataList[x],10) + int(dataList[x+1],10) + int(dataList[x+2],10)
        data_window_1 = int(dataList[x+1],10) + int(dataList[x+2],10) + int(dataList[x+3],10)
                

        if data_window_0 < data_window_1:
            counter_test+=1

        
    print("counter = ",counter)
    print("counter_test = ",counter_test)



if __name__ == "__main__":

    func()







