from Node_type import Node_type
from Node import Node

class Tree:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def set_root(self, node):
        self.__root = node

    def count_nodes(self, node):
        if node is None:
            return 0
        
        number = 0
        for child in node.get_children():
            number += self.count_nodes(child)
        
        return number + 1

    def print_tree(self):
        self.__print_tree(self.get_root(), "root", "")

    def __print_tree(self, node, branch_name, deep):
        if node == None:
            return
        print(deep + branch_name, node.get_column_name())
        deep += "-"
        for c in node.get_children().keys():
            self.__print_tree(node.get_children()[c], c, deep)