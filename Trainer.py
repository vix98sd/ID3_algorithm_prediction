from Node_type import Node_type
from Node import Node
from Tree import Tree
import math

class Trainer:
    def __init__(self, tree, dataset):
        self.__tree = tree
        self.__dataset = dataset

    def get_tree(self):
        return self.__tree
    def change_dataset(self, dataset):
        self.__dataset = dataset

    # First method calculates entropy of given column
    # by the formula: entropy(s) = - sum(p(x)*log2(p(x)))
    # where x is an unique element from column, and the
    # second one calculates entropy 
    def __calculate_entropy_s(self, column):
        entropy = 0
        unique = self.__get_unique_from_column(column)
        for item in unique :
            entropy -= (column.count(item) / (len(column) - 1)) * math.log((column.count(item) / (len(column) - 1)), 2)
        return round(entropy, 3)
    
    def __calculate_entropy(self, t, f):
        if t == 0 or f == 0 :
            return 0
        s = t+f
        entropy = -(t/s * math.log(t/s,2)) - (f/s * math.log(f/s,2))
        return round(entropy,3)
    # A method which returns a dictionary whth unique items in 
    # column, and with number of their showing in column
    def __get_unique_from_column(self, column):
        unique = []
        for item in column[1:] :
            try:
                unique.index(item)
            except:
                unique.append(item)
        return unique
            
    # A method which calculates the gain some column 
    def __calculate_gain(self, column, outcome):
        gain = 0
        entropyS = self.__calculate_entropy_s(outcome)
        gain_part = 0
        for i in self.__get_unique_from_column(column):
            t = 0
            f = 0
            for j in range(len(outcome) - 1):
                if column[j] == i and outcome[j] == "Yes":
                    t += 1
                else:
                    f += 1
            gain_part -= self.__calculate_entropy(t,f)
        gain = entropyS - gain_part
        return round(gain, 3)



    