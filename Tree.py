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

    