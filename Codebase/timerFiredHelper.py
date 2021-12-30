###############################################################################
# This file contains all the helper functions for gameMode_timerFired
# Citation 1. Sprite sheets Code: 
    # TA led mini lecture on images/Pil: 
    # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    # Extend of what I copied: primarily just initImages.
# Including:
    # checkIfTAChosen 
    # sprites (See citation 1 for sprite code)
    # moveBacktrackerGhost
    # moveBacktrackerGhost2
    # alterRowCol
    # checkIfTAOverNode
    # updateHealth
    # checkIfTAOverPowerUp
###############################################################################

from makeMazeStudent import *
import copy, time

def checkIfTAChosen(app):
    if app.ta == 'winston':
        app.taImage = 'images/spriteSheet-trans1.png'
        app.taImage = app.loadImage(app.taImage)
        app.taImage = app.scaleImage(app.taImage, 0.25) 
        app.TA.initImages(app.taImage)
    elif app.ta == 'stephanie':
        app.taImage = 'images/spriteSheet-trans2.png'
        app.taImage = app.loadImage(app.taImage)
        app.taImage = app.scaleImage(app.taImage, 0.25) 
        app.TA.initImages(app.taImage)

# (See citation 1 for sprite code)
def sprites(app):
    # ohq Student sprite counter
    app.ohqStudentSpriteCounter = ( (1 + app.ohqStudentSpriteCounter) 
                                      % len(app.ohqStudentSprites) )
    # ta sprite counter
    if app.isMoving:
        app.TA.spriteCounter = (app.TA.spriteCounter + 1) % 4
    else:
        app.TA.spriteCounter = 0

def moveBacktrackerGhost(app):
    # nodesToGo: the next node to go to is at the end of the list. 
    # so if we reach a power up, we want to take a step back. we would need to 
    # append that node to app.nodesToGo
    # we should keep track of nodes we went to. (app.pastNodes)
    if app.reachedPowerUp == True:
        app.nodesToGo.append(app.lastNode)
        app.nodesToGo.append(app.lastNode)
        app.reachedPowerUp = False
    if app.nodesToGo != []:
        cop = copy.deepcopy(app.nodesToGo) 
        if time.time() - app.t1 > 0.5:
            if cop != []:
                start = (app.backtrackerGhostX, app.backtrackerGhostY)
                end = cop[-1]
                #app.pastNodes.append(end)
                app.lastNode = end
                # if going down or up (x is same)
                if start[0] == end[0]:
                    h = abs(start[1]-end[1])
                    # if going down. 
                    if end[1] >= start[1]:
                        app.backtrackerGhostY += h 
                    # if going up. 
                    else: 
                        app.backtrackerGhostY -= h 
                # if going left or right (y is same)
                else: # elif start[1] == end[1]:
                    h = abs(start[0]-end[0])
                    # if going left. 
                    if end[0] <= start[0]:
                        app.backtrackerGhostX -= h 
                    # if going right. 
                    else: 
                        app.backtrackerGhostX += h 
                app.t1 = time.time()
                cop.pop()
                app.nodesToGo = cop

def moveBacktrackerGhost2(app):
    if app.reachedPowerUp == True:
        app.nodesToGo2.append(app.lastNode)
        app.nodesToGo.append(app.lastNode)
        app.reachedPowerUp = False
    if app.nodesToGo2 != []:
        cop = copy.deepcopy(app.nodesToGo2) 
        if time.time() - app.t2 > 0.5:
            if cop != []:
                start = (app.backtrackerGhostX2, app.backtrackerGhostY2)
                end = cop[-1]

                # if going down or up (x is same)
                if start[0] == end[0]:
                    h = abs(start[1]-end[1])
                    # if going down. 
                    if end[1] >= start[1]:
                        app.backtrackerGhostY2 += h 
                    # if going up. 
                    else: 
                        app.backtrackerGhostY2 -= h 
                # if going left or right (y is same)
                else: # elif start[1] == end[1]:
                    h = abs(start[0]-end[0])
                    # if going left. 
                    if end[0] <= start[0]:
                        app.backtrackerGhostX2 -= h 
                    # if going right. 
                    else: 
                        app.backtrackerGhostX2 += h 
                app.t2 = time.time()
                cop.pop()
                app.nodesToGo2 = cop
    updateHealth(app)
    checkIfTAOverPowerUp(app)

def alterRowCol(app, row, col): # returns (x, y)
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    x = app.margin + row*cellWidth
    y = app.margin + col*cellHeight
    return (x, y)
    
def checkIfTAOverNode(app):
    lstOfAllPossibleNodes = []
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    for i in range(app.cols):
        for j in range(app.rows):
            nodeX = app.margin + i*cellWidth
            nodeY = app.margin + j*cellHeight
            node = (nodeX, nodeY)
            lstOfAllPossibleNodes.append(node)
    possX = app.margin
    possY = app.margin
    for (nodeX, nodeY) in app.nodesToGo:
        if (possX - 5 <= nodeX <= possX + 5 and 
            possY - 5 <= nodeY <= possY + 5):
            app.nodesToGo.remove((nodeX, nodeY))
            break
    for (nodeX, nodeY) in app.nodesToGo2:
        if (possX - 5 <= nodeX <= possX + 5 and 
            possY - 5 <= nodeY <= possY + 5):
            app.nodesToGo2.remove((nodeX, nodeY))
            break
    x = 0
    y = 0
    for (nodeX, nodeY) in lstOfAllPossibleNodes:
        if (nodeX - 10 <= app.TA.playerX <= nodeX + 10 and
            nodeY - 10 <= app.TA.playerY <= nodeY + 10):
            # this means the TA is at a node. 
            x = nodeX
            y = nodeY
            node = (x, y)
            if node in app.nodesToGo:
                app.nodesToGo.remove(node)
            app.nodesToGo.insert(0, node)
            if node in app.nodesToGo2:
                app.nodesToGo2.remove(node)
            app.nodesToGo2.insert(0, node)
            break
    if x == 0 and y == 0:
        pass

def updateHealth(app):
    app.drawHealthMessage = False
    # check if TA's location is same as ghost location. (or within 20)
    if (app.backtrackerGhostX - 20 <= app.TA.playerX 
        <= app.backtrackerGhostX + 20 and 
        app.backtrackerGhostY - 20 <= app.TA.playerY 
        <= app.backtrackerGhostY + 20):
        app.health -= 10
        app.drawHealthMessage = True

def checkIfTAOverPowerUp(app):
    app.drawPowerUpMessage = False
    if (app.TA.playerX - 10 <= app.powerUpX <= app.TA.playerX + 10 and
        app.TA.playerY - 10 <= app.powerUpY <= app.TA.playerY + 10):
        app.drawPowerUp = False # when we reach powerUp. 
        app.reachedPowerUp = True
        app.drawPowerUpMessage = True
        # if this is true, the student will automatically go back to where it 
        # originally spawned. 