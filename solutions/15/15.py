
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string
from numpy import ubyte
import pandas as pd

import sys
sys.setrecursionlimit(15000)

def first():
    inp = open('15.txt').read()
    inp = inp.split('\n')

    inp = [list(map(int, list(x))) for x in inp]
    # print(inp)

    board = [[0]*len(inp[0]) for _ in range(len(inp))]

    inp[0][0] = 0
    # print(len(board), len(board[0]))
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if i==0 and j!=0:
                if j==1:
                   board[i][j] = inp[0][j] 
                else:
                    board[i][j] = board[0][j-1]+inp[0][j]
            elif j==0 and i!=0:
                if i==1:
                   board[i][j] = inp[i][0] 
                else:
                    board[i][j] = board[i-1][0]+inp[i][0]
            else:
                board[i][j] = min(board[i-1][j], board[i][j-1]) + inp[i][j]

    # print(board[-1][-1], inp[0][0])
    # print([x[:6] for x in board[:4]])
    # print(board)
    ans = board[-1][-1]

    # df = pd.DataFrame(board)
    print(df)

    return ans
    # di = defaultdict(str)

    # for instruct in ins:
    #     left, right = instruct.split(' -> ') 
    #     di[left] = right
    
    # # print(di, tem)
    # # consider every pair in template
    # tem = tem[0]
    # # cache = {}
    # for _ in range(40):
    #     new_p = ''
    #     for i in range(1, len(tem)):
    #         pair = tem[i-1]+tem[i] 

    #         # print(pair, i, di[pair], tem, pair in di, new_p, tem[i-1] + di[pair]+ tem[i])
    #         if pair in di:
    #             bef = new_p[:i-1]
    #             mid = tem[i-1]+di[pair]+tem[i]
    #             # te = di[pair]
    #             # aft = new_p[i+1:]
    #             if len(new_p)>0:
    #                 new_p += mid[1:]
    #             else:
    #                 new_p = mid
    #             # print(bef, mid)
    #             # print(new_p)
        
    #     tem=new_p


    # count = Counter(new_p) 

    # values = list(count.values())
    # print(values)
    # print(max(values)-min(values))
    # create a hash of instructions

import heapq
def first_1():
    inp = open('15.txt').read()
    inp = inp.split('\n')

    inp = [list(map(int, list(x))) for x in inp]
    # print(inp)

    hq = [(0,0,0)]

    heapq.heapify(hq)
    cost = defaultdict(int)

    while hq:
        c, row, col = heapq.heappop(hq)

        if (row, col) in cost and c>=cost[(row, col)]:
            continue
        # visited.add((row, col))
        cost[(row, col)] = c

        for rs, cs in ((0,1), (0,-1), (1, 0), (-1,0)):
            rr = row+rs
            cc = col+cs

            if not (0<=rr<len(inp) and 0<=cc<len(inp[0])):
                continue

            heapq.heappush(hq, (c+ inp[rr][cc], rr, cc))


    print(cost[(len(inp)-1, len(inp[0])-1)])

def second():
    inp = open('15.txt').read()
    inp = inp.split('\n')

    inp = [list(map(int, list(x))) for x in inp]
    df = pd.DataFrame(inp)

    N = len(inp)
    M = len(inp[0])

    rows = len(inp)*5
    cols = len(inp[0])*5

    def wmod(n):
        if n>9:
            n-=9
        return n

    def get(r, c):
        x = (inp[r%N][c%M] + (r//N) + (c//M))
        return wmod(x)


    # print(df.shape)
    tempi = [[wmod(x[i%M]+i//M) for i in range(cols)] for x in inp]
    temp = tempi
    for i in range(1, 5):
        tempj = [[wmod(x+i) for x in y] for y in tempi]
        temp = temp+tempj

    # # print(inp)
    # # for i in range(len(inp[0])*5):

    # # print(inp)

    # # df = pd.DataFrame(temp)
    # # print(df.shape)
    from copy import deepcopy
    inp = deepcopy(temp)
    # df = pd.DataFrame(inp)
    # print(df.shape)

    # print(inp)
    hq = [(0,0,0)]

    heapq.heapify(hq)
    cost = defaultdict(int)

    while hq:
        c, row, col = heapq.heappop(hq)

        if (row, col) in cost and c>=cost[(row, col)]:
            continue
        # visited.add((row, col))
        cost[(row, col)] = c

        for rs, cs in ((0,1), (0,-1), (1, 0), (-1,0)):
            rr = row+rs
            cc = col+cs

            if not (0<=rr<rows and 0<=cc<cols):
                continue
            heapq.heappush(hq, (c+ inp[rr][cc], rr, cc))


    # print(cost)
    print(cost[(rows-1, cols-1)])

if __name__=="__main__":
    print(second())