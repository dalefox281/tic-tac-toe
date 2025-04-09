#!/usr/bin/env python3

def new_board():
    global board
    board = [[None, None, None],[None, None, None],[None, None, None],]
    return board

def render_board(board):
    for item in board:
        print(item)

def main():
    board = []
    print(render_board(new_board()))

if __name__ == "__main__":
    main()