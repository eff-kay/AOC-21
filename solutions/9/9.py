
from typing import DefaultDict
from collections import defaultdict, deque
import sys

sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())
def first():
    inp = open('9.txt').read()
    inp = inp.split('\n')
    inp = [list(map(int, list(x))) for x in inp]

    print(len(inp), len(inp[0]))

    def t_board(board, i, j, count, points):
        if i==len(board)-1 and j==len(board[0])-1:
            return points
        else: 
            dstep, ustep, rstep, lstep= 1, 1, 1, 1
            if i==len(board)-1:
                dstep = 0
            elif i==0:
                ustep = 0
            if j==len(board[0])-1:
                rstep = 0
            elif j==0:
                lstep = 0

            point = board[i][j]


            if point< board[i-ustep][j] if ustep!=0 else point<float('inf'):
                if point< board[i+dstep][j] if dstep!=0 else point<float('inf'):
                    if point < board[i][j+rstep] if rstep!=0 else point<float('inf'):
                        if point< board[i][j-lstep] if lstep!=0 else point<float('inf'):
                            points.append(point)
            
            if j==len(board[0])-1 and i<len(board)-1:
                i+=1
                j=0
            elif j<len(board[0])-1:
                j+=1
            print(i,j) 
            return t_board(board, i, j, count, points)

    count = 0
    board = inp
    points = []
    points = t_board(board, 0, 0, count, points)

    return sum([x+1 for x in points])

def second():
    inp = open('9.txt').read()
    inp = inp.split('\n')
    inp = [list(map(int, list(x))) for x in inp]

    print(len(inp), len(inp[0]))

    def t_board(board, i, j, SEEN:set(), S:list()):
        if i==len(board)-1 and j==len(board[0])-1:
            return S
        else: 

            rst = [-1,0,1,0]
            cst = [0,1,0,-1]

            # print(i,j)
            if (i,j) not in SEEN and board[i][j]!=9:
                print(board[i][j])
                q = deque()
                q.append((i,j))

                lsize=0
                while q:
                    r,c = q.popleft()

                    if (r,c) in SEEN:
                        continue

                    SEEN.add((r,c))

                    lsize+=1
                    for rs, cs in zip(rst, cst):
                        x = r+rs
                        y = c+cs
                        if 0<=x<=len(board)-1 and 0<=y<=len(board[0])-1 and board[x][y] !=9:
                            # print('basin', x, y, board[x][y], SEEN)
                            q.append((x,y))
                    # print(q)
                # print('size', lsize)
                S.append(lsize)
        
            if j<=len(board[0])-1:
                j+=1

            if j==len(board[0]):
                i+=1
                j=0
            return t_board(board, i, j, SEEN, S)

    count = 0
    board = inp
    points = []
    SEEN = set()
    S = []
    sizes = t_board(board, 0, 0, SEEN, S)

    from functools import reduce
    print(reduce(lambda x,y:x*y, sorted(sizes)[-3:]))
    # return sum([x+1 for x in points])

if __name__=="__main__":
    print(second())