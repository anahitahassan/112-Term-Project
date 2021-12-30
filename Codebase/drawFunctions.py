###############################################################################
# This file contains all the helper functions for gameMode__redrawAll
# Citation 1. Sprite sheets Code: 
    # TA led mini lecture on images/Pil: 
    # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    # Extend of what I copied: primarily just initImages.
# Citation 3. Image Caching Code
    # 15112 course notes (Animations Part 4)
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#cachingPhotoImages
    # Extend of what I copied: I directly copied the entire method 
    # getCachedPhotoImage so I could use it for my images
# Citation 4: All Images/Sprites
    # I copied these images from the internet and used them for the project:
    # 'idle-student-transparent' : https://www.artstation.com/artwork/48Q5Ok 
    # 'Student' : https://www.flaticon.com/free-icon/student_1046374 
    # 'spriteSheet-trans' : https://openclipart.org/detail/248259/retro-character-sprite-sheet 
        # 'spriteSheet-trans1.png' (Winston) The original avatar has a red 
        # shirt but I just took a blue marker in preview and covered the 
        # red with blue to replicate the 112 TA hoodies
        # 'spriteSheet-trans2.png' (Stephanie) I took the one above and 
        # used a dark brown marker for hair
# Citation 12: CMU 112 Graphics
    # Downloaded from: https://www.cs.cmu.edu/~112/notes/notes-graphics.html 
# Including:
    # # drawOHQStudent (See Citation 1 and 4 regarding sprites)
    # drawTA (See Citation 1 and 4 regarding sprites)
    # getCachedPhotoImage (See Citation 3)
    # drawColors
    # drawPKButtons
    # drawMazeWalls
    # drawSolution
    # drawTextAtTop
    # drawPopUpGameOver
    # drawGhostStudentSolution
    # drawGhostStudentSolution2
    # drawGhostStudentSolution3
    # drawHealth
    # drawPowerUp
###############################################################################

from cmu_112_graphics import * 

# See Citation 3
def getCachedPhotoImage(app, image):
    if ('cached PhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage

def drawColors(app, canvas):
    # Background color:
    canvas.create_rectangle(0, 0, app.width, app.height, fill="cadetblue2")
    # Background color of maze:
    canvas.create_rectangle(app.margin - 15, app.margin - 15, 
                            app.width - (1.5*app.margin) + 20 + 2, 
                            app.height - (1.5*app.margin) + 20 + 2, 
                            fill="Black", outline="Black")

def drawPKButtons(app, canvas):
    # Prim / Kruskal Buttons
    canvas.create_text(375, 700, text=
"""Generate a new maze with either  
  Prim's or Kruskals's algorithm.""", fill="Black")
    canvas.create_rectangle(250, 725, 350, 775, fill="Blue")
    canvas.create_text(300, 750, text="Prim's", fill="White")
    canvas.create_rectangle(400, 725, 500, 775, fill="Blue")
    canvas.create_text(450, 750, text="Kruskals's", fill="White")

def drawOHQStudent(app, canvas):
    # Idle Student Sprite Sheet Animation:
    ohqStudent = app.ohqStudentSprites[app.ohqStudentSpriteCounter]
    canvas.create_image(app.ohqStudentX, app.ohqStudentY, 
                        image=getCachedPhotoImage(app, ohqStudent))

def drawMazeWalls(app, canvas):
    # Creating the walls of the maze:
    for (x0, y0), (x1, y1) in app.listOfPaths:
        canvas.create_rectangle(x0, y0, x1, y1, 
              fill="cadetblue3", outline="cadetblue3")

def drawSolution(app, canvas):
    if app.drawSolutionBool == True:
        if app.listOfSolutionPaths != None:
            for (x0, y0), (x1, y1) in app.listOfSolutionPaths:
                canvas.create_rectangle(x0, y0, x1, y1, 
                    fill="light yellow", outline="light yellow")

# Note regarding sprites: see Citations 1 and 4. 
def drawTA(app, canvas):
    # TA Sprite Sheet Animation and Movement:
    spriteImage = app.sprites[app.direction][app.TA.spriteCounter]
    canvas.create_image(app.TA.playerX, app.TA.playerY, 
                        image=getCachedPhotoImage(app, spriteImage))

def drawTextAtTop(app, canvas):
    # Text at the top: 
    canvas.create_text(app.width/2, app.height/20, text=
"""                Press h for help.
          Press r to reset the game.
Press s for help (highlighted solutions path).""")

def drawPopUpGameOver(app, canvas):
    # Pop up if game over
    if app.showPopUp == True:
        canvas.create_rectangle(2*app.width/9, 3.75*app.height/9 - 20, 
                                7*app.width/9, 5.25*app.height/9, 
                                fill="Light Green")
        if app.health <= 0:
            canvas.create_text(app.width/2 - 20, app.height/2 - 35, 
                text="You're health is too low.")
            canvas.create_text(app.width/2 + 80, app.height/2 - 35, 
                text="FAIL", fill="Red", font="Times 15 bold underline")

        canvas.create_text(app.width/2, app.height/2, 
            text=
f"""You have reached the OHQ Student. Score = {app.health}
                  Press r to reset the game.
              Press q to play the bonus round.""", fill="Black")

def drawStartStopBoxes(app, canvas):
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    # start:
    lowerX = app.margin - 15
    lowerY = app.margin - 15
    upperX = app.margin - 15 + cellWidth*(4/7) - 1
    upperY = app.margin - 15 + cellHeight*(4/7) - 1
    canvas.create_rectangle(lowerX, lowerY, upperX, upperY, 
        fill="white", outline="white")
    # stop: 
    lowerX = 1.5*app.margin + ((app.cols-2.5)*cellWidth) + 5
    lowerY = 1.5*app.margin + ((app.rows-3.5)*cellHeight) + 5
    upperX = 1.5*app.margin + ((app.cols-2)*cellWidth) + 7
    upperY = 1.5*app.margin + ((app.rows-3)*cellHeight) + 7
    canvas.create_rectangle(lowerX, lowerY, upperX, upperY, 
        fill="white", outline="white")

# ghost solution from TA start point to some arbitrary node
def drawGhostStudentSolution(app, canvas):
    r = 10
    x = app.backtrackerGhostX
    y = app.backtrackerGhostY
    image = app.ghostStudentImage
    canvas.create_image(x, y, image=ImageTk.PhotoImage(image))

def drawGhostStudentSolution2(app, canvas):
    r = 10
    x = app.backtrackerGhostX2 - 5
    y = app.backtrackerGhostY2 
    image = app.ghostStudentImage
    canvas.create_image(x, y, image=ImageTk.PhotoImage(image))

def drawGhostStudentSolution3(app, canvas):
    if app.listOfBacktrackerSolutionPaths3 != None:
            for (x0, y0), (x1, y1) in app.listOfBacktrackerSolutionPaths3:
                canvas.create_rectangle(x0, y0, x1, y1, 
                    fill="light green", outline="light green")
    r = 10
    x = app.backtrackerGhostX3 + 5
    y = app.backtrackerGhostY3 
    image = app.ghostStudentImage
    canvas.create_image(x, y, image=ImageTk.PhotoImage(image))

def drawHealth(app, canvas):
    x = 6*app.width/7
    y = app.width/12
    r1 = 20
    r2 = 50
    canvas.create_rectangle(x - r2, y - r1, x + r2, y + r1, fill="pink")
    canvas.create_text(x, y, text=f'Health = {app.health}')
    if app.drawHealthMessage == True:
        canvas.create_text(x, y+30, text="-10 Health!", fill="Red", 
            font="Helvetica 20 bold")

def drawPowerUp(app, canvas):
    x = app.powerUpX 
    y = app.powerUpY 
    r = 10
    if app.reachedPowerUp == False:
        if app.drawPowerUp == True:
            canvas.create_oval(x - r, y - r, x + r, y + r, fill="Light Green")
            canvas.create_text(x, y, text="P")
    if app.reachedPowerUp == True:
        if app.drawPowerUpMessage == True:
            canvas.create_text(6*app.width/7 + 5, (app.width/12)-30, text="Power Up!", 
                fill="Blue", font="Helvetica 16 bold")