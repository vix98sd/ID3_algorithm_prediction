from Node_type import Node_type

class Node:
    def __init__(self):
        self.__column_name = None
        self.__type = None
        self.__children = {}

    def get_column_name(self):
        return self.__column_name
    def set_column_name(self, column_name):
        self.__column_name = column_name

    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type

    def get_children(self):
        return self.__children
    def add_child(self, branch_name, child):
        self.__children[branch_name] = child