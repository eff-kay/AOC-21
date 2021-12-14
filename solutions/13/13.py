
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string

import sys
sys.setrecursionlimit(15000)

def first():
    inp = open('13_t1.txt').read()

    inp = inp.split('\n')  

    sp = inp.index('')
    grid = inp[:sp]
    ins = inp[sp+1:]

    grid = [list(map(int, x.split(','))) for x in grid]
    ins = [x.split(' ')[-1] for x in ins] 

    print(ins)
    max_y = max(grid, key=lambda x:x[1])[1]
    max_x = max(grid, key=lambda x:x[0])[0]

    # print(max_y, max_x, type(max_x))
    def draw_board(inst):
        board = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
        for x,y in inst:
            board[y][x] = '#'
        return board
    
    board = draw_board(grid)
    # print(board)

    for step in ins:
        ax, co = step.split('=')
        co = int(co)

        if ax=='y':
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if y>=co and col=='#':
                        # print('y', y, (2*co)-y, x, col)
                        board[(2*co)-y][x] = board[y][x]
            board = board[:co]
        
        if ax=='x':
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if x>=co and col=='#':
                        # print('y', y, (2*co)-x, col)
                        board[y][(2*co)-x] = board[y][x]

            board = [x[:co] for x in board]
        # print('step', step, board)

    print(board)
    count=0
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col=='#':
                count+=1

    return count


def second():
    inp = open('13.txt').read()

    inp = inp.split('\n')  

    sp = inp.index('')
    grid = inp[:sp]
    ins = inp[sp+1:]

    grid = [list(map(int, x.split(','))) for x in grid]
    ins = [x.split(' ')[-1] for x in ins] 

    max_y = max(grid, key=lambda x:x[1])[1]
    max_x = max(grid, key=lambda x:x[0])[0]

    # print(max_y, max_x, type(max_x))
    def draw_board(inst):
        board = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
        for x,y in inst:
            board[y][x] = '#'
        return board
    
    board = draw_board(grid)
    # print(board)

    for step in ins:
        ax, co = step.split('=')
        co = int(co)

        if ax=='y':
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if y>=co and col=='#':
                        # print('y', y, (2*co)-y, x, col)
                        board[(2*co)-y][x] = board[y][x]
            board = board[:co]
        
        if ax=='x':
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if x>=co and col=='#':
                        # print('y', y, (2*co)-x, col)
                        board[y][(2*co)-x] = board[y][x]

            board = [x[:co] for x in board]
        # print('step', step, board)

    print(board)

if __name__=="__main__":
    print(second())