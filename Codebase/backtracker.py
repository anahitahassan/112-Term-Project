###############################################################################
# This file contains all the functions/helper functions for my backtracking 
# algorithm for maze solving.
# Citation 5. Backtracking/Recursion/Maze Solving
    # Inspired from Course Notes Recursion pt. 2
    # https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html#mazeSolving
    # I didn't actually copy anything, but I followed/was inspired by the 
    # general backtracking algorithm taught in the course material.
    # isLegal and getPossiblePaths were inspired by similar methods from the 
    # general backtracking algorithm
# Including:
    # solution 
    # solve (see citation 5 for backtracking/recursion)
    # getPossiblePaths
    # isLegal
###############################################################################

def solution(app, listOfPaths, start, end):
    start = start #(0, 0)
    end = end # (app.rows - 1, app.cols - 2)
    result = [] # note! contains paths not nodes
    return solve(listOfPaths, start[0], start[1], end[0], end[1], result)

# This uses recursion. 
def solve(listOfPaths, r, c, endR, endC, result):
    if (r, c) == (endR, endC):
        return result
    else:
        possPaths = getPossiblePaths(listOfPaths, r, c)
        for possPath in possPaths:
            result.append(possPath)
            if isLegal(result):
                # make no change since we already made the move. 
                lastPoint = result[-1][1]
                solution = solve(listOfPaths, lastPoint[0], lastPoint[1], 
                    endR, endC, result)
                if solution != None:
                    return solution
                # backtracking
                result.remove(possPath)
        return None

def getPossiblePaths(listOfPaths, r, c):
    result = []
    for (t1, t2) in listOfPaths:
        if t1 == (r, c):
            f = [t1, t2]
            result.append(f)
    return result

def isLegal(result):
    if len(result) == 0 or len(result) == 1: 
        return True
    lastPath = result[-1]
    secLastPath = result[-2]
    if secLastPath[1] == lastPath[0]:
        return True
    return False