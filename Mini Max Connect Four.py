rows , columns = (6,7)
gameboard = [[0]* columns]* rows
for row in gameboard:
    print (row)
playerturn =1
gamestate = 0
turnsplayed = 0
thislist = gameboard



        





row_index = 5 
while(gamestate == 0):
    print(gameboard)
    if turnsplayed % 2 == 1:
        playermove = int(input("Choose a space 0 through 7"))
    while True: 
        if gameboard[row_index][playermove] != 0: 
            row_index -= 1
        else: 
            gameboard[row_index][playermove] = -1 or 1 
            break
