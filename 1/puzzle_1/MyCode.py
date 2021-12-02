#!/usr/bin/env python

#import sys




def func():
    file_input = "input.txt"

    data = None
    data_test = None
    counter = 0
    counter_test = 0

    f = open(file_input,'r')

    test = [199,
    200, 
    208 ,
    210 ,
    200 ,
    207 ,
    240 ,
    269 ,
    260 ,
    263 ,]

    dataList = f.readlines()
    data_output = open("output_test.txt",'w')
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
        

        '''
        print("INPUT= ",test[x],"x= ",x)
        print("prev number = ",data_test)
        print("_________________")
        if data_test == None:
            data_test = test[x]
        else:
            if data_test < test[x]:
                print(" data_test=",data_test,"test= ",test[x])

                data_test = test[x]
                counter+=1
                data_output.write(str(data_test)+'\n')
            else:
                data_test = test[x]
        print("---------------------")
        '''
        if x+1 > len(dataList)-1:
            break

        if dataList[x] < dataList[x+1]:
            counter_test+=1

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







