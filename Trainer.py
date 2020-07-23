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
            for j in range(1,len(outcome)):
                if column[j] == i and outcome[j] == "Yes":
                    t += 1
                elif column[j] == i and outcome[j] == "No":
                    f += 1
            gain_part +=(t+f)/(len(outcome)-1) * self.__calculate_entropy(t,f)
        gain = entropyS - gain_part
        return round(gain, 3)

    # A method which begins training process by calling __train method
    def begin_training(self):
        self.__tree.set_root(self.__train(self.__dataset))

    # A recursive method which starts training for real
    def __train(self, dataset):
        child = Node()

        # At first if, we need to check is there only one outcome
        # if it is, we have a leaf node, and this is the end of the branch
        if self.__is_one_outcome(dataset[-1]):
            child.set_column_name(dataset[-1][1])
            child.set_type(Node_type.Leaf)

        # At this elif, we need to check if we used all the columns from the dataset
        # but we have multiple outcomes, in this case, we are taking the outcome 
        # with maximum number of appearance
        elif len(dataset) == 2 and not(self.__is_one_outcome(dataset[-1])) :
            unique_outcomes = self.__get_unique_from_column(dataset[-1])
            column_name = unique_outcomes[0] if (dataset[-1].count(unique_outcomes[0]) > dataset[-1].count(unique_outcomes[1])) else unique_outcomes[1]
            child.set_column_name(column_name)
            child.set_type(Node_type.Leaf)
            
        # And here, at this else statment, we need to find column with maximum gain, 
        # and then to remove this column from dataset and proceed with child finding
        else:
            gains = []
            for dataline in dataset[:-1]:
                gains.append(self.__calculate_gain(dataline, dataset[-1]))
            
            max_gain_index = gains.index(max(gains))
            values_from_max_gain_col = self.__get_unique_from_column(dataset[max_gain_index])

            new_dataset = []
            for value in values_from_max_gain_col:
                new_dataset = self.__remove_rows_except(dataset, value, max_gain_index)
                child.set_column_name(new_dataset[max_gain_index][0])
                child.set_type(Node_type.NotLeaf)
                new_dataset = self.__remove_column(new_dataset, max_gain_index)

                child.add_child(value, self.__train(new_dataset))
        
        return child
        


    # A method which removes column from dataset
    def __remove_column(self, dataset, column_index):
        if column_index == 0 :
            return dataset[1:]
        elif column_index == len(dataset) - 1 :
            return dataset[:-1]
        else:
            return dataset[:column_index] + dataset[column_index + 1 :]

    # A method which removes all rows from dataset
    # except rows with the given value
    def __remove_rows_except(self, dataset, value, column):
        new_dataset = [list(x) for x in zip(*dataset)]
        
        for dataline in new_dataset[1:]:
            if dataline[column] != value:
                new_dataset.remove(dataline)

        new_dataset = [list(x) for x in zip(*new_dataset)]
        return new_dataset

    ## A method which cheking if there is only one outcome left
    def __is_one_outcome(self, outcome):
        for line in outcome[1:]:
            if line != outcome[1]:
                return False
        return True


