###############################################################################
# This file contains all the helper functions for gameMode_keyPressed
# Citation 3. Image Caching Code
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#cachingPhotoImages
    # Extend of what I copied: I directly copied the entire method 
    # getCachedPhotoImage so I could use it for my images
# 10: getCellBounds for my method alterRowCol
    # Snake: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    # While I didn't copy getCellBounds directly, I thought alterRowCol 
    # seemed very similar to getCellBounds in snake.
# Including:
    # reSpawnTA
    # alterRowCol (See Citation 10)
    # getCachedPhotoImage (See Citation 3)
    # keyPressedHelper
    # checkTAReachedOHQStudent
###############################################################################

from Leaderboard import *

def reSpawnTA(app, listOfTiles):
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / 19
    cellHeight = mazeHeight / 19
    x, y = 0, 0
    lowerX = app.margin + 4*cellWidth
    lowerY = app.margin + 4*cellHeight
    upperX = app.margin + 15*cellWidth
    upperY = app.margin + 15*cellHeight
    for i in range(len(listOfTiles)):
        (x0, y0, x1, y1) = listOfTiles[i]
        if lowerX < x0 < upperX and lowerY < y0 < upperY:
            x = x0 + (x1 - x0)/2
            y = y0 + (y1 - y0)/2
            break
    app.TA.playerX, app.TA.playerY = x, y

# See citation 10
def alterRowCol(app, row, col): # returns (x, y)
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    x = app.margin + row*cellWidth
    y = app.margin + col*cellHeight
    return (x, y)

def keyPressedHelper(app, event):
    # if 'h' is pressed, we instantly go into helpMode
    if (event.key == 'h'):
        app.mode = 'helpMode'
    elif (event.key == 'q'):
        app.mode = 'bonusMode'
        app.bonusPressed = True
        # we also want to move TA. 
        reSpawnTA(app, app.listOfTiles)
        app.accessToArrowKeysOff = False

    # if 's' is pressed, we show the solutions. 
    elif (event.key == 's'):
        app.drawSolutionBool = not app.drawSolutionBool

    # cell width and height:
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols

    if app.accessToArrowKeysOff == False:
        if event.key == "Left":
            isOnAPath = False
            app.TA.movePlayer(-10, 0)
            app.direction = event.key

            if (app.margin - 15 + 5 < app.TA.playerX < 
                app.width - (1.5*app.margin) + 20 - 5 and
                app.margin - 15 + 5 < app.TA.playerY < 
                app.height - (1.5*app.margin) + 20 - 5):

                for (x0, y0), (x1, y1) in app.listOfPaths:
                    if (min(x0, x1) + 15 <= app.TA.playerX <= max(x0, x1) + 15
                        and
                        min(y0, y1) <= app.TA.playerY <= max(y0, y1)):
                        isOnAPath = True
                        break    
                if isOnAPath == False:
                    app.TA.movePlayer(+10, 0)
                    app.direction = event.key

            # went too far left, off canvas. 
            if app.TA.playerX <= app.margin - 5:
                app.TA.movePlayer(10, 0)
                app.direction = event.key

                
        elif event.key == "Right":
            isOnAPath = False
            app.TA.movePlayer(+10, 0)
            app.direction = event.key

            if (app.margin - 15 + 5 < app.TA.playerX < 
                app.width - (1.5*app.margin) + 20 - 5 and
                app.margin - 15 + 5 < app.TA.playerY < 
                app.height - (1.5*app.margin) + 20 - 5):

                for (x0, y0), (x1, y1) in app.listOfPaths:
                    if (min(x0, x1) - 15 <= app.TA.playerX <= max(x0, x1) - 15 
                        and
                        min(y0, y1) <= app.TA.playerY <= max(y0, y1)):
                        # legal move
                        isOnAPath = True
                        break
                # at this point, we went through all paths
                # and found that we are not on a path
                # so we must be on a wall
                # undo move       
                if isOnAPath == False:
                    # the only exception is when we are at this little corner
                    # to get out of the maze. 
                    lowerX = 1.5*app.margin + ((app.cols-2.5)*cellWidth) + 5
                    lowerY = 1.5*app.margin + ((app.rows-3.5)*cellHeight) + 5
                    upperX = 1.5*app.margin + ((app.cols-2)*cellWidth) + 7
                    upperY = 1.5*app.margin + ((app.rows-3)*cellHeight) + 7

                    if (lowerX <= app.TA.playerX <= upperX and
                        lowerY <= app.TA.playerY <= upperY):
                        pass
                    else:
                        app.TA.movePlayer(-10, 0)
                        app.direction = event.key

        elif event.key == "Up":
            isOnAPath = False
            app.TA.movePlayer(0, -10)
            app.direction = event.key

            if (app.margin - 15 + 5 < app.TA.playerX < 
                app.width - (1.5*app.margin) + 20 - 5 and
                app.margin - 15 + 5 < app.TA.playerY < 
                app.height - (1.5*app.margin) + 20 - 5):

                for (x0, y0), (x1, y1) in app.listOfPaths:
                    if (min(x0, x1) <= app.TA.playerX <= max(x0, x1) and
                        min(y0, y1) + 15 <= app.TA.playerY <= max(y0, y1) + 15):
                        isOnAPath = True
                        break    
                if isOnAPath == False:
                    app.TA.movePlayer(0, +10)
                    app.direction = event.key

            if app.TA.playerY <= app.margin - 5:
                app.TA.movePlayer(0, +10)
                app.direction = event.key

        elif event.key == "Down":
            isOnAPath = False
            app.TA.movePlayer(0, +10)
            app.direction = event.key

            if (app.margin - 15 + 5 < app.TA.playerX < 
                app.width - (1.5*app.margin) + 20 - 5 and
                app.margin - 15 + 5 < app.TA.playerY < 
                app.height - (1.5*app.margin) + 20 - 5):

                for (x0, y0), (x1, y1) in app.listOfPaths:
                    if (min(x0, x1) <= app.TA.playerX <= max(x0, x1) and
                        min(y0, y1) - 15 <= app.TA.playerY <= max(y0, y1) - 15):
                        isOnAPath = True
                        break    
                if isOnAPath == False:
                    app.TA.movePlayer(0, -10)
                    app.direction = event.key
            if app.TA.playerY >= app.margin + ((app.rows-1)*cellHeight)- 10:
                app.TA.movePlayer(0, -10)
                app.direction = event.key

        else:
            pass

def checkTAReachedOHQStudent(app):
    # Checking if the TA reached the OHQ Student
    lowerX = app.ohqStudentX - 10
    upperX = app.ohqStudentX + 10
    lowerY = app.ohqStudentY - 40
    upperY = app.ohqStudentY + 40

    if (lowerX <= app.TA.playerX <= upperX and 
        lowerY <= app.TA.playerY <= upperY):
        # then that means the TA reached the OHQ Student
        # make the pop up show. 
        app.showPopUp = True
        app.accessToArrowKeysOff = True
        # at this point, we also need to save the score!!!!
        # app.name, app.health. 
        if app.bonusPressed == False:
            if app.addToLeaderboard == True:
                app.name = ""
                for (char, x) in app.value:
                    app.name += char
                addToLeaderboard(app.name, app.health)
                app.addToLeaderboard = False