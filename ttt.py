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
        pprint.pprint(item)
        

if __name__ == "__main__":
    board = []
    main()