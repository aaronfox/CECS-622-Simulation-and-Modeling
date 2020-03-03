# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Assignment 3 Problem 4

import random # for uniform random distributions of length of process between nodes

# Node class is used to contain all info abotu the nodes and their connections and connection lengths
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

    def get_connection_length(self, other_node):
        for node, length in self.node_connections:
            if node == other_node:
                return length

# list_results stores all connections globally for use in main function
list_results = []
# analyze_performance recursively iterates through every node connection
# and attaches every completed path to global variable list_results
def analyze_performance(start_node, end_node, curr_list):
    if start_node == end_node:
        curr_list.append(start_node)
        list_results.append(curr_list)
        return
    for node, node_length in start_node.get_connecting_nodes():
        # Ensure duplicates aren't added to list
        if start_node not in curr_list:
            curr_list.append(start_node)
        copy_list = curr_list.copy()
        analyze_performance(node, end_node, copy_list)

# get_length_of_connections returns the length of all the connections of the path
# INPUT: node_list (list): list of all nodes and their connections, e.g. [Node 1, Node 2, Node 3, Node 4, Node 7]
# OUTPUT: length_sum (float): float sum of all the lengths
def get_length_of_connections(node_list):
    length_sum = 0
    for i in range(len(node_list) - 1):
        length = node_list[i].get_connection_length(node_list[i + 1])
        length_sum = length_sum + length
    # print(node_list)
    return length_sum

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

    ## Node 6 ##
    node_6.add_connection(node_7, random.uniform(9, 10))  # (6, 7): U (9, 10)

    # Run over each path to get average values for each path
    path_12347_values = []
    path_1247_values = []
    path_15347_values = []
    path_1547_values = []
    path_1567_values = []

    iterations_to_run = 5000
    for i in range(iterations_to_run):
        list_results = []
        analyze_performance(start_node=node_1, end_node=node_7, curr_list=[])

        max_value = 0
        min_value = float('inf')
        max_connection = []
        min_connection = []

        for connection_list in list_results:
            length = get_length_of_connections(connection_list)
            print(connection_list, end='')
            print(": ", end=' ')
            print(length)

            # Assign length values to each path to get average values
            if str(connection_list) == "[Node 1, Node 2, Node 3, Node 4, Node 7]":
                path_12347_values.append(length)
            elif str(connection_list) == "[Node 1, Node 2, Node 4, Node 7]":
                path_1247_values.append(length)
            elif str(connection_list) == "[Node 1, Node 5, Node 3, Node 4, Node 7]":
                path_15347_values.append(length)
            elif str(connection_list) == "[Node 1, Node 5, Node 4, Node 7]":
                path_1547_values.append(length)
            elif str(connection_list) == "[Node 1, Node 5, Node 6, Node 7]":
                path_1567_values.append(length)
                

            if max_value < length:
                max_value = length
                max_connection = connection_list
            if min_value > length:
                min_value = length
                min_connection = connection_list
    
        print("Max Value list: ", end='')
        print(max_connection, end=', Length of ')
        print(max_value, end='\n')
        print("Min Value list: ", end='')
        print(min_connection, end=', Length of ')
        print(min_value, end='\n')
        print("Finished iteration " + str(i + 1), end='\n\n')

print("Average values for each path over " + str(iterations_to_run) + " samples: ")
print("Average path_12347_values: " + str(sum(path_12347_values)/len(path_12347_values)))
print("Average path_1247_values: " + str(sum(path_1247_values)/len(path_1247_values)))
print("Average path_15347_values: " + str(sum(path_15347_values)/len(path_15347_values)))
print("Average path_1547_values: " + str(sum(path_1547_values)/len(path_1547_values)))
print("Average path_1567_values: " + str(sum(path_1567_values)/len(path_1567_values)))
    
