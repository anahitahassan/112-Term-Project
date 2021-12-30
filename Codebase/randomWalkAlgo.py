###############################################################################
# This file contains all the functions/helper functions for maze generation
# with the Random Walk Algo.

# 1. Sprite sheets Code: 
    # TA led mini lecture on images/Pil: 
    # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    # Extend of what I copied: primarily just initImages.
# 9: Random Walk Algorithm
    # Suggested by my TP mentor Winston : Random Walk Algorithm
    # I used this for the bonus round at the end. 
    # This was for maze generation
    # In the bonus round, the maze is noticably more 'loopy'
    # https://www.freecodecamp.org/news/how-to-make-your-own-procedural-dungeon-map-generator-using-the-random-walk-algorithm-e0085c8aa9a/
    # I used this aritcle as a guide and wrote the code myself.
###############################################################################

import random

# helper function that makes a 2d list / map of walls
# dim (dimensions) is both width and height of the map.
def make2dList(dim):
    L = [([1]*dim) for i in range(dim)]
    return L

def getRandomStartingPoint(L):
    dim = len(L)
    x = random.randint(0, dim - 1)
    y = random.randint(0, dim - 1)
    return (x, y)

def getRandomLength(maxLength):
    return random.randint(1, maxLength)

def getDirection():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    index = random.randint(0, len(directions) - 1)
    return directions[index]

# returns the map
def createMap(dimensions, maxTunnels, maxLength):
    map = make2dList(dimensions)
    lastDirection = [] # holds older randomDirection values
    
    # maxTunnels gets decremented
    (startX, startY) = getRandomStartingPoint(map)
    while maxTunnels != 0:
        # (startX, startY) = getRandomStartingPoint(map)
        randomDirection = getDirection()
        if lastDirection == []:
            lastDirection = randomDirection
        # if randomDirection = (0, 1), lastTurn can't be (0, -1)
        # if randomDirection = (1, 0), lastTurn can't be (-1, 0)
        while (lastDirection == [] or not
             ((randomDirection[0] == (-1)*lastDirection[0] and 
               randomDirection[1] == (-1)*lastDirection[1]) or
              (randomDirection[0] == lastDirection[0] and 
               randomDirection[1] == lastDirection[1]))):
            randomDirection = getDirection()
            # (startX, startY) = getRandomStartingPoint(map)
            # so we should have a randomDirection that satisfies the conditions. 
            randomLength = getRandomLength(maxLength)
            tunnelLength = 0

            while tunnelLength < randomLength:
                if (startX == 0 and randomDirection[0] == -1 or
                    startY == 0 and randomDirection[1] == -1 or
                    startX == dimensions - 1 and randomDirection[0] == 1 or 
                    startY == dimensions - 1 and randomDirection[1] == 1):
                    break
                else:
                    map[startX][startY] = 0
                    startX += randomDirection[0]
                    startY += randomDirection[1]
                    tunnelLength += 1
            # eventually we will break out of this loop
            # if we reach an edge
            # or if we max out the tunnel length

            # now what do we do?
            # check if tunnel is at least one block long. 
            if tunnelLength >= 1:
                lastDirection = randomDirection
                maxTunnels -= 1
    return map
