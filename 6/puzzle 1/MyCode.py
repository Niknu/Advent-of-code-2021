#!/usr/bin/env python3

import numpy as np


class fish():
    def __init__(self, counterIn=8) -> None:

        if isinstance(counterIn,str):
            self.counter = int(counterIn,10)
        else:
            self.counter = counterIn
    
    def bornFish(self):
        return fish()
    
    def count(self):

        self.counter -=1

        if self.counter < 0:
            self.counter = 6
            return self.bornFish()
        else:
            return None
    def printCount(self):
        print(self.counter)

def func():
    #read and format data
    file_input = "input_test.txt"
    f = open(file_input)
    string = f.readline().split(",")

    #init
    arr = []
    for x in range(len(string)):
        arr.append(fish(string[x]))
    
    #Run the puzzle
    for k in range(0,18):
        for x in range(len(arr)):
            
            newFish = arr[x].count()
            if newFish != None:
                arr.append(newFish)

    #Answer
    amount = len(arr)
    print(amount)
    


    





if __name__ == "__main__":

    func()
