###############################################################################
# This file contains all the helper functions for making a 'maze student' in main.py
# 1. Sprite sheets Code: 
    # TA led mini lecture on images/Pil: 
    # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    # Extend of what I copied: primarily just initImages.
# 10: getCellBounds for my method alterRowCol
    # Snake: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    # While I didn't copy getCellBounds directly, I thought alterRowCol 
    # seemed very similar to getCellBounds in snake.
# Including:
    # makeBackTrackerGhostStudent (see citation 1)
    # makeBackTrackerGhostStudent2 (see citation 1)
    # alterRowCol (see citation 10)
###############################################################################

from backtracker import *
import copy, time

def makeBackTrackerGhostStudent(app, taX, taY):
    app.t1 = time.time()
    # all we need to do is get a defined node
    # preferably in top right corner
    x, y = 0, 0
    for (x0, y0), (x1, y1) in app.originalListOfPaths:
        if 8 <= x0 <= 9 and 0 <= y0 <= 1:
            # then we found a node in the top right corner
            x = x0
            y = y0
            break
    if x == 0 and y == 0:
        # if none of those worked. 
        for (x0, y0), (x1, y1) in app.originalListOfPaths:
            if 6 <= x0 <= 9 and 0 <= y0 <= 3:
                # then we found a node in the top right corner
                x = x0
                y = y0
                break

    # node coords like (0, 0)
    app.backtrackerGhostXNode = x
    app.backtrackerGhostYNode = y

    # actual dimensions when drawing on canvas
    (app.backtrackerGhostX, app.backtrackerGhostY) = alterRowCol(app, x, y) 
    app.OGbacktrackerGhostX = app.backtrackerGhostX
    app.OGbacktrackerGhostY = app.backtrackerGhostY

    # for start: it's (x, y) not (row, col) ! (I know, super weird)
    app.listOfBacktrackerSolutionPaths = solution(app, app.originalListOfPaths, 
        (taX, taY), 
        (app.backtrackerGhostXNode, app.backtrackerGhostYNode))

    app.backtrackCoordPaths = copy.deepcopy(app.listOfBacktrackerSolutionPaths)

    if (app.listOfBacktrackerSolutionPaths != None and 
        app.backtrackCoordPaths != None):
        mazeWidth = app.width - 2*app.margin
        mazeHeight = app.height - 2*app.margin
        cellWidth = mazeWidth / app.rows
        cellHeight = mazeHeight / app.cols

        for i in range(len(app.listOfBacktrackerSolutionPaths)):
            currPath = app.listOfBacktrackerSolutionPaths[i]
            (x0, y0), (x1, y1) = currPath
            newX0 = app.margin + x0*cellWidth
            newY0 = app.margin + y0*cellHeight
            newX1 = app.margin + x1*cellWidth
            newY1 = app.margin + y1*cellHeight
            app.backtrackCoordPaths[i] = [(newX0, newY0), (newX1, newY1)]
            app.listOfBacktrackerSolutionPaths[i] = [(newX0 - 10, newY0 - 10), 
                                                     (newX1 + 10, newY1 + 10)]

    app.nodesToGo = []
    if app.backtrackCoordPaths != None:
        for (t1, t2) in app.backtrackCoordPaths:
            app.nodesToGo.append(t1)
        # AYOOO WE HAVE A VALID app.listOfBacktrackerSolutionPaths !!!!!
    app.nodesToGo2 = copy.copy(app.nodesToGo)

    # See citation 1
    app.ghostStudentImage = 'images/Student.png'
    app.ghostStudentImage = app.loadImage(app.ghostStudentImage)
    app.ghostStudentImage = app.scaleImage(app.ghostStudentImage, 0.05) 
    app.pastNodes = []
    app.lastNode = []

def makeBackTrackerGhostStudent2(app):
    app.t2 = time.time()
    # all we need to do is get a defined node
    # preferably in bottom Left corner
    x, y = 0, 0
    for (x0, y0), (x1, y1) in app.originalListOfPaths:
        if 0 <= x0 <= 2 and 7 <= y0 <= 9:
            x = x0
            y = y0
            break
    if x == 0 and y == 0:
        # if none of those worked. 
        for (x0, y0), (x1, y1) in app.originalListOfPaths:
            if 0 <= x0 <= 4 and 5 <= y0 <= 9:
                x = x0
                y = y0
                break

    # node coords like (0, 0)
    app.backtrackerGhostXNode2 = x
    app.backtrackerGhostYNode2 = y

    # actual dimensions when drawing on canvas
    (app.backtrackerGhostX2, app.backtrackerGhostY2) = alterRowCol(app, x, y) 

    # for start: it's (x, y) not (row, col) ! (I know, super weird)
    app.listOfBacktrackerSolutionPaths2 = solution(app, app.originalListOfPaths, 
        (0, 0), 
        (app.backtrackerGhostXNode2, app.backtrackerGhostYNode2))

    app.backtrackCoordPaths2 = copy.deepcopy(app.listOfBacktrackerSolutionPaths2)

    if (app.listOfBacktrackerSolutionPaths2 != None and 
        app.backtrackCoordPaths2 != None):
        mazeWidth = app.width - 2*app.margin
        mazeHeight = app.height - 2*app.margin
        cellWidth = mazeWidth / app.rows
        cellHeight = mazeHeight / app.cols

        for i in range(len(app.listOfBacktrackerSolutionPaths2)):
            currPath = app.listOfBacktrackerSolutionPaths2[i]
            (x0, y0), (x1, y1) = currPath
            newX0 = app.margin + x0*cellWidth
            newY0 = app.margin + y0*cellHeight
            newX1 = app.margin + x1*cellWidth
            newY1 = app.margin + y1*cellHeight
            app.backtrackCoordPaths2[i] = [(newX0, newY0), (newX1, newY1)]
            app.listOfBacktrackerSolutionPaths2[i] = [(newX0 - 10, newY0 - 10), 
                                                     (newX1 + 10, newY1 + 10)]

    app.nodesToGo2 = []
    if app.backtrackCoordPaths2 != None:
        for (t1, t2) in app.backtrackCoordPaths2:
            app.nodesToGo2.append(t1)

    app.ghostStudentImage = 'images/Student.png'
    app.ghostStudentImage = app.loadImage(app.ghostStudentImage)
    app.ghostStudentImage = app.scaleImage(app.ghostStudentImage, 0.05) 

# see citation 10
def alterRowCol(app, row, col): # returns (x, y)
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    x = app.margin + row*cellWidth
    y = app.margin + col*cellHeight
    return (x, y)