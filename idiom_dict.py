import csv
from _collections import defaultdict

class IdiomDict:
    def __init__(self):
        self.idiomdict = defaultdict()
        csvfile = open('idiom.csv', 'r')
        idiom_reader = csv.reader(csvfile)
        for row in idiom_reader:
            self.idiomdict[row[0]] = (row[1], int(row[2]))

    def lookup(self, word):
        return self.idiomdict[word]