#!/usr/bin/env python3

def new_board():
    board = [[None, None, None], 
             [None, None, None], 
             [None, None, None]]
    return board

def render_board(board):
    for item in board:
        print(item)
    
print(render_board(new_board()))
