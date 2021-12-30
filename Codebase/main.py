# CITATIONS:
    # 1. Sprite sheets Code: 
        # TA led mini lecture on images/Pil: 
        # https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=249eb6cc-06ee-450b-8d1e-adda0085dd69 
        # 15112 course notes (Animations Part 4)
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
        # Extend of what I copied: primarily just initImages.

    # 2. Modes/Screens Code: 
        # 15112 course notes (Animations Part 4)
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes 
        # Extend of what I copied: I was inspired by the code on modes and 
        # esentially wrote my modes by myself but I used this code as a 
        # reference/guide. 

    # 3. Image Caching Code
        # 15112 course notes (Animations Part 4)
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#cachingPhotoImages
        # Extend of what I copied: I directly copied the entire method 
        # getCachedPhotoImage so I could use it for my images

    # 4: All Images/Sprites
        # I copied these images from the internet and used them for the project:
        # 'idle-student-transparent' : https://www.artstation.com/artwork/48Q5Ok 
        # 'Student' : https://www.flaticon.com/free-icon/student_1046374 
        # 'spriteSheet-trans' : https://openclipart.org/detail/248259/retro-character-sprite-sheet 
            # 'spriteSheet-trans1.png' (Winston) The original avatar has a red 
            # shirt but I just took a blue marker in preview and covered the 
            # red with blue to replicate the 112 TA hoodies
            # 'spriteSheet-trans2.png' (Stephanie) I took the one above and 
            # used a dark brown marker for hair

    # 5. Backtracking/Recursion/Maze Solving
        # Inspired from Course Notes Recursion pt. 2
        # https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html#mazeSolving
        # I didn't actually copy anything, but I followed/was inspired by the 
        # general backtracking algorithm taught in the course material.

    # 6. Prim's Algorithm
        # My TP mentor Winston explained the algorithm to me on whiteboard. 
        # I also got help from Piazza: https://piazza.com/class/ksxdyap437e1yk?cid=4320
        # Didn't really use any supplemental materials like videos, code from online.

    # 7. Kruskals's Algorithm
        # Also suggested by my TP mentor Winston
        # I watched the following Youtube videos to understand/visualize the 
        # concept, but all code was written by myself.
        # https://www.youtube.com/watch?v=4ZlRH0eK-qQ&t=1011s
        # https://www.youtube.com/watch?v=8pJKJBdOMME
        # https://www.youtube.com/watch?v=LRM-xGmyQNg 

    # 8: Accessing .txt files
        # https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
        # https://www.pythontutorial.net/python-basics/python-read-text-file/ 
        # I wrote my code up myself using help from this article, read about 
        # open, readlines(), write, and close. 

    # 9: Random Walk Algorithm
        # Suggested by my TP mentor Winston : Random Walk Algorithm
        # I used this for the bonus round at the end. 
        # This was for maze generation
        # In the bonus round, the maze is noticably more 'loopy'
        # https://www.freecodecamp.org/news/how-to-make-your-own-procedural-dungeon-map-generator-using-the-random-walk-algorithm-e0085c8aa9a/
        # I used this aritcle as a guide and wrote the code myself.

    # 10: getCellBounds for my method alterRowCol
        # Snake: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
        # While I didn't copy getCellBounds directly, I thought alterRowCol 
        # seemed very similar to getCellBounds in snake.

    # 11: rgbString(r, g, b)
        # copied directly from https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors 
        # so I could use more colors.

    # 12: CMU 112 Graphics
        # Downloaded from: https://www.cs.cmu.edu/~112/notes/notes-graphics.html 

from cmu_112_graphics import * 
from timerFiredHelper import *
from keyPressedHelper import *
from makeMazeStudent import *
from randomWalkAlgo import *
from drawFunctions import *
from backtracker import *
from Leaderboard import *
from classes import *
#from modes import *
import time

################################################################################
# Home Screen Mode
################################################################################

def homeScreenMode_keyPressed(app, event):
    # If any key is pressed, we instantly go into gameMode
    if event.key == "1":
        # app.mode = 'gameMode'
        app.mode = 'pickYourTAMode'
    helper_keyPressed(app, event)
    
def helper_keyPressed(app, event):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if event.key in alphabet:
        # location of last letter:
        if app.value == []:
            app.textX += 10
            t = (event.key, app.textX)
            app.value.append(t)
            app.cursorX += 10
        else:
            lastLetterX = app.value[-1][1]

            if app.cursorX > lastLetterX:
                app.textX += 10
                t = (event.key, app.textX)
                app.value.append(t)
                app.cursorX += 10
            else:
                app.textX += 10
                app.cursorX += 10
                # what textcursor is inbetween two letters?
                index = 0
                while index < len(app.value) - 1:
                    # if text cursor is inbetween letters. 
                    if app.value[index][1] < app.cursorX < app.value[index+1][1]:
                        moveRightAhead(app, index)
                        t = (event.key, app.textX)
                        app.value.insert(index+1, t)
                        break
                    index += 1

    if event.key == "Space":
        app.textX += 10
        t = (" ", app.textX)
        app.value.append(t)
        app.cursorX += 10
    if event.key == "Delete":
        # it depends on where the text cursor is...
        currMaxX = app.value[-1][1]
        if app.cursorX > currMaxX:
            app.value.pop()
        index = 0
        while index < len(app.value) - 1:
            # if text cursor is inbetween letters. 
            if app.value[index][1] <= app.cursorX <= app.value[index+1][1]:
                (char, x) = app.value[index]
                app.value.pop(index)
                # but for all the letters after, we need to move them back. 
                moveRightBack(app, index)
                app.textX = x
            index += 1
        app.textX -= 10
        app.cursorX -= 10
    if event.key == "Left":
        app.cursorX -= 10
    if event.key == "Right":
        app.cursorX += 10
    if event.key == "Enter":
        app.done = True
        for (char, x) in app.value:
            app.name += char

def moveRightBack(app, index):
    for i in range(index, len(app.value)):
        tup = app.value[i]
        (char, x) = tup
        x -= 10
        tup = (char, x)
        app.value[i] = tup

def moveRightAhead(app, index):
    for i in range(index, len(app.value)):
        tup = app.value[i]
        (char, x) = tup
        x += 10
        tup = (char, x)
        app.value[i] = tup

def homeScreenMode_timerFired(app):
    if abs(time.time() - app.t0) > 0.5:
        app.showCursor = not app.showCursor
        app.t0 = time.time()

def homeScreenMode_mousePressed(app, event):
    app.cursorX = event.x + 10
    app.textX = event.x 
    app.cursorY = app.textY = event.y

# CITATION 11
# from: https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors 
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def homeScreenMode_redrawAll(app, canvas):
    rustyPurple = rgbString(210, 195, 216)
    mediumPurple = rgbString(169, 154, 196)
    darkPurple = rgbString(48, 25, 52)
    pink = rgbString(243, 218, 219)
    bolderPink = rgbString(248, 203, 209)
    beige = rgbString(246, 242, 236)
    darkerBeige = rgbString(247, 229, 215)
    brown = rgbString(92, 63, 51)
    homeScreenMode_drawWelcome(app, canvas, rustyPurple, mediumPurple, darkPurple)
    homeScreenMode_drawRules(app, canvas, bolderPink, pink, darkPurple)
    homeScreenMode_drawTextEditor(app, canvas, darkerBeige)
    homeScreenMode_drawLeaderboard(app, canvas, beige, darkerBeige, brown)

def homeScreenMode_drawWelcome(app, canvas, rustyPurple, mediumPurple, darkPurple):
    # Background Color:
    canvas.create_rectangle(0, 0, app.width, app.height, fill=rustyPurple)
    # Block 1: Welcome
    canvas.create_rectangle(app.width/2 - 200, 25, 
                            app.width/2 + 200, 125, 
                            fill=mediumPurple, outline=darkPurple)
    canvas.create_text(app.width/2, 75, 
        text=
"""     Welcome to 
112 TA Simulator!""", font="Times 35 bold italic", fill=darkPurple)

def homeScreenMode_drawRules(app, canvas, bolderPink, pink, darkPurple):
    # Block 2: Rules
    canvas.create_rectangle(0 + 50, 145, 
                            app.width - 50, app.height/2 - 50, 
                            fill=pink, outline=bolderPink)

    canvas.create_text(app.width/2, app.height/2 - 150, 
text = """
Rules:
- You are a 112 TA at Office Hours. In order to get to the student at the top of the Office Hour Queue, you must go through a maze and 
  find them at the end. However, throughout the maze are students, who are not on the OHQ, and they want to bug you with questions. 
  You must avoid them and get to the end of the maze as fast as you can without bumping into any students in the maze. 
- You begin with 20 health, each time you bump into a student in the maze, -10 health. 
- However, if you run into a powerup, the maze students temporarily freeze.  
- You can pick which algorithm you want to generate the maze (Prim's/Kruskal's)
- Press 'r' to reset the game, and press 's' to show the highlighted solution.
- Press 'h' for additional shortcut help. 
How to begin the game:
- Enter your name in the text editor below. 
- Press 1 to begin the game. 
""", font="Times 12", fill=darkPurple)

def homeScreenMode_drawTextEditor(app, canvas, darkerBeige):
    # Block 3: Name
    canvas.create_rectangle(50 - 5, 400 - 5, 400 + 5, 760 + 5, fill=darkerBeige) 
    canvas.create_rectangle(50, 400, 400, 760, fill=darkerBeige)     

    canvas.create_text(app.width/10, app.textY -25, anchor='w',
            text=f"""Begin by entering your 
name in this text editor""", font="Courier 14")
    # draw text:
    for (char, x) in app.value:
        canvas.create_text(x , app.textY + 10, text=char, 
            font="Courier 20")
    # draw cursor:
    if app.showCursor == True:
        canvas.create_line(app.cursorX, app.cursorY, 
                        app.cursorX, app.cursorY + 20, width=2, fill="Green")
    if app.done == True:
        canvas.create_text(app.width/10, app.textY + 30, anchor='w',
            text=f"You entered {app.name}", font="Courier 14")
        canvas.create_text(app.width/10, app.textY + 60, anchor='w',
            text=f"""Press 1 to pick your 
TA, {app.name}.""", font="Courier 14")

def homeScreenMode_drawLeaderboard(app, canvas, beige, darkerBeige, brown):
    # Block 4: Leaderboard
    # x dimensions 250 - 550 
    # y dimensions 400 - 760
    canvas.create_rectangle(250 + 200, 400, 550 + 200, 760, fill=beige, outline=brown)
    canvas.create_rectangle(250 + 200, 400, 550 + 200, 460, fill=darkerBeige, outline=brown)
    canvas.create_text(400 + 200, 415, text="Leaderboard", fill=brown)

    # divider between number and names
    canvas.create_line(300 + 200, 430, 300 + 200, 760, fill=brown)

    # divider between names and scores
    canvas.create_line(450 + 200, 430, 450 + 200, 760, fill=brown)

    # we want to draw this line multiple times 
    canvas.create_line(250 + 200, 430, 550 + 200, 430, fill=brown)
    canvas.create_text(275 + 200, 430 + 15, text="Rank", fill=brown)
    canvas.create_text(375 + 200, 430 + 15, text="Name", fill=brown)
    canvas.create_text(500 + 200, 430 + 15, text="Score", fill=brown)

    y = 460
    num = 1
    for i in range(10):
        canvas.create_line(250 + 200, y, 550 + 200, y, fill=brown)
        canvas.create_text(275 + 200, y + 15, text=num, fill=brown)
        y += 30
        num += 1
    canvas.create_line(250 + 200, y, 550, y, fill=brown)

    lst = getTop10()
    y = 460
    for elem in lst: # [name, score]
        # name:
        canvas.create_text(375 + 200, y + 15, text=elem[0], fill=brown)
        canvas.create_text(500 + 200, y + 15, text=elem[1], fill=brown)
        y += 30

################################################################################
# Help Mode
################################################################################

def helpMode_keyPressed(app, event):
    # If any key is pressed, we go BACK to gameMode
    app.mode = 'gameMode'

def helpMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="light green")
    canvas.create_text(app.width/2, app.height/10, 
        text='This is the Help Screen', font='Times 24 bold')
    font = 'Times 12 bold'
    canvas.create_text(app.width/2, 2*app.height/10, text='Rules', 
        font='Times 16 bold')
    canvas.create_text(app.width/2 + 10, app.height/2 - 150, text = 
"""
    - You are a 112 TA at Office Hours. In order to get to the student at the top of the Office Hour Queue, you must 
      go through a maze and find them at the end. However, throughout the maze are students, who are not on the OHQ, 
      and they want to bug you with questions. You must avoid them and get to the end of the maze as fast as you can 
      without bumping into any students in the maze. 
    - You begin with 20 health, each time you bump into a student in the maze, -10 health. 
    - However, if you run into a powerup, the maze students temporarily freeze.  
    - You can pick which algorithm you want to generate the maze (Prim's/Kruskal's)
    - Press 'r' to reset the game, and press 's' to show the highlighted solution.
    - Press 'h' for additional shortcut help. 
""", font=font)

    canvas.create_text(app.width/2, app.height/2, text='Shortcut commands', 
        font='Times 16 bold')
    canvas.create_text(app.width/2, app.height/2 + 150, text=
""" 
    Game Mode:
    - 'r' = resets the bonus round/maze
    - 's' = shows the highlighted solutions path
    - 'h' = goes to the help screen
    - Left arrow key = moves TA left
    - Right arrow key = moves TA right
    - Up arrow key = moves TA up
    - Down arrow key = moves TA down

    Bonus Mode:
    - 'r' = resets the bonus round/maze
    - 'h' = goes back to Home Screen Mode
    - Left arrow key = moves TA left
    - Right arrow key = moves TA right
    - Up arrow key = moves TA up
    - Down arrow key = moves TA down
""", font=font)

    canvas.create_text(app.width/2, 9*app.height/10, 
        text='Press any key to return back to the game!', font=font)

################################################################################
# Pick Your TA Mode
################################################################################

def pickYourTAMode_keyPressed(app, event):
    # If any key is pressed, we go BACK to gameMode
    app.mode = 'gameMode'

def pickYourTAMode_mousePressed(app, event):
    # if clicked on winston
    if (app.width/3 - 20 <= event.x <= app.width/3 + 20 and
        app.height/2 - 25 <= event.y <= app.height/2 + 30):
        app.ta = 'winston'
    # if clicked on stephanie
    if (2*app.width/3 - 20 <= event.x <= 2*app.width/3 + 20 and
        app.height/2 - 25 <= event.y <= app.height/2 + 30):
        app.ta = 'stephanie'

def pickYourTAMode_redrawAll(app, canvas):
    darkerBeige = rgbString(247, 229, 215)
    canvas.create_rectangle(0, 0, app.width, app.height, fill=darkerBeige)

    canvas.create_text(app.width/2, app.height/6, 
        text="Pick Your TA!", font="Times 20")
    canvas.create_text(app.width/2, app.height/6 + 20, 
        text="Click the TA to select.", font="Times 20")

    canvas.create_text(app.width/3, app.height/2 - 50, text="Winston", 
        font="Times 20")
    canvas.create_text(2*app.width/3, app.height/2 - 50, text="Stephanie", 
        font="Times 20")

    canvas.create_oval(app.width/3 - 20, app.height/2 + 25, 
                       app.width/3 + 20, app.height/2 + 35, 
                       fill="grey", outline="grey")

    canvas.create_oval(2*app.width/3 - 20, app.height/2 + 25, 
                       2*app.width/3 + 20, app.height/2 + 35, 
                       fill="grey", outline="grey")

    # see citation 3
    canvas.create_image(app.width/3, app.height/2, 
        image=getCachedPhotoImage(app, app.winstonIcon))
    canvas.create_image(2*app.width/3, app.height/2, 
        image=getCachedPhotoImage(app, app.stephanieIcon))
    
    if app.ta != "":
        canvas.create_text(app.width/2, 4*app.height/5, 
            text=f'You selected {app.ta}!', font="Times 20")
        canvas.create_text(app.width/2, 4*app.height/5 + 20, 
            text='Press any key to begin the game. ', 
            font="Times 20")

##########################################
# Bonus Mode
##########################################

def bonusMode_appStarted(app):
    app.margin = 125
    app.map = createMap(19, 60, 12)
    app.init = time.time()
    app.seconds = 20
    app.timeUp = False
    app.original = app.health
    app.accessToArrowKeysOff = False

def removeStudent(app):
    # go through list of all tiles. 
    # if TA is on center of a tile, delete the student
    for (x0, y0, x1, y1) in app.listOfTiles:
        tileCenterX = x0 + (x1 - x0)/2
        tileCenterY = y0 + (y1 - y0)/2
        if (tileCenterX - 10 <= app.TA.playerX <= tileCenterX + 10 and
            tileCenterY - 10 <= app.TA.playerY <= tileCenterY + 10):
            # get the listOfStudents. 
            # we have a certain x and y. 
            for i in range(len(app.listOfStudents)):
                (x, y) = app.listOfStudents[i]
                if (x == tileCenterX and y == tileCenterY):
                    # erase that student. 
                    app.listOfStudents.pop(i)
                    app.health += 1
                    break

def keyPressedHelperBonus(app, event):
    if event.key == "Left":
        isOnAPath = False
        app.TA.movePlayer(-10, 0)
        app.direction = event.key
        if (app.margin < app.TA.playerX < app.width - app.margin and
            app.margin < app.TA.playerY < app.height - app.margin):
            for (x0, y0, x1, y1) in app.listOfTiles:
                if (min(x0, x1) + 5 <= app.TA.playerX <= max(x0, x1) + 5 and
                    min(y0, y1) <= app.TA.playerY <= max(y0, y1)):
                    isOnAPath = True
                    break
            if isOnAPath == False:
                    app.TA.movePlayer(10, 0)
                    app.direction = event.key
        # went too far left, off canvas. 
        if app.TA.playerX <= app.margin:
            app.TA.movePlayer(10, 0)
            app.direction = event.key
                
    elif event.key == "Right":
        isOnAPath = False
        app.TA.movePlayer(+10, 0)
        app.direction = event.key
        if (app.margin < app.TA.playerX < app.width - app.margin and
            app.margin < app.TA.playerY < app.height - app.margin):
            for (x0, y0, x1, y1) in app.listOfTiles:
                if (min(x0, x1) - 5 <= app.TA.playerX <= max(x0, x1) - 5 and
                    min(y0, y1) <= app.TA.playerY <= max(y0, y1)):
                    isOnAPath = True
                    break
            if isOnAPath == False:
                    app.TA.movePlayer(-10, 0)
                    app.direction = event.key
        # went too far right, off canvas. 
        if app.TA.playerX >= app.width - app.margin:
            app.TA.movePlayer(-10, 0)
            app.direction = event.key

    elif event.key == "Up":
        isOnAPath = False
        app.TA.movePlayer(0, -10)
        app.direction = event.key
        if (app.margin < app.TA.playerX < app.width - app.margin and
            app.margin < app.TA.playerY < app.height - app.margin):
            for (x0, y0, x1, y1) in app.listOfTiles:
                if (min(x0, x1) <= app.TA.playerX <= max(x0, x1) and
                    min(y0, y1) + 5 <= app.TA.playerY <= max(y0, y1) + 5):
                    isOnAPath = True
                    break
            if isOnAPath == False:
                    app.TA.movePlayer(0, +10)
                    app.direction = event.key
        # went too far up, off canvas. 
        if app.TA.playerY <= app.margin:
            app.TA.movePlayer(0, +10)
            app.direction = event.key

    elif event.key == "Down":
        isOnAPath = False
        app.TA.movePlayer(0, +10)
        app.direction = event.key
        if (app.margin < app.TA.playerX < app.width - app.margin and
            app.margin < app.TA.playerY < app.height - app.margin):
            for (x0, y0, x1, y1) in app.listOfTiles:
                if (min(x0, x1) <= app.TA.playerX <= max(x0, x1) and
                    min(y0, y1) - 5 <= app.TA.playerY <= max(y0, y1) - 5):
                    isOnAPath = True
                    break
            if isOnAPath == False:
                    app.TA.movePlayer(0, -10)
                    app.direction = event.key
        # went too far down, off canvas. 
        if app.TA.playerY >= app.height - app.margin:
            app.TA.movePlayer(0, -10)
            app.direction = event.key
    else:
        pass

def bonusMode_keyPressed(app, event):
    if event.key == 'r':
        app.health = app.original
        bonusMode_appStarted(app)
        reSpawnTA(app, app.listOfTiles)
        makeListOfTiles(app)
        makeBonusStudents(app)
        app.accessToArrowKeysOff = False
    if event.key == 'h':
        appStarted(app)
    if app.accessToArrowKeysOff == False:
        keyPressedHelperBonus(app, event)

def bonusMode_timerFired(app):
    removeStudent(app)
    if app.seconds != 0:
        if time.time() - app.init > 1:
            app.seconds -= 1
            app.init = time.time()
    else:
        app.timeUp = True
        app.accessToArrowKeysOff = True
        if app.bonusPressed == True:
            if app.addToLeaderboard == False:
                app.name = ""
                for (char, x) in app.value:
                    app.name += char
                addToLeaderboard(app.name, app.health)
                app.addToLeaderboard = True

def bonusMode_mousePressed(app, event): 
    pass

def bonusMode_drawTiles(app, canvas):
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / 19
    cellHeight = mazeHeight / 19

    for i in range(19):
        for j in range(19):
            topX = app.margin + i*cellWidth
            topY = app.margin + j*cellHeight
            botX = app.margin + (i+1)*cellWidth
            botY = app.margin + (j+1)*cellHeight
            if app.map[i][j] == 0:
                canvas.create_rectangle(topX, topY, botX, botY, fill="light blue")
    x = app.width/2
    y = app.height/2

def bonusMode_drawStudents(app, canvas):
    for (x, y) in app.listOfStudents:
        #canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="light green")
        canvas.create_image(x, y, image=getCachedPhotoImage(app, app.bonusStudent))


def bonusMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="cadetblue2")
    canvas.create_text(app.width/2, app.height/15, text="""
              Bonus round!
For every student you get to, 
you get an extra +1 health!""", font = "Times 20")

    canvas.create_text(app.width/4, 14*app.height/15 - 20, 
        text="Press r to reset game.")
    canvas.create_rectangle(app.width/2 - 50, 14*app.height/15 - 40, 
                            app.width/2 + 60, 14*app.height/15, 
                            fill="cadetblue3")
    canvas.create_text(app.width/2, 14*app.height/15 - 20, 
        text=f"Health = {app.health}", fill="Black", font="Times 16")
    canvas.create_text(3*app.width/4, 14*app.height/15 - 20, 
        text=f"Timer: {app.seconds} ", font="Times 20")

    canvas.create_rectangle(app.margin, app.margin, 
                            app.width - (app.margin), 
                            app.height - (app.margin), 
                            fill="Black", outline="Black")
    bonusMode_drawTiles(app, canvas)
    bonusMode_drawStudents(app, canvas)
    drawTA(app, canvas)
    if app.timeUp == True:
        drawTimeUpPopUp(app, canvas)

def drawTimeUpPopUp(app, canvas):
    canvas.create_rectangle(app.width/2 - 200, app.height/2 - 80, 
                            app.width/2 + 200, app.height/2 + 90, 
                            fill="Beige")
    canvas.create_text(app.width/2, app.height/2 - 20, text="Time up!", 
        font="Times 20")
    canvas.create_text(app.width/2, app.height/2, 
        text=f"Health = {app.health}", font="Times 20")
    canvas.create_text(app.width/2, app.height/2 + 20, 
        text=f"Press h to go back to the Home Screen.", font="Times 20")


def drawTA(app, canvas):
    # TA Sprite Sheet Animation and Movement:
    spriteImage = app.sprites[app.direction][app.TA.spriteCounter]
    canvas.create_image(app.TA.playerX, app.TA.playerY, 
                        image=getCachedPhotoImage(app, spriteImage))

def getCachedPhotoImage(app, image):
    # this allows it to run much faster 
    # stores cached version
    if ('cached PhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage







##########################################
# Game Mode
##########################################

def gameMode_mousePressed(app, event):
    # Prim's button: 250, 725, 350, 775
    if (250 <= event.x <= 350 and 725 <= event.y <= 775):
        usePrims = True
        removeMaze(app)
    # Kruskals's button: 400, 725, 500, 775
    if (400 <= event.x <= 500 and 725 <= event.y <= 775):
        usePrims = False
        removeMaze(app)

def gameMode_keyPressed(app, event):
    keyPressedHelper(app, event)
    checkTAReachedOHQStudent(app)
    # if 'r' is pressed, we reset the game.
    if (event.key == 'r'):
        ta = app.ta
        appStarted(app)
        app.mode = 'gameMode'
        app.ta = ta

# This function is needed to update timerFired and app.spriteCounter
def keyReleased(app, event):
    app.isMoving = False

def gameMode_timerFired(app):
    sprites(app)
    checkIfTAChosen(app)
    moveBacktrackerGhost2(app)
    moveBacktrackerGhost(app)
    checkIfTAOverNode(app)
    checkIfTAOverPowerUp(app)

def gameMode_redrawAll(app, canvas):
    drawColors(app, canvas)
    drawPKButtons(app, canvas)
    drawOHQStudent(app, canvas)
    drawMazeWalls(app, canvas)
    drawStartStopBoxes(app, canvas)
    drawSolution(app, canvas)
    drawGhostStudentSolution(app, canvas)
    drawGhostStudentSolution2(app, canvas)
    
    drawTextAtTop(app, canvas)
    drawPowerUp(app, canvas)
    drawPopUpGameOver(app, canvas)
    drawHealth(app, canvas)
    drawTA(app, canvas)
    

##########################################
# Main App
##########################################

# See citation 10 
def alterRowCol(app, row, col): # returns (x, y)
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols
    x = app.margin + row*cellWidth
    y = app.margin + col*cellHeight
    return (x, y)

# See citation 10 
def alterListOfPaths(app, listPaths):
    # takes in listPaths = app.listOfPaths
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / app.rows
    cellHeight = mazeHeight / app.cols

    for i in range(len(listPaths) - 1):
        currPath = listPaths[i]
        (x0, y0), (x1, y1) = currPath
        newX0 = app.margin + x0*cellWidth
        newY0 = app.margin + y0*cellHeight
        newX1 = app.margin + x1*cellWidth
        newY1 = app.margin + y1*cellHeight
        listPaths[i] = [(newX0 - 15, newY0 - 15), 
                        (newX1 + 15, newY1 + 15)]
    # now all of app.listOfPaths should be altered with actual coordintes 
    # instead of just nodes. 

def removeMaze(app):
    for elem in app.listOfPaths:
        app.listOfPaths.remove(elem)
    makeBoard(app)
    app.mode = 'gameMode'

def makeBoard(app):
    app.rows = 10     # note that this number isn't actually 
    app.cols = 10     # the # of rows, it's # of nodes.
    app.boardObject = Board(app.rows, app.cols)
    app.board = app.boardObject.getBoardOfCoords()
    app.listOfPaths = app.boardObject.getListOfPaths(app.board) 
    app.originalListOfPaths = copy.deepcopy(app.listOfPaths)

    app.listOfSolutionPaths = solution(app, app.listOfPaths, (0, 0), 
        (app.rows - 1, app.cols - 2))
    app.listOfSolutionCoords = []
    if app.listOfSolutionPaths != None:
        # alter the values...
        mazeWidth = app.width - 2*app.margin
        mazeHeight = app.height - 2*app.margin
        cellWidth = mazeWidth / app.rows
        cellHeight = mazeHeight / app.cols

        for i in range(len(app.listOfSolutionPaths)):
            currPath = app.listOfSolutionPaths[i]
            (x0, y0), (x1, y1) = currPath
            newX0 = app.margin + x0*cellWidth
            newY0 = app.margin + y0*cellHeight
            newX1 = app.margin + x1*cellWidth
            newY1 = app.margin + y1*cellHeight
            app.listOfSolutionCoords.append([(newX0, newY0), 
                                             (newX1, newY1)])
            app.listOfSolutionPaths[i] = [(newX0 - 10, newY0 - 10), 
                                        (newX1 + 10, newY1 + 10)]
    else:
        app.listOfSolutionPaths = solution(app, app.listOfPaths, (0, 0), 
        (app.rows - 1, app.cols - 2))
        
    alterListOfPaths(app, app.listOfPaths)   
    # app.listOfPaths is now altered
    app.listOfAllNodes = [] # [(0, 0), (0, 1), ...]
    for r in range(app.rows):
        for c in range(app.cols):
            (x, y) = alterRowCol(app, r, c)
            t = (x, y) 
            app.listOfAllNodes.append(t)
    # in timerFired, we check if the TA went over a node, and if it did, 
    # we add that node to app.listOfNodesTAVisited

    app.solutionNodesToGo = []
    for (t1, t2) in app.listOfSolutionCoords:
        app.solutionNodesToGo.append(t1)

def makeIconImages(app):
    # winston:
    winston = 'images/spriteSheet-trans1.png'
    winston = app.loadImage(winston)
    winston = app.scaleImage(winston, 0.5) 
    # stephanie
    stephanie = 'images/spriteSheet-trans2.png'
    stephanie = app.loadImage(stephanie)
    stephanie = app.scaleImage(stephanie, 0.5) 
    imageWidth, imageHeight = winston.size
    topLeftX = 0
    topLeftY = 0
    botRightX = imageWidth / 4
    botRightY = imageHeight / 4
    app.winstonIcon = winston.crop((topLeftX, topLeftY, botRightX, botRightY))
    app.stephanieIcon = stephanie.crop((topLeftX, topLeftY, botRightX, botRightY))

def makeBonusStudents(app):
    app.bonusStudent = 'images/Student.png'
    app.bonusStudent = app.loadImage(app.bonusStudent)
    app.bonusStudent = app.scaleImage(app.bonusStudent, 0.03) 

# Note regarding sprites: see Citations 1 and 4. 
def makeTA(app):
    app.playerX = app.margin 
    app.playerY = app.margin 
    app.spriteCounter = 0
    app.TA = TA(app.playerX, app.playerY, app.spriteCounter)
    app.spriteCounter = app.TA.spriteCounter
    app.sprites = app.TA.sprites
    app.direction = app.TA.direction
    app.isMoving = app.TA.isMoving
    app.ta = ""
    if app.ta == 'winston':
        app.taImage = 'images/spriteSheet-trans1.png'
        app.taImage = app.loadImage(app.taImage)
        app.taImage = app.scaleImage(app.taImage, 0.25) 
        app.TA.initImages(app.taImage)
    else:
        app.taImage = 'images/spriteSheet-trans2.png'
        app.taImage = app.loadImage(app.taImage)
        app.taImage = app.scaleImage(app.taImage, 0.25) 
        app.TA.initImages(app.taImage)
    app.taImage = 'images/spriteSheet-trans1.png'
    app.taImage = app.loadImage(app.taImage)
    app.taImage = app.scaleImage(app.taImage, 0.25) 
    app.TA.initImages(app.taImage)
    
# see citation 1 and 4 for sprite code
def makeOHQStudent(app):
    ohqStudent = OHQStudent()
    app.ohqStudentImage = 'images/idle-student-transparent.png'
    app.ohqStudentImage = app.loadImage(app.ohqStudentImage)
    app.ohqStudentImage = app.ohqStudentImage.transpose(Image.FLIP_LEFT_RIGHT)
    app.ohqStudentImage = app.scaleImage(app.ohqStudentImage, 0.4) 
    ohqStudent.makeOHQStudent(app.ohqStudentImage)
    app.ohqStudentSpriteCounter = ohqStudent.ohqStudentSpriteCounter
    app.ohqStudentSprites = ohqStudent.ohqStudentSprites
    app.ohqStudentX = ohqStudent.ohqStudentX
    app.ohqStudentY = ohqStudent.ohqStudentY

def makePowerUp(app):
    app.drawPowerUp = True
    # fixed location in center. 
    x, y = 0, 0
    for (x0, y0), (x1, y1) in app.originalListOfPaths:
        if 4 <= x0 <= 6 and 4 <= y0 <= 6:
            x = x0
            y = y0
            break
    if x == 0 and y == 0:
        # if none of those worked -- wider range. 
        for (x0, y0), (x1, y1) in app.originalListOfPaths:
            if 2 <= x0 <= 7 and 2 <= y0 <= 7:
                x = x0
                y = y0
                break
    # actual dimensions when drawing on canvas
    (app.powerUpX, app.powerUpY) = alterRowCol(app, x, y) 

def makeTextEditor(app):
    # let's change app.value into a list of tuples ("a", 790), char and x location. 
    app.value = []
    app.cursorX = app.width/10
    app.cursorY = app.height/2 + 50 # this never changes.
    app.textX = app.cursorX - 5
    app.textY = app.cursorY
    app.showCursor = True
    app.timeTextCursor = time.time()
    app.done = False

def makeListOfTiles(app):
    app.listOfTiles = [] # list of tuples (x0, y0, x1, y1)
    app.listOfStudents = [] # list of tuples (x, y)
    mazeWidth = app.width - 2*app.margin
    mazeHeight = app.height - 2*app.margin
    cellWidth = mazeWidth / 19
    cellHeight = mazeHeight / 19
    for i in range(19):
        for j in range(19):
            if app.map[i][j] == 0:
                topX = app.margin + i*cellWidth
                topY = app.margin + j*cellHeight
                botX = app.margin + (i+1)*cellWidth
                botY = app.margin + (j+1)*cellHeight
                midX = topX + (botX - topX)/2
                midY = topY + (botY - topY)/2
                t = (topX, topY, botX, botY)
                p = (midX, midY)
                app.listOfTiles.append(t)
                app.listOfStudents.append(p)

def appStarted(app):
    app.mode = 'homeScreenMode'
    app.margin = 125
    app.accessToArrowKeysOff = False
    app.t0 = time.time()
    app.drawSolutionBool = False
    app.map = createMap(19, 60, 12)
    app.init = time.time()
    app.seconds = 20
    app.timeUp = False

    # Scoring / Leaderboard 
    app.showPopUp = False
    app.health = 20
    app.original = app.health
    app.drawHealthMessage = False
    app.drawPowerUpMessage = False
    app.printName = False
    app.name = ""
    app.addToLeaderboard = True
    app.reachedPowerUp = False
    app.bonusPressed = False

    makeBoard(app)
    makeTA(app)
    makeOHQStudent(app)
    makeBackTrackerGhostStudent(app, 0, 0)
    makeBackTrackerGhostStudent2(app)
    makePowerUp(app)
    makeIconImages(app)
    makeTextEditor(app)
    makeListOfTiles(app)
    makeBonusStudents(app)

runApp(width=800, height=800)