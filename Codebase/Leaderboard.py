#############################################################################
# This file creates the leaderboard list.
# Citation 8: Accessing .txt files
    # https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
    # https://www.pythontutorial.net/python-basics/python-read-text-file/ 
    # I wrote my code up myself using help from this article, read about 
    # open, readlines(), write, and close. 
#############################################################################

def addToLeaderboard(name, score):
    file_object = open('leaderboard.txt', 'a')
    file_object.write(f'{name}, {score}')
    file_object.write("\n")
    file_object.close()

def makeList():
    with open('leaderboard.txt') as f:
        contents = f.readlines()
        lst = []
        for line in contents:
            miniList = []
            for elem in line.split(" "):
                miniList.append(elem[:-1])
            miniList[-1] = int(miniList[-1])
            if miniList[0] == "":
                miniList[0] = "Anonymous Player"
            lst.append(miniList)
        return lst

def sortList():
    l = makeList()
    # list of all numbers
    numList = []
    for elem in l:
        numList.append(elem[-1])
    
    # sort numList. 
    numList.sort()
    numList = numList[::-1]
    # list of numbers sorted from highest to lowest. 
    newList = []
    for num in numList: # num = 20
        name = ""
        newMiniList = [num]
        # find the corresponding name. 
        index = 0
        while index < len(l):
            if l[index][-1] == num:
                # save elem[0]
                name = l[index][0]
                l.pop(index)
                break
            index += 1
        newMiniList.insert(0, name)
        newList.append(newMiniList)
    
    return newList

def getTop10():
    L = sortList()
    return L[:10]
