
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string
from numpy import product, ubyte
from numpy.lib.arraysetops import isin
import pandas as pd

import sys
sys.setrecursionlimit(15000)

def first():

    # X = 20, 30
    # Y = -10, -5

    #  x=96..125, y=-144..-98
    X  = 96, 125
    Y = -144, -98

    ans = 0
    for DX in range(0, 1000):
        for DY in range(-200, 200):
            ok = False
            x = 0
            y = 0
            dx = DX
            dy = DY
            maxy = 0
            # print(dx, dy)
            for t in range(500):
                x = x+dx
                y = y+dy
                maxy = max(maxy, y)
                if dx>0:
                    dx-=1
                elif dx<0:
                    dx+=1
                dy-=1

                if X[0]<=x<=X[1] and Y[0]<=y<=Y[1]:
                    ok = True
            
            if ok:
                print(DX, DY)
                ans = max(maxy, ans)
    print(ans)

def second():
    # X = 20, 30
    # Y = -10, -5

    #  x=96..125, y=-144..-98
    X  = 96, 125
    Y = -144, -98

    answers = []
    for DX in range(0, 1000):
        for DY in range(-200, 200):
            ok = False
            x = 0
            y = 0
            dx = DX
            dy = DY
            maxy = 0
            # print(dx, dy)
            for t in range(500):
                x = x+dx
                y = y+dy
                maxy = max(maxy, y)
                if dx>0:
                    dx-=1
                elif dx<0:
                    dx+=1
                dy-=1

                if X[0]<=x<=X[1] and Y[0]<=y<=Y[1]:
                    ok = True
            
            if ok:
                print(DX, DY)
                answers.append(maxy)
                # if maxy< ans:
                #     print('less than event', maxy)                
                # print(ans)
    print(len(answers))
if __name__=="__main__":
    print(second())