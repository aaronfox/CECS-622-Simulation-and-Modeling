# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Assignment 3 Problem 4

import random # for uniform random distributions of length of process between nodes
class Node:
    def __init__(self, name):
        self.node_connections = []
        self.name = name
        print("Creating Node...")

    # For printing purposes
    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.name + ". Connections: " + str(self.node_connections))

    def add_connection(self, connecting_node, length):
        self.node_connections.append([connecting_node, length])

    def get_connecting_nodes(self):
        return self.node_connections

    # def print(self):
    #     print(self.node_connections)

if __name__ == "__main__":
    print("Running critical path simulation...")
    node_1 = Node("Node 1")
    node_2 = Node("Node 2")
    node_3 = Node("Node 3")
    node_4 = Node("Node 4")
    node_5 = Node("Node 5")
    node_6 = Node("Node 6")
    node_7 = Node("Node 7")

    ## Node 1 ##
    node_1.add_connection(node_2, random.uniform(4, 6))  # (1, 2): U (4,6)
    node_1.add_connection(node_5, 6)  # (1, 5): 6
    print(node_1)

    ## Node 2 ##
