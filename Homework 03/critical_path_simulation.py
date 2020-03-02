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


def analyze_performance(start_node, end_node, curr_list):
    # print(start_node)
    if start_node == end_node:
        curr_list.append(start_node)
        print("curr_list == " + str(curr_list))
        print("FINISHED")
        return
    for node, node_length in start_node.get_connecting_nodes():
        if start_node not in curr_list:
            curr_list.append(start_node)
        copy_list = curr_list.copy()
        analyze_performance(node, end_node, copy_list)

if __name__ == "__main__":
    print("Running critical path simulation...")
    node_1 = Node("Node 1")
    node_2 = Node("Node 2")
    node_3 = Node("Node 3")
    node_4 = Node("Node 4")
    node_5 = Node("Node 5")
    node_6 = Node("Node 6")
    node_7 = Node("Node 7")

    # Add respective deterministic/uniformly distributed connections per prompt
    ## Node 1 ##
    node_1.add_connection(node_2, random.uniform(4, 6))  # (1, 2): U (4,6)
    node_1.add_connection(node_5, 6)  # (1, 5): 6

    ## Node 2 ##
    node_2.add_connection(node_3, 6)  # (2, 3): 6
    node_2.add_connection(node_4, random.uniform(6, 8))  # (2, 4): U (6,8)

    ## Node 3 ##
    node_3.add_connection(node_4, random.uniform(4, 8))  # (3, 4): U (4,8)

    ## Node 4 ##
    node_4.add_connection(node_7, 4)  # (4, 7): 4

    ## Node 5 ##
    node_5.add_connection(node_3, 8)  # (5, 3): 8
    node_5.add_connection(node_4, 11)  # (5, 4): 11
    node_5.add_connection(node_6, random.uniform(8, 10))  # (5, 6): U (8,10)

    ## Node 5 ##
    node_6.add_connection(node_7, random.uniform(9, 10))  # (6, 7): U (9, 10)

    analyze_performance(start_node=node_1, end_node=node_7, curr_list=[])
