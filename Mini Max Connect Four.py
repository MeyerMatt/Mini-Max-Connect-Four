def valid_move(gameboard,columns):
    for i in range(5,0,-1):
        if gameboard[i][columns] == 0:
            return i
        if i != 0:
            return -1

def placement(gameboard, columns, playerturn, turnsplayed):
    playermove = int(input("Choose a column 0 through 7:"))
    Nigga = valid_move(gameboard,playermove)
    if Nigga != -1:
        gameboard[Nigga][playermove] = 1
        playerturn = 2 
        turnsplayed = turnsplayed + 1
        print(gameboard)
    if valid_move == -1:
        print("Pick New Column:")
    return placement(gameboard,columns,playerturn,turnsplayed)


rows , columns = (6,7)
gameboard = [[0]* columns]* rows
for row in gameboard:
    print (row)
playerturn = 1
gamestate = 0
turnsplayed = 0


row_index = 6
column_index = 7
turn = 0
while(gamestate == 0):
    print(gameboard)
    if turn == 0:
        puck_1 = placement(gameboard,columns,playerturn,turnsplayed)
    else:
        puck_2 = placement(gameboard,columns,playerturn,turnsplayed)
    turn += 1
    turn = turn % 2


#NEW SHIT
def valid_move(gameboard,columns):
    for i in range(5,0,-1):
        if gameboard[i][columns] == 0:
            return i
        if i != 0:
            return -1

def placement(gameboard, columns, playerturn, turnsplayed):
    playermove = int(input("Choose a column 0 through 7: "))
    Nigga = valid_move(gameboard,playermove)
    if Nigga != -1:
        if playerturn == 1:
            gameboard[Nigga][playermove] = 1
            playerturn = 2 
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
        elif playerturn == 2:
            gameboard[Nigga][playermove] = 2
            playerturn = 1
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
    if Nigga == -1:
        print("Pick New Column: ")
        return placement(gameboard,columns,playerturn,turnsplayed)

def PrintBoard(gb, row):
    for row in gb:
        print(row)

rows , columns = (6,7)
gameboard = [[0]* columns]* rows
for row in gameboard:
    print (row)

    
playerturn = 1
gamestate = 0
turnsplayed = 0


row_index = 6
column_index = 7

while(gamestate == 0):
##    print(gameboard)
    if playerturn == 1:
        puck_1 = placement(gameboard,columns,playerturn,turnsplayed)
        playerturn = 2
    else:
        puck_2 = placement(gameboard,columns,playerturn,turnsplayed)
        playerturn = 1


