# -*- coding: UTF-8 -*-
'''
class bookFinder():
    readData(Data, whatFind)
        return array
    mainFinder():
        Find Keys
        Find Key pieces
        return bookIndex
'''

class bookFinder():
    
    def readData(dataWay, dataSection):
        data = open(dataWay, "r")
        book = data.readline()
        return book
    def mainFinder(dataListBook):
        return dataListBook

data = open("Data.txt", "r")
print(data.readline())
print("apologia de sócrates|platão|hunter|apologia|físico|1877")
