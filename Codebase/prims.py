###############################################################################
# This file contains my implementation of Prim's algorithm

# Citation 6. Prim's Algorithm
    # My TP mentor Winston explained the algorithm to me on whiteboard. 
    # I also got help from Piazza: https://piazza.com/class/ksxdyap437e1yk?cid=4320
    # Didn't really use any supplemental materials like videos, code from online.

# Maze Generation w/ Prims's Algorithm. 

# A   B   C   D
# E   F   G   H
# I   J   K   L 
# M   N   O   P 

# Say we start from A. 
    # visited = [A]
    # possPaths = [AB, AE]
# We pick a random path from possPaths, say AB --> connect A and B
    # visited = [A, B]
    # possPaths = [AE, BC, BF]
# Let's try once again, picking BF. --> connect B and F
    # visited = [A, B, F]
    # possPaths = [AE, BC, FG, FJ, FE]
# Let's say we randomly picked FE out of possPaths.  --> connect F and E
    # visited = [A, B, F, E]
    # possPaths = [AE, BC, FG, FJ, EA, EI]
# Lastly, let's say we picked EA out of possPaths. --> connect E and A
    # the thing is, we can't do EA because that would form a square (bad)
    # what we can do before ever making these connections, 
    # is check if A is in visited. 
    # if A in visited:
        # choose a different path from possPaths
    # else:
        # make the connection with that path. 

# In short, before we decide on a path to take, we need to make sure the
# node it connects to is not already in visited. 
###############################################################################

import random
import copy

# Creates a 2d list of tuples (coordinates), given n rows and m cols
def makeBoardOfCoords(n, m):
    board = [ ([(0, 0)])*m for i in range(n) ]
    for row in range(n):
        for col in range(m):
            board[row][col] = (row, col)
    return board

def prims(board):
    visited = set()
    possPaths = [] # a possible path looks like [(0,0), (0,1)], for example. # IMPLEMENT THIS!!!!!
    finalListOfConnections = []
    # *note: a connection looks like: [(0,0), (0,1)], for example. 
    # so finalListOfConnections is a list of lists, each containing 2 tuples.

    start = board[0][0]
    end = board[ len(board)-1 ][ len(board[0])-1 ]

    visited.add(start)
    node = start
    possPaths += getAllNodePaths(board, node) # where node is like (x, y)

    while end not in visited:
        # let's pick a path from possPaths randomly. 
        random.shuffle(possPaths)
        ourPath = possPaths[0] # recall that a 'path' is a list of 2 tuples.

        # check if the latter tuple is not in visited
        if ourPath[1] not in visited:
            # we can make this path! 
            visited.add(ourPath[1])
            possPaths.remove(ourPath)
            possPaths += getAllNodePaths(board, ourPath[1])
            finalListOfConnections.append(ourPath)

        for pathIndex in range(len(possPaths)):
            path = possPaths[pathIndex]

        newPath = copy.copy(possPaths)
        for path in possPaths:
            if ((path[0][0] == 0 and path[1][0] == 0) or # top
                (path[0][1] == 0 and path[1][1] == 0) or # left
                (path[0][0] == len(board)-1 and path[1][0] == len(board)-1 ) or # bottom
                (path[0][1] == len(board[0])-1 and path[1][1] == len(board[0])-1)):  # right
                newPath.insert(0, path)

    return finalListOfConnections


# For a given node (x, y), this function will return a list of all of it's 
# possible paths (to adjacent nodes)
# For example, the result list may look like: [ [(0,0), (0, 1)], [...]] 
def getAllNodePaths(board, node):
    result = []
    x, y = node
    dXdY = [ (0, -1), (-1, 0), (0, 1), (1, 0) ]
    random.shuffle(dXdY)
    for (dx, dy) in dXdY:
        newX = x + dx
        newY = y + dy
        if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
            n = (x, y)
            t = (newX, newY) 
            lst = [n, t]
            result.append(lst)
    return result
