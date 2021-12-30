###############################################################################
# Maze Generation w/ Kruskals's Algorithm. 

# Kruskal's algorithm finds minimum spanning trees of weighted graphs. 
# The graph representing our maze is unweighted, however, so the algorithm has 
# been modified to select edges at random rather than by lowest weight.

# Citation 7. Kruskals's Algorithm
    # Also suggested by my TP mentor Winston
    # I watched the following Youtube videos to understand/visualize the 
    # concept, but all code was written by myself.
    # https://www.youtube.com/watch?v=4ZlRH0eK-qQ&t=1011s
    # https://www.youtube.com/watch?v=8pJKJBdOMME
    # https://www.youtube.com/watch?v=LRM-xGmyQNg 

# Steps:
    # Step 1: Choose an arbitrary vertex (Let's call the chosen vertex as the 
    # shaded vertex)
    # Step 2: Choose a non-visited Neighbor of the shaded vertex with minimum 
    # weight on its edge and connect it to the shaded vertex. Let's also call 
    # this newly chosen vertex as shaded.
    # Step 2.1: Select a neighbor from any one of shaded vertex if more than 
    # one vertices are shaded, this happens after first iteration of the 
    # algorithm. 
    # Don't choose a vertex that forms a cycle because MST is a tree and a 
    # tree cannot have a cycle.
    # If more than one vertex has equal weight, choose any of them, your MST 
    # will not be affected.
    # Step 3: Repeat from the step 2.1 until all the vertices are visited 
    # only once.
###############################################################################

import random

# This is the only class outside of classes.py
class Node(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.isConnected = False 
        self.listOfNeighbors = []
        # change this to true when I connect it with another node. 

# I want to represent pairs of connected nodes the same way I did w/ Prims:
# [(node1R, node1C), (node2R, node2C)]
    
def getNumOfNodesThatAreConnected(listOfNodes, rows, cols):
    # recall that listOfNodes is a 1D list of Nodes
    count = 0
    for node in listOfNodes:
        if node.isConnected == True:
            count += 1
    return count

# a major difference between prims and kruskals
# is that in kruskals, when we pick a new node 
# it can only be connected to one of its neighbors
# we don't add that node's neighbors to our greater 
# list of neighbors
def getNeighbors(listOfNodes, node, rows, cols):
    # node.row, node.col
    result = []
    x, y = node.row, node.col
    dXdY = [ (0, -1), (-1, 0), (0, 1), (1, 0) ]
    random.shuffle(dXdY)
    for (dx, dy) in dXdY:
        newX = x + dx
        newY = y + dy
        if 0 <= newX < rows and 0 <= newY < cols:
            for node in listOfNodes:
                result += [(newX, newY)]
    return result

def kruskals(rows, cols):
    # 1. Create list of Nodes:
    listOfNodes = []
    for r in range(rows):
        for c in range(cols):
            newNode = Node(r, c)
            listOfNodes.append(newNode)
    # [ Node(0, 0), Node(0, 1), Node(0, 2), Node(0, 3), Node(1, 0), ...]

    listOfConnectedNodes = []
    visited = [] # list of tuples

    while (getNumOfNodesThatAreConnected(listOfNodes, rows, cols) < rows*cols):
        # Step 1: pick a random node. 
        random.shuffle(listOfNodes)
        ourNode = listOfNodes[0]
        ourNode.listOfNeighbors += getNeighbors(listOfNodes, ourNode, rows, cols)
        random.shuffle(ourNode.listOfNeighbors)
        ourConnectingNode = ourNode.listOfNeighbors[0]

        if (ourConnectingNode[0], ourConnectingNode[1]) not in visited:
            # now we want to connect ourNode, ourConnectingNode
            elem = [(ourNode.row, ourNode.col), 
                    (ourConnectingNode[0], ourConnectingNode[1])]
            
            listOfConnectedNodes.append(elem)

            ourNode.isConnected = True
            for node in listOfNodes:
                if (node.row == ourConnectingNode[0] and 
                    node.col == ourConnectingNode[1]):
                    node.isConnected = True

            # and slowly we build up listOfConnectedNodes. 
            # we use this to draw our maze as well. 
            # [ [(node1R, node1C), (node2R, node2C)], [(), ()], ... ] 

        visited += [(ourConnectingNode[0], ourConnectingNode[1])]
    # finally, make sure there aren't any duplicates. 
    newListOfConnectedNodes = []
    for elem in listOfConnectedNodes:
        if elem not in newListOfConnectedNodes:
            newListOfConnectedNodes.append(elem)

    return newListOfConnectedNodes