'''
Created on 18 Jan 2020

@author: Arezo
'''
from random import choice
        
def display_board(board):
    print('\n')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('------- ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------- ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('\n')

def player_input(ply):
    player1 =''
    
    while player1 !='x' and player1 != 'o':
        player1 = input(f'{ply} select your favorite marker x or o')
    
    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
        
    return (player1, player2)
        

def place_marker(board, marker, position):
       
    board[position]=marker
     

def win_check(board, marker):
        
    if board[1] == board[2] == board[3]== marker:
        return True
    
    if board[4] == board[5] == board[6]== marker:
        return True
        
    if board[7] == board[8] == board[9]== marker:
        return True
    
    if board[1] == board[4] == board[7]== marker:
        return True
    
    if board[2] == board[5] == board[8]== marker:
        return True
        
    if board[3] == board[6] == board[9]== marker:
        return True
        
    if board[1] == board[5] == board[9]== marker:
        return True

    if board[3] == board[5] == board[7]== marker:
        return True


def choose_first():
    name1 = input('What is your name? ')
        
    while not name1:
        print('You should enter a name')
        name1 = input('What is your name? ')
    
    name2 = input('What is other player name? ')
    while not name2:
        print('You should enter a name')
        name2 = input('What is your name? ')
           
    player = choice([name1, name2])
    
    print(f'{player} should start the game')
    player1 = player
    if player1 == name1:
        player2 =  name2
    else:
        player2 = name1 
    return player1, player2

        
def space_check(board, position):
    if board[position] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False


def full_board_check(board):
    count =0
    for i in range(1,10):
        if board[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count +=1
    if count == 0:
        return True
    else:
        return False

def player_choice(board, player):
    while True:
        try:
            position = int(input(f'{player} enter your desire position from 1-9 '))
            while position ==0 or position > 9:
                position = int(input(f'{player} please enter a position in range 1-9 '))       
            break
        except ValueError:
            print('please enter integer')
        
    while not space_check(board, position):
        while True:
            try:
                position = int(input(f'{player} please enter an empty position from 1-9 '))
                while position ==0 or position > 9:
                    position = int(input(f'{player} please enter a position in range 1-9 '))       
                break
            except ValueError:
                print('please enter integer')
        space_check(board, position)
    return position
       

def replay():
    answer = input('do you want to play again? y/n ')
    if answer == 'y':
        return True
    else:
        return False

def tic_tac_toe():    
    print('Welcome to Tic Tac Toe!')
    
    while True:
        board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            
        game_on = True
    
        display_board(board)
        player1, player2 = choose_first()
        
        player1_marker, player2_marker = player_input(player1)
        
        while game_on:
            # player1
            if not full_board_check(board): 
                position = player_choice(board, player1)                
                place_marker(board, player1_marker, position)
                display_board(board)
                if win_check(board, player1_marker):
                    print(f'Conguradulation {player1},  you win.')
                    game_on = False
                if full_board_check(board):
                    game_on = False
                
                # player2
                if game_on:
                    position = player_choice(board, player2)                   
                    place_marker(board, player2_marker, position)
                    display_board(board)
                    if win_check(board, player2_marker):
                        print(f'Conguradulation {player2} you win')
                        game_on = False
                    if full_board_check(board):
                        game_on = False
                        
                    
        if game_on == False: 
            if full_board_check(board):
                print('sorry board is full')
                if not replay():
                    break
            else:
                if not replay():
                    break      

tic_tac_toe() 