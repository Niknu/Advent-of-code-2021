#!/usr/bin/env python

#import sys




def func():
    file_input = "input.txt"

    data = None
    data_test = None
    counter = 0
    counter_test = 0

    f = open(file_input,'r')

    test = [190,
        168,
        166,
        163,
        170,
        160,
        171,
        166,
        161,
        167,
        175,
        178]

    dataList = f.readlines()
    data_output = open("output.txt",'w')
    for x in range(len(dataList)):
        
        if data == None:
            data = dataList[x]
        else:
            if data < dataList[x]:
                counter+=1
                data = dataList[x]
                data_output.write(data)
            else:
                data = dataList[x]
    data_output.close()

        

    '''
    while True:
        line = f.readline()


        if data == None:
            data = line
        else:
            if data < line:
                counter+=1
                data = line
            else:
                data = line

        
        if not line:
            break
    '''
    print(counter)
    print(counter_test)



if __name__ == "__main__":

    func()







