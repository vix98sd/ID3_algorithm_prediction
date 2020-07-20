from Node_type import Node_type

class Node:
    def __init__(self, data, type):
        self.__data = data
        self.__children = {}
        self.__type = type

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data

    def get_type(self):
        return self.__type
    def set_type(self, type):
        return self.__type

    def get_children(self):
        return self.__children
    def add_child(self, branch_name, child):
        self.__children[branch_name] = child