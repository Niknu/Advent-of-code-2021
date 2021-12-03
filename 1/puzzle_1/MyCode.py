#!/usr/bin/env python 3

#import sys




def func():
    file_input = "input.txt"

    data = None
    data_test = None
    counter = 0
    counter_test = 0

    f = open(file_input,'r')


    dataList = f.readlines()
    #data_output = open("output_test.txt",'w')
    for x in range(len(dataList)):
        
        
        if data == None:
            data = int(dataList[x],10)
        else:
            if data < int(dataList[x],10):
                counter+=1
                data = int(dataList[x],10)
                #data_output.write(data)
            else:
                data = int(dataList[x],10)
                
                
        
        if x+1 > len(dataList)-1:
            break

        if int(dataList[x],10) < int(dataList[x+1],10):
            counter_test+=1

    #data_output.close()

        
    print("counter = ",counter)
    print("counter_test = ",counter_test)



if __name__ == "__main__":

    func()







