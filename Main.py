# -*- coding: UTF-8 -*-
import Finder as finder

'''
class Librarian:
    findBooks
    seeAllBooks
    addBooks
'''

class Librarian():
    
    def findBooks():
        # Caminho até o index do livro:
        find = finder.bookFinder
        bookIndex = find.mainFinder(find.readData("Data.txt", "titulo"))
        # Resposta do programa:
        print("putz", bookIndex)
        return bookIndex
    def addBooks():
        a = "hello", 2
        return "sócrates..."
    def seeAllBooks():
        return "Seeing all books..."

print(Librarian.addBooks())
