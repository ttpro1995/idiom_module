import csv
from _collections import defaultdict

class IdiomDict:
    def __init__(self, csv_path):
        """
        csv format:
        idiom, meaning, sentiment(1,2,3)
        1 is bad
        2 is neutral
        3 is good
        :param csv_path: path to csv file
        """
        self.idiomdict = defaultdict()
        csvfile = open(csv_path, 'r')
        idiom_reader = csv.reader(csvfile)
        for row in idiom_reader:
            self.idiomdict[row[0]] = (row[1], int(row[2]))

    def lookup(self, words):
        """
        Input a word, get the meaning
        :param words: idiom sentences
        :return: a tuple (meaning as string, sentiment as int)
        """
        return self.idiomdict[words]


