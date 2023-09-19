def valid_move(gameboard,columns):
    for i in range(5,0,-1):
        if gameboard[i][columns] == 0:
            return i
        if i != 0:
            return -1

def placement(gameboard, columns, playerturn, turnsplayed):
    """
    placement()

    places piece on gameboard
    
    """
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


#updatetd at night 
def placement(gameboard, columns, playerturn, turnsplayed):
    playermove = int(input("Choose a column 0 through 7: "))
    Nigga = valid_move(gameboard,playermove)
    if Nigga != -1:
        if playerturn == 1:
            print(f'Nigga={type(Nigga)}, playermove={type(playermove)}')
            gameboard[Nigga][playermove] = 1
            print(gameboard[Nigga][playermove])
            playerturn = 2 
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
        elif playerturn == 2:
            gameboard[Nigga][playermove] = 2
            playerturn = 1
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
    if Nigga == -1:
        print("Invalid Move Pick A New Column: ")
        return placement(gameboard,columns,playerturn,turnsplayed)

def valid_move(gameboard,columns):
    i=5
    print(i)
    for i in range(5,-1,-1):
##        if gameboard[i][columns] != 0:
##            return -1
        if gameboard[i][columns] == 0:
            print(i)
            return i
    for i in range(5, -1, -1):
        if gameboard[i] != 0:
            return -1

def PrintBoard(gb, row):
    for row in gb:
        print(row)

rows , columns = (6,7)
gameboard = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
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
        player_1 = placement(gameboard,columns,playerturn,turnsplayed)
        playerturn = 2
    else:
        player_2 = placement(gameboard,columns,playerturn,turnsplayed)
        playerturn = 1

#This is with the win check
def placement(gameboard, columns, playerturn, turnsplayed):
    playermove = int(input("Choose a column 0 through 7: "))
    Nigga = valid_move(gameboard,playermove)
    if Nigga != -1:
        if playerturn == 1:
            print(f'Nigga={type(Nigga)}, playermove={type(playermove)}')
            gameboard[Nigga][playermove] = 1
            print(gameboard[Nigga][playermove])
            playerturn = 2 
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
        elif playerturn == 2:
            gameboard[Nigga][playermove] = 2
            playerturn = 1
            turnsplayed = turnsplayed+1
            PrintBoard(gameboard, Nigga)
    if Nigga == -1:
        print("Invalid Move Pick A New Column: ")
        return placement(gameboard,columns,playerturn,turnsplayed)
    

def valid_move(gameboard,columns):
    i=5
    print(i)
    for i in range(5,-1,-1):
        if gameboard[i][columns] == 0:
            print(i)
            return i
    for i in range(5, -1, -1):
        if gameboard[i] != 0:
            return -1

def PrintBoard(gb, row):
    for row in gb:
        print(row)
 
def Check_Win(board, puck): #puck is just the number that each player uses
    # Check horizontal locations for win
    for c in range(columns-3):
        for r in range(6):
            if board[r][c] == puck and board[r][c+1] == puck and board[r][c+2] == puck and board[r][c+3] == puck:
                return True
 
    # Check vertical locations for win
    for c in range(7):
        for r in range(rows-3):
            if board[r][c] == puck and board[r+1][c] == puck and board[r+2][c] == puck and board[r+3][c] == puck:
                return True
 
    # Check positively sloped diaganols
    for c in range(columns-3):
        for r in range(rows-3):
            if board[r][c] == puck and board[r+1][c+1] == puck and board[r+2][c+2] == puck and board[r+3][c+3] == puck:
                return True
 
    # Check negatively sloped diaganols
    for c in range(columns-3):
        for r in range(3, rows):
            if board[r][c] == puck and board[r-1][c+1] == puck and board[r-2][c+2] == puck and board[r-3][c+3] == puck:
                return True



rows , columns = (6,7)
gameboard = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

for row in gameboard:
    print (row)

    
playerturn = 1
gamestate = 0
turnsplayed = 0


row_index = 6
column_index = 7

while(gamestate == 0):
    
    if playerturn == 1:
        player_1_move = placement(gameboard,columns,playerturn,turnsplayed) #they are the #1 (puck)
        playerturn = 2
        
    if Check_Win(gameboard, 1):
        print("player 1 Wins!!!")
        gamestate = 1
        
    else:
        
        player_2_move = placement(gameboard,columns,playerturn,turnsplayed) #they are the #2 (puck)
        playerturn = 1
        if Check_Win(gameboard, 2):
            print("player 2 Wins!!!")
            gamestate = 2


#this should work its what I had
def placement(gameboard, columns, playerturn, turnsplayed):
    good_list = [0,1,2,3,4,5,6]
    playermove = int(input("Choose a column 0 through 7: ")) #added a good_list...if you dont want it then take out the good list the first if and then the else statment at the bottom!
    if playermove in good_list:
        Nigga = valid_move(gameboard,playermove)
        if Nigga != -1:
            if playerturn == 1:
                print(f'Nigga={type(Nigga)}, playermove={type(playermove)}')
                gameboard[Nigga][playermove] = 1
                print(gameboard[Nigga][playermove])
                playerturn = 2 
                turnsplayed = turnsplayed+1
                PrintBoard(gameboard, Nigga)
            elif playerturn == 2:
                gameboard[Nigga][playermove] = 2
                playerturn = 1
                turnsplayed = turnsplayed+1
                PrintBoard(gameboard, Nigga)
        if Nigga == -1:
            print("Invalid Move Pick A New Column: ")
            return placement(gameboard,columns,playerturn,turnsplayed)
    else:
        print("That is not a column in the game bud")
        placement(gameboard,columns,playerturn,turnsplayed)
        

def valid_move(gameboard,columns):
    i=5
    print(i)
    for i in range(5,-1,-1):
        if gameboard[i][columns] == 0:
            print(i)
            return i
    for i in range(5, -1, -1):
        if gameboard[i] != 0:
            return -1

def PrintBoard(gb, row):
    for row in gb:
        print(row)
 
def Check_Win(board, puck): #puck is just the number that each player uses
    # Check horizontal locations for win
    for c in range(columns-3):
        for r in range(6):
            if board[r][c] == puck and board[r][c+1] == puck and board[r][c+2] == puck and board[r][c+3] == puck:
                return True
 
    # Check vertical locations for win
    for c in range(7):
        for r in range(rows-3):
            if board[r][c] == puck and board[r+1][c] == puck and board[r+2][c] == puck and board[r+3][c] == puck:
                return True
 
    # Check positively sloped diaganols
    for c in range(columns-3):
        for r in range(rows-3):
            if board[r][c] == puck and board[r+1][c+1] == puck and board[r+2][c+2] == puck and board[r+3][c+3] == puck:
                return True
 
    # Check negatively sloped diaganols
    for c in range(columns-3):
        for r in range(3, rows):
            if board[r][c] == puck and board[r-1][c+1] == puck and board[r-2][c+2] == puck and board[r-3][c+3] == puck:
                return True

def Mini_Max():
    
    return 0


rows , columns = (6,7)
gameboard = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

for row in gameboard:
    print (row)

    
playerturn = 1
gamestate = 0
turnsplayed = 0


row_index = 6
column_index = 7

while(gamestate == 0):
    
    if playerturn == 1:
        player_1_move = placement(gameboard,columns,playerturn,turnsplayed) #they are the #1 (puck)
        playerturn = 2
        
    if Check_Win(gameboard, 1):
        print("\nPlayer 1 Wins!!!\n")
        gamestate = 1
        
    else:
        
        player_2_move = placement(gameboard,columns,playerturn,turnsplayed) #they are the #2 (puck)
        playerturn = 1
        if Check_Win(gameboard, 2):
            print("\nPlayer 2 Wins!!!\n")
            gamestate = 2
