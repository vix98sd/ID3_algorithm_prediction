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
        negative_tests = 0
        not_trained = 0
        for dataline in self.__dataset[1:]:
            test_res = self.__check_line(dataline, self.__dataset[0], self.__tree.get_root())
            if test_res == 1:
                positive_tests += 1
            elif test_res == 0:
                negative_tests += 1
            else:
                not_trained += 1
        print("Your algorithm have " + str(positive_tests) + " succeded tests, " + str(negative_tests) + " negative tests, and your algorithm is not trained for " + not_trained + " tests.")

    # Method which checks accurency of algorithm for the given row
    def __check_line(self, dataline, labels, node):
        if node.get_type() == Node_type.Leaf:
            if node.get_column_name() == dataline[-1]:
                return 1
            else:
                return 0
        
        label_index = labels.index(node.get_column_name())
        try:
            return self.__check_line(dataline, labels, node.get_children()[dataline[label_index]])
        except:
            print("Algorithm didn't learn how to predict your input.")
            print(dataline)
            return 2