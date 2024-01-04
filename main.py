from tkinter import *
from time import *
import sys
root = Tk()
s = Canvas(root, width=800, height=800, background="#f2b06d")
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

def connect(oopsie):
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            if groups[y][x] == oopsie[0]:
                groups[y][x] = oopsie[1]

def UpdateGroups():
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            if board[y][x] != 0:
                groups[y][x] = chr(y + 97) + chr(x + 97)


    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            oopsie = []
            if y < 18:
                if board[y][x] == board[y + 1][x]:
                    groups[y][x] = groups[y + 1][x]
                    #print("jobb")
            if x < 18:
                if board[y][x] == board[y][x + 1]:
                    groups[y][x] = groups[y][x + 1]
                    #print("le")
            if y > 0:
                if board[y][x] == board[y - 1][x]:
                    groups[y][x] = groups[y - 1][x]
                    oopsie.append(groups[y - 1][x])
            if x > 0:
                if board[y][x] == board[y][x - 1]:
                    groups[y][x] = groups[y][x - 1]
                    oopsie.append(groups[y][x - 1])
            if len(oopsie) == 2:
                connect(oopsie)


    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            if groups[y][x] == "0":
                print(groups[y][x], end="  ")
            else:
                print(groups[y][x], end=" ")
        print()
    print("-------------------------------------------------------")
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            print(board[y][x], end="  ")
        print()



def Capture (capturedGroup):
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            if groups[y][x] == capturedGroup:
                groups[y][x] = "0"
                board[y][x] = 0

def UpdateLiberties(groups):
    liberties.clear()
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            neighbours = set()
            if y < 18:
                if groups[y][x] == "0" and groups[y + 1][x] != "0":
                    neighbours.add(groups[y + 1][x])
                    #print("felső")
            if x < 18:
                if groups[y][x] == "0" and groups[y][x + 1] != "0":
                    neighbours.add(groups[y][x + 1])
                    #print("bal")
            if y > 0:
                if groups[y][x] == "0" and groups[y - 1][x] != "0":
                    neighbours.add(groups[y - 1][x])
                    #print("alsó")
            if x > 0:
                if groups[y][x] == "0" and groups[y][x - 1] != "0":
                    neighbours.add(groups[y][x - 1])
                    #print("jobb")
            for group in neighbours:
                AddLiberty(group)
    print(liberties)

def AddLiberty(group):
    try:
        liberties[group] += 1
    except:
        liberties[group] = 1

def TakeStones(turn):
    if turn == "black":
        turnturn = 2
    if turn == "white":
        turnturn = 1
    for y in range(Board_Size + 1):
        for x in range(Board_Size + 1):
            isDead = True
            for group in liberties:
                if groups[y][x] == group:
                    isDead = False
            if isDead and board[y][x] == abs(turnturn - 3):
                board[y][x] = 0
                groups[y][x] = "0"
    s.update()

def CheckSuicide():
    if Turn == "black":
        turnturn = 2
    if Turn == "white":
        turnturn = 1

    if Y > 1:
        #bal
        if board[Y - 2][X - 1] == 0:
            return False
        if board[Y - 2][X - 1] == turnturn:
            if liberties[groups[Y - 2][X - 1]] > 1:
                print("cica", liberties[groups[Y - 2][X - 1]], groups[Y - 2][X - 1])
                return False
        if board[Y - 2][X - 1] == abs(turnturn - 3):
            if liberties[groups[Y - 2][X - 1]] ==  1:
                return False

    if X > 1:
        #fel
        if board[Y - 1][X - 2] == 0:
            return False
        if board[Y - 1][X - 2] == turnturn:
            if liberties[groups[Y - 1][X - 2]] > 1:
                print("mica", liberties[groups[Y - 1][X - 2]], groups[Y - 1][X - 2])
                return False
        if board[Y - 1][X - 2] == abs(turnturn - 3):
            if liberties[groups[Y - 1][X - 2]] ==  1:
                return False
    if Y < 19:
        #bal
        if board[Y][X - 1] == 0:
            return False
        if board[Y][X - 1] == turnturn:
            if liberties[groups[Y][X - 1]] > 1:
                print("cucu", liberties[groups[Y][X - 1]], groups[Y][X - 1])
                return False
        if board[Y][X - 1] == abs(turnturn - 3):
            if liberties[groups[Y][X - 1]] ==  1:
                return False
    if X < 19:
        #bal
        if board[Y - 1][X] == 0:
            return False
        if board[Y - 1][X] == turnturn:
            if liberties[groups[Y - 1][X]] > 1:
                print("mucu", liberties[groups[Y - 1][X]], groups[Y - 1][X])
                return False
        if board[Y - 1][X] == abs(turnturn - 3):
            if liberties[groups[Y - 1][X]] ==  1:
                return False
    return True

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
        isSuicide = CheckSuicide()
        if isSuicide == False:

            if Turn_Num % 2 == 1:
                White_Cord_PickedX.append(X)
                White_Cord_PickedY.append(Y)
                board[Y - 1][X - 1] = 2
                print()
                print(Turn, "picked", Y, X)
                UpdateGroups()
                UpdateLiberties(groups)
                TakeStones(Turn)

                Turn = "white"

            elif Turn_Num % 2 == 0:
                Black_Cord_PickedX.append(X)
                Black_Cord_PickedY.append(Y)
                board[Y - 1][X - 1] = 1
                print()
                print(Turn, "picked", Y, X)
                UpdateGroups()
                UpdateLiberties(groups)
                TakeStones(Turn)

                Turn = "black"

            s.delete("cica")
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == 1:
                        create_stone(Board_X1 + Board_GapX * (j), Board_Y1 + Board_GapY * (i), radius=Chess_Radius,
                                     fill="white")
                    if board[i][j] == 2:
                        create_stone(Board_X1 + Board_GapX * (j), Board_Y1 + Board_GapY * (i), radius=Chess_Radius,
                                     fill="black")
            Turn_Num = Turn_Num + 1

            if Turn == "white":
                Colour_Check = Black_Piece


            elif Turn == "black":
                Colour_Check = White_Piece

