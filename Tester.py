from Node_type import Node_type

class Tester():
    def __init__(self, tree, dataset):
        self.__tree = tree
        self.__dataset = dataset
    
    def get_tree(self):
        return self.__tree
    def change_dataset(self, new_dataset):
        self.__dataset = new_dataset


    # Method which starting looping trough testing dataset
    def begin_testing(self):
        positive_tests = 0
        for dataline in self.__dataset[1:]:
            if self.__check_line(dataline, self.__dataset[0], self.__tree.get_root()):
                positive_tests += 1
        print("Your algorithm have " + str(positive_tests) + " succeded tests, of " + str(len(self.__dataset) - 1) + " tests in testing dataset.")

    # Method which checks accurency of algorithm for the given row
    def __check_line(self, dataline, labels, node):
        if node.get_type() == Node_type.Leaf:
            if node.get_column_name() == dataline[-1]:
                return True
            else:
                return False
        
        label_index = labels.index(node.get_column_name())
        try:
            return self.__check_line(dataline, labels, node.get_children()[dataline[label_index]])
        except:
            print("Algorithm didn't learn how to predict your input.")
            print(dataline)
            return False