###############################################################################
# This file contains all the functions/helper functions classes. 
# Citation 1. Sprite sheets Code: 
    # TA led mini lecture on images/Pil: 
    # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    # Extend of what I copied: primarily just initImages.
# Including:
    # Board 
    # TA (contains initImages, see Citation 1)
    # OHQStudent
###############################################################################

from kruskals import *
from prims import *

class Board(object): 
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.usePrims = True

    def getBoardOfCoords(self):
        return makeBoardOfCoords(self.rows, self.cols)

    def getListOfPaths(self, board):
        if self.usePrims == True:
            return prims(board)
        else:
            return kruskals(self.rows, self.cols)

class TA(object):
    def __init__(self, playerX, playerY, spriteCounter):
        self.playerX = playerX
        self.playerY = playerY
        self.spriteCounter = spriteCounter
        self.sprites = {}
        self.direction = "Down"
        self.isMoving = False

    def movePlayer(self, dx, dy):
        self.spriteCounter = (self.spriteCounter + 1) % 4
        self.playerX += dx
        self.playerY += dy

    # **** See Citation 1 (on main.py)
    # This following method was copied entirely from
    # The TA led mini lecture on Images/Pil
    def initImages(self, spriteSheet):
        imageWidth, imageHeight = spriteSheet.size
        for direction in ("Down0", "Up1", "Left2", "Right3"):
            # the last char gives the index. 
            index = int(direction[-1]) 
            # eventhing (except last char) gives direction.
            newDir = direction[:-1] 
            topLefty = index * imageHeight / 4
            botRighty = (index + 1) * imageHeight / 4
            tempSprites = []
            for j in range(4):
                topLeftx = j * imageWidth / 4
                botRightx = (j + 1) * imageWidth / 4
                sprite = spriteSheet.crop((topLeftx, topLefty, 
                                            botRightx, botRighty))
                tempSprites.append(sprite)
            self.sprites[newDir] = tempSprites

class OHQStudent(object):
    def __init__(self):
        self.ohqStudentSprites = []
        self.ohqStudentSpriteCounter = 0
        self.ohqStudentX = 660
        self.ohqStudentY = 570

    def makeOHQStudent(self, image):
        ohqStudentImageWidth, ohqStudentImageHeight = image.size
        for i in range(4):
            cellWidth = ohqStudentImageWidth / 4
            topLeftX = i*cellWidth
            topLeftY = 0
            botRightX = (i+1)*cellWidth
            botRightY = ohqStudentImageHeight
            sprite = image.crop((topLeftX, topLeftY, botRightX, botRightY))
            self.ohqStudentSprites.append(sprite)