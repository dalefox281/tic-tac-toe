#!/usr/bin/env python3

import pprint

def main():
    # testBoard = [['X','X','X'],[None, None, None],[None, None, None]]
    board = []
    game = True
    render_board(new_board(board))
    while game == True:
        render_board(board)

def new_board(board):
    board = [[None, None, None],[None, None, None],[None, None, None]]
    return board

def render_board(board):
    for item in board:
<<<<<<< HEAD
        print(item)

def main():
    board = []
    player = str('')
    print("Welcome to tic-tac-toe!")
    input(print("Choose a side; X's or O's"))
    
    print(render_board(new_board()))
=======
        pprint.pprint(item)
        
>>>>>>> a5ececff632659bb2e59b9e851e648281f76cd24

if __name__ == "__main__":
    board = []
    main()