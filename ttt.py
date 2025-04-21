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
        print(item)

def main():
    board = []
    player = str('')
    print("Welcome to tic-tac-toe!")
    input(print("Choose a side; X's or O's"))
    
    print(render_board(new_board()))

if __name__ == "__main__":
    board = []
    main()