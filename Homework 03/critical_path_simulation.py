# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Assignment 3 Problem 4

import random # for uniform random distributions of length of process between nodes
class Node:
    def __init__(self):
        self.node_connections = []
        print("Creating Node...")
        pass

    def add_connection(self, connecting_node, length):
        self.node_connections.append([connecting_node, length])

    def get_connecting_nodes(self):
        return self.node_connections

if __name__ == "__main__":
    print("Running critical path simulation...")
    node_1 = Node()
    node_2 = Node()
    node_3 = Node()
    node_4 = Node()
    node_5 = Node()
    node_7 = Node()
    node_6 = Node()

    ## Node 1 ##
    node_1.add_connection(node_2, random.uniform(4, 6))  # (1, 2): U (4,6)
    node_1.add_connection(node_5, 6)  # (1, 5): 6

    ## Node 2 ##
