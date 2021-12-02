#!/usr/bin/env python3




def func():
    file_input = "input.txt"

    x = 0
    y = 0
    depth = 0

    f = open(file_input,'r')

    dataList = f.readlines()
    
    
    test = dataList[0].split( )
    print(test)
    print(test[0])
    
    '''
    print(int(test[1])+int(test[1]))
    print(type(test[1]))
    '''
    
    for z in range(len(dataList)):

        input = dataList[z].split( )
        if input[0] == "forward":
            x+= int( input[1] )
            depth+= y*int( input[1] )
        elif input[0] == "down":
            y+= int(input[1])
        elif input[0] == "up":
            y-= int(input[1])
    
    print("horisontal = ",x)
    print("depth = ",depth)
    print("total x*y = ",x*depth)




if __name__ == "__main__":

    func()
