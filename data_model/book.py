from data_model.author import Author
from data_model.publication import Publication


class Book():
    def __init__(self, title="", author=Author(), price=0, copies=0):
        self.publik = Publication(title,price,copies)
        self.__author = author

    def orderCopy(self, order):
        self.copies += order

    def toString(self):
        return "{}, {}".format(self.publik.title, self.__author.name)

    def getTitle(self):
        return self.publik.title.lower()

    def getAuthor(self):
        return self.__author.name.lower()

    def toRow(self):
        return "| {0:32s} | {1:15s} | {2:10.2f} | {3:6d} |".\
            format(self.title[:32], self.__author.name[:15],
                   self.price, self.copies)

    def displayInfo(self):
        print("=============================================")
        print("|               BOOK DETAIL                 |")
        print("=============================================")
        print("| Title   : {0:31s} |".format(self.title[:30]))
        print("| Author  : {0:31s} |".format(self.__author.name[:30]))
        print("| Price   : {0:31s} |".format(str(self.price)))
        print("| Copies  : {0:31s} |".format(str(self.copies)))
        print("=============================================")
