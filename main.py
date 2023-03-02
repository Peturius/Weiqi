from tkinter import *
from time import *
import sys
root = Tk()
s = Canvas(root, width=800, height=800, background="#b69b4c")
s.pack()

Board_Size = 19
Frame_Gap = 35
width = 800
height = 800
groups = []
liberties = {}

for i in range(Board_Size):
    groups.append(["0"] * (Board_Size))
print(groups)



def UpdateGroups(moveY, moveX):

    capturedgroup = ""
    move = board[moveY-1][moveX-1]
    groups[moveY-1][moveX-1] = chr(moveY+96) + chr(moveX+96)
    liberties[groups[moveY-1][moveX-1]] = 4
    libertyCount = liberties[groups[moveY-1][moveX-1]]
    moveGroup = groups[moveY-1][moveX-1]
    print("move", move)
    print("movegroup", moveGroup)

    if moveY == 1:
        libertyCount -= 1
    if moveY > 1:
        target = board[moveY-2][moveX-1]
        targetGroup = groups[moveY-2][moveX-1]
        print("up target", target)
        print("up targetGroup", targetGroup)
        if target == 0:
            pass
        elif target != move:
            libertyCount -= 1
            liberties[targetGroup] -= 1
            if liberties[targetGroup] == 0:
                for i in range(Board_Size + 1):
                    for j in range(Board_Size + 1):
                        if groups[j][i] == targetGroup:
                            capturedgroup = targetGroup
                            board[j][i] = 0
                            Capture(capturedgroup)

                liberties.pop(targetGroup)

        elif target == move:
            for i in range(Board_Size + 1):
                for j in range(Board_Size + 1):
                    if groups[j][i] == targetGroup:
                        groups[j][i] = moveGroup
            targetLiberties = liberties.get(targetGroup)
            liberties.pop(targetGroup)
            libertyCount += targetLiberties
            libertyCount -= 2
            liberties[moveGroup] = libertyCount

    if moveY == 19:
        libertyCount -= 1
    if moveY < 19:
        target = board[moveY][moveX-1]
        targetGroup = groups[moveY][moveX-1]
        print("down target", target)
        print("down targetGroup", targetGroup)
        if target == 0:
            pass
        elif target != move:
            libertyCount -= 1
            liberties[targetGroup] -= 1
            if liberties[targetGroup] == 0:
                for i in range(Board_Size + 1):
                    for j in range(Board_Size + 1):
                        if groups[j][i] == targetGroup:
                            capturedgroup = targetGroup
                            board[j][i] = 0
                            Capture(capturedgroup)


                liberties.pop(targetGroup)

        elif target == move:
            for i in range(Board_Size + 1):
                for j in range(Board_Size + 1):
                    if groups[j][i] == targetGroup:
                        groups[j][i] = moveGroup
            targetLiberties = liberties.get(targetGroup)
            liberties.pop(targetGroup)
            libertyCount += targetLiberties
            libertyCount -= 2
            liberties[moveGroup] = libertyCount

    if moveX == 1:
        libertyCount -= 1
    if moveX > 1:
        target = board[moveY-1][moveX-2]
        targetGroup = groups[moveY-1][moveX-2]
        print("left target", target)
        print("left targetGroup", targetGroup)
        if target == 0:
            pass
        elif target != move:
            libertyCount -= 1
            liberties[targetGroup] -= 1
            if liberties[targetGroup] == 0:
                for i in range(Board_Size + 1):
                    for j in range(Board_Size + 1):
                        if groups[j][i] == targetGroup:
                            capturedgroup = targetGroup
                            board[j][i] = 0
                            Capture(capturedgroup)

                liberties.pop(targetGroup)

        elif target == move:
            for i in range(Board_Size + 1):
                for j in range(Board_Size + 1):
                    if groups[j][i] == targetGroup:
                        groups[j][i] = moveGroup
            targetLiberties = liberties.get(targetGroup)
            liberties.pop(targetGroup)
            libertyCount += targetLiberties
            libertyCount -= 2
            liberties[moveGroup] = libertyCount

    if moveX == 19:
        libertyCount -= 1

    if moveX < 19:
        target = board[moveY-1][moveX]
        targetGroup = groups[moveY-1][moveX]
        print("right target", target)
        print("right targetGroup", targetGroup)
        if target == 0:
            pass
        elif target != move:
            libertyCount -= 1
            liberties[targetGroup] -= 1
            if liberties[targetGroup] == 0:
                for i in range(Board_Size + 1):
                    for j in range(Board_Size + 1):
                        if groups[j][i] == targetGroup:
                            capturedgroup = targetGroup
                            board[j][i] = 0
                            Capture(capturedgroup)
                liberties.pop(targetGroup)


        elif target == move:
            for i in range(Board_Size + 1):
                for j in range(Board_Size + 1):
                    if groups[j][i] == targetGroup:
                        groups[j][i] = moveGroup
            targetLiberties = liberties.get(targetGroup)
            liberties.pop(targetGroup)
            libertyCount += targetLiberties
            libertyCount -= 2
            liberties[moveGroup] = libertyCount

    if moveX > 1 and board[moveY-1][moveX-2] == 0:
        if moveX > 2:
            target1 = groups[moveY-1][moveX-3]
            if target1 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveY > 1:
            target2 = groups[moveY-2][moveX-2]
            if target2 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveY < 19:
            target3 = groups[moveY][moveX-2]
            if target3 == groups[moveY-1][moveX-1]:
                libertyCount -= 1

    if moveY > 1 and board[moveY - 2][moveX - 1] == 0:
        if moveY > 2:
            target1 = groups[moveY-3][moveX-1]
            if target1 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveX > 1:
            target2 = groups[moveY-2][moveX-2]
            if target2 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveX < 19:
            target3 = groups[moveY-2][moveX]
            if target3 == groups[moveY-1][moveX-1]:
                libertyCount -= 1

    if moveX < 19 and board[moveY - 1][moveX] == 0:
        if moveY > 1:
            target1 = groups[moveY - 2][moveX]
            if target1 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveY < 19:
            target2 = groups[moveY][moveX]
            if target2 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveX < 18:
            target3 = groups[moveY-1][moveX+1]
            if target3 == groups[moveY-1][moveX-1]:
                libertyCount -= 1

    if moveY < 19 and board[moveY][moveX-1] == 0:
        if moveY < 18:
            target1 = groups[moveY+1][moveX-1]
            if target1 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveX > 1:
            target2 = groups[moveY][moveX-2]
            if target2 == groups[moveY-1][moveX-1]:
                libertyCount -= 1
        if moveX < 19:
            target3 = groups[moveY][moveX]
            if target3 == groups[moveY-1][moveX-1]:
                libertyCount -= 1

    for i in groups:
        for j in i:
            print(j, end=" ")
        print()

    liberties[groups[moveY - 1][moveX - 1]] = libertyCount
    #UpdateLiberties()


    #print(liberties[groups[moveY-1][moveX-1]])
    #print(liberties)

def Capture (capturedGroup):
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            if groups[y][x] == capturedGroup:
                groups[y][x] = "0"

def UpdateLiberties():


    for group in liberties:
        liberties[group] = 0


    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            moveGroupsSet = set()
            if y > 0 and board[y][x] == 0:
                if groups[y-1][x] != "0":
                    moveGroupsSet.add(groups[y-1][x])
            if y < 18 and board[y][X] == 0:
                if groups[y+1][x] != "0":
                    moveGroupsSet.add(groups[y+1][x])
            if x > 0 and board[y][x] == 0:
                if groups[y][x-1] != "0":
                    moveGroupsSet.add(groups[y][x-1])
            if x < 18 and board[y][x] == 0:
                if groups[y][x+1] != "0":
                    moveGroupsSet.add(groups[y][x+1])
            for group in moveGroupsSet:
                liberties[group] += 1

            if len(moveGroupsSet) > 0:
                print("liberties", moveGroupsSet, y+1, x+1)
    print(liberties)
def create_star(X, Y):
    s.create_oval((Board_X1 + Board_GapX * (X - 1)) - Chess_Radius / 5,
                  (Board_Y1 + Board_GapY * (Y - 1)) - Chess_Radius / 5,
                  (Board_X1 + Board_GapX * (X - 1)) + Chess_Radius / 5,
                  (Board_Y1 + Board_GapY * (Y - 1)) + Chess_Radius / 5, fill="black")


def create_stone(x, y, radius, fill="", outline="black", width=1):
    s.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill, outline=outline, width=width, tags="cica")

def Value_Check_int(Value):
    try:
        Value = int(Value)
    except ValueError:
        return "string"
    else:
        return "int"

def MouseClick(event):
    global clickCoord
    coordX = event.x
    coordY = event.y
    clickCoord = Location(coordX, coordY)
    #print(clickCoord)
s.bind("<Button-1>", MouseClick)
clickCoord = [None, None]

def Location(coordX, coordY):
    X = None
    Y = None
    for i in range(len(ActualCoordX1)):

        if coordX > ActualCoordX1[i] and coordX < ActualCoordX2[i]:
            X = GameCoordX[i]

        if coordY > ActualCoordY1[i] and coordY < ActualCoordY2[i]:
            Y = GameCoordY[i]

    return X, Y

def Location_Validation():
    if X == None or Y == None:
        return False

    elif board[Y - 1][X - 1] == 0:
        return True

# Board
Board_Size = Board_Size - 1
Board_X1 = width / 10
Board_Y1 = height / 10
Board_GapX = (width - Board_X1 * 2) / Board_Size
Board_GapY = (height - Board_Y1 * 2) / Board_Size

# Chess Piece
Chess_Radius = (Board_GapX * (9 / 10)) / 2

# Turn
Turn_Num = 1
Turn = "black"
Winner = None

# Cord List
Black_Cord_PickedX = []
Black_Cord_PickedY = []
White_Cord_PickedX = []
White_Cord_PickedY = []
GameCoordX = []
GameCoordY = []
ActualCoordX1 = []
ActualCoordY1 = []
ActualCoordX2 = []
ActualCoordY2 = []
board = []

B = Button(root, text="Resign", font="Helvetica 10 bold", bg="white", fg="black")
B.pack()
B.place(x=width / 2 * 0.5, y=height - Frame_Gap * 1.6 + 15, height=Chess_Radius * 2, width=Chess_Radius * 4)

# 2D list for gameboard
for i in range(Board_Size + 1):
    board.append([0] * (Board_Size + 1))

Unfilled = 0
Black_Piece = 1
White_Piece = 2

# Fills Empty List
for z in range(1, Board_Size + 2):

    for i in range(1, Board_Size + 2):
        GameCoordX.append(z)
        GameCoordY.append(i)
        ActualCoordX1.append((z - 1) * Board_GapX + Board_X1 - Chess_Radius)
        ActualCoordY1.append((i - 1) * Board_GapY + Board_Y1 - Chess_Radius)
        ActualCoordX2.append((z - 1) * Board_GapX + Board_X1 + Chess_Radius)
        ActualCoordY2.append((i - 1) * Board_GapY + Board_Y1 + Chess_Radius)

# Create Board
s.create_rectangle(Board_X1 - Frame_Gap, Board_Y1 - Frame_Gap, Board_X1 + Frame_Gap + Board_GapX * Board_Size,
                   Board_Y1 + Frame_Gap + Board_GapY * Board_Size, width=3)

for f in range(Board_Size + 1):
    s.create_line(Board_X1, Board_Y1 + f * Board_GapY, Board_X1 + Board_GapX * Board_Size, Board_Y1 + f * Board_GapY)
    s.create_line(Board_X1 + f * Board_GapX, Board_Y1, Board_X1 + f * Board_GapX, Board_Y1 + Board_GapY * Board_Size)

    s.create_text(Board_X1 - Frame_Gap * 1.7, Board_Y1 + f * Board_GapY, text=f + 1, font="Helvetica 10 bold",
                  fill="black")
    s.create_text(Board_X1 + f * Board_GapX, Board_Y1 - Frame_Gap * 1.7, text=f + 1, font="Helvetica 10 bold",
                  fill="black")

#s.create_oval((Board_X1 + Board_GapX * (4 - 1)) - Chess_Radius / 5, (Board_Y1 + Board_GapY * (4 - 1)) - Chess_Radius / 5, (Board_X1 + Board_GapX * (4 - 1)) + Chess_Radius / 5, (Board_Y1 + Board_GapY * (4 - 1)) + Chess_Radius / 5, fill="black")
create_star(4, 4)
create_star(4, 10)
create_star(4, 16)
create_star(10, 4)
create_star(10, 10)
create_star(10, 16)
create_star(16, 4)
create_star(16, 10)
create_star(16, 16)


while Winner == None:

    s.update()

    X = clickCoord[0]
    Y = clickCoord[1]

    Picked = Location_Validation()

    if Picked:

        if Turn_Num % 2 == 1:
            White_Cord_PickedX.append(X)
            White_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 2
            print()
            print(Turn, "picked", Y, X)
            UpdateGroups(Y, X)

            UpdateLiberties()
            Turn = "white"

        elif Turn_Num % 2 == 0:
            Black_Cord_PickedX.append(X)
            Black_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 1
            print()
            print(Turn, "picked", Y, X)
            UpdateGroups(Y, X)
            UpdateLiberties()

            Turn = "black"

        #s.delete(Turn_Text)
        s.delete("cica")
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    create_stone(Board_X1 + Board_GapX * (j), Board_Y1 + Board_GapY * (i), radius=Chess_Radius,
                                 fill="white")
                if board[i][j] == 2:
                    create_stone(Board_X1 + Board_GapX * (j), Board_Y1 + Board_GapY * (i), radius=Chess_Radius,
                                 fill="black")
        #create_stone(Board_X1 + Board_GapX * (X - 1), Board_Y1 + Board_GapY * (Y - 1), radius=Chess_Radius, fill=Turn)

        Turn_Num = Turn_Num + 1

        if Turn == "white":
            Colour_Check = Black_Piece


        elif Turn == "black":
            Colour_Check = White_Piece


        #Winner = winCheck(Colour_Check, Win_Check, board)

#s.delete(Turn_Text)