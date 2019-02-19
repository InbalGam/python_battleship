# ' ' nothing in square
# 'o' ship in square
# 'x' ship in square and it was bombed
# '-' no ship in square and the square was bombed
import time
import json
import sys

# in the list the 1st element is the amount of squares for the ship and 
#the second element is how many ships are like that


#function to load or new game:
def load_not():
    u_inp = input('Hello, would you like to start a new game or load previous game?\n'
                  'please enter n/l:')
    if u_inp == 'l':
        with open('battleship_game.json') as b_game:  
            data = json.load(b_game)
        u_game = data.get("type game")
        u1_name = data.get("pl1 name")
        u2_name = data.get("pl2 name")
        pl_1 = data.get("pl1 board")
        pl_2 = data.get("pl2 board")
        play_win(pl_1, pl_2, u_game, u1_name, u2_name)
        sys.exit('End Game')
    else:
        return
    
def new_board():
    lst_ex = [[' ']*10 for i in range(10)]
    return lst_ex

#printing game board:
def print_board(board):
    print('| |0|1|2|3|4|5|6|7|8|9|')
    abc = 'ABCDEFGHIJ'
    for i in range(len(abc)):
        print('|' + abc[i] +'|' + '|'.join(board[i]) +'|')

## printing boards without 'o'
def print_board_wo(board):
    print('| |0|1|2|3|4|5|6|7|8|9|')
    abc = 'ABCDEFGHIJ'
    for i in range(len(abc)):
        print('|' + abc[i] +'|' + '|'.join(board[i]).replace('o', ' ') +'|')

#function to enter ships:      
def enter_ship(board, u_game, u_name):
    if u_game == 1:
        ship_lst = ship_sqaure.get("option 1")     
    else:
        ship_lst = ship_sqaure.get("option 2")##needs some changes because [1,4] 
    for i in range(4):
        if ship_lst[i][1] != 1:
            for k in range(ship_lst[i][1]):
                check_board(board, i, ship_lst,u_name)
        else:
            check_board(board, i, ship_lst,u_name)
    print_board(board)      
         
#function to check boards:
def check_board(board, i, ship_lst,u_name):
    let = "ABCDEFGHIJ"
    print_board(board)
    u_ind = input(u_name + ', enter range of battleship of size ' + str(ship_lst[i][0]) +":")
    u_range = u_ind.split()
    sq_range = abs((int(u_range[1][1])+1) - int(u_range[0][1]))
    sq_let_range = abs((let.find(u_range[1][0])+1) - let.find(u_range[0][0]))
    if sq_range == ship_lst[i][0] and sq_let_range-1 == 0 :
        for j in range(int(u_range[0][1]), int(u_range[1][1])+1):
            if board[let.find(u_range[0][0])][j] != ' ':
                print("Cells already taken!")
                check_board(board, i, ship_lst,u_name)
                return board
        for j in range(int(u_range[0][1]), int(u_range[1][1])+1):
            board[let.find(u_range[0][0])][j] = 'o'        
    elif sq_let_range == ship_lst[i][0] and sq_range-1 == 0:
        for j in range(let.find(u_range[0][0]), let.find(u_range[1][0])+1):
            if board[j][int(u_range[0][1])] != ' ':
                print("Cells already taken!")
                check_board(board, i, ship_lst,u_name)
                return board
        for j in range(let.find(u_range[0][0]), let.find(u_range[1][0])+1):
            board[j][int(u_range[0][1])] = 'o' 
    else:
        print("Incorrect size!")
        check_board(board, i, ship_lst,u_name)
        return board
    return board

## function to enter ships for each player, calling enter_ship:
def creating_pl_boards(board, u_game, u_name):
    time.sleep(3)
    print('\n' *100)
    enter_ship(board, u_game, u_name) 
    
#we are starting to play!
#checking who is the winner:
def winner(op_b, player):
    pl = player
    for i in range(len(op_b)):
        for j in range(len(op_b)):
            if op_b[i][j]=='o':
                pl = 'no'
    if pl == 'no':
        return pl
    else:
        return pl

        
#function to start guess where the other player's ships:
def guess_ship(board_p, board_op, u_game, pl_name, player):
#board_p = the real board of the player that's now hitting
#board_op = the real board of the one that gets hit
#pl_name = the one that now hit
    time.sleep(3)
    print('\n' *100)
    let = "ABCDEFGHIJ"
    pl_inp = input('Other player, please do not look! ' + pl_name + ' enter something\n' +
                   'in order to see your board:')
    print_board(board_p)
    pl_inp2 = input(pl_name + ' enter something to see the opponent\'s board:')
    print_board_wo(board_op)
    p = True
    while p == True:
        hit_inp = input(pl_name + ' where would you like to hit?')
        if board_op[let.find(hit_inp[0])][int(hit_inp[1])] == 'o':
            board_op[let.find(hit_inp[0])][int(hit_inp[1])] = 'x'
            print('Nice shot!')
            win = winner(board_op, player)
            if win == player:
                p = False
                return win
            else:
                p = True
            print_board_wo(board_op)
        elif board_op[let.find(hit_inp[0])][int(hit_inp[1])] == ' ':
            board_op[let.find(hit_inp[0])][int(hit_inp[1])] = '-'
            print('Nope, not here')
            p = False
        elif board_op[let.find(hit_inp[0])][int(hit_inp[1])] == 'x' or board_op[let.find(hit_inp[0])][int(hit_inp[1])] == '-':
            print('Oops, you tried it already')
            print_board_wo(board_op) 
            p = True
                 
    
#function that calls for guess_ship and winner:
def play_win(board1, board2, u_game, pl_name, ot_name):
#board1 = pl_1
#board2 = pl_2
#pl_name = u1_name
#ot_name = u2_name
    while True:
        player = 1
        w = guess_ship(board1, board2, u_game, pl_name, player)
        if w == 1:
            break
        player = 2
        w = guess_ship(board2, board1, u_game, ot_name, player)
        if w ==2:
            break
        g = save_game(u_game, board1, board2, pl_name, ot_name)
        if g == 'c':
            continue
        elif g == 'exit':
            return g

    if w == 1:
        print('Congratularions! ' + u1_name + ' is the winner!')
    elif w == 2:
        print('Congratularions! ' + u2_name + ' is the winner!')
        
#function to save or continue:
def save_game(u_game, pl1_b, pl2_b, pl1_name, pl2_name):
    u_inp = input('Save game and exit or Continue? please enter s/c:') 
    if u_inp == 's':
        game_data = {'type game':u_game, 'pl1 board':pl1_b,
                     'pl2 board':pl2_b, 'pl1 name':pl1_name, 'pl2 name':pl2_name}
        with open('battleship_game.json', 'w') as game:
           json.dump(game_data, game)
        g = 'exit'
    else:
        g = 'c'
    return g

load_not()  
###      
ship_sqaure = {"option 1": [[5,1],[4,1],[3,2],[2,1]], "option 2":[[4,1],[3,2],[2,3],[1,4]]}
u_game = int(input("Please choose the type of game to play 1 or 2:"))

#players names:
u1_name = input("please enter the first player's name:")
u2_name = input("please enter the second player's name:")
#players boards:
pl_1 = new_board()
pl_2 = new_board()    
creating_pl_boards(pl_1, u_game, u1_name)
creating_pl_boards(pl_2, u_game, u2_name)
#checking for the winner:
play_win(pl_1, pl_2, u_game, u1_name, u2_name)
