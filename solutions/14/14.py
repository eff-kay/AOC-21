
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string

import sys
sys.setrecursionlimit(15000)

def first():
    inp = open('14_t1.txt').read()

    inp = inp.split('\n')

    ind = inp.index('')
    tem, ins = inp[:ind], inp[ind+1:]

    di = defaultdict(str)

    for instruct in ins:
        left, right = instruct.split(' -> ') 
        di[left] = right
    
    # print(di, tem)
    # consider every pair in template
    tem = tem[0]
    # cache = {}
    for _ in range(10):
        new_p = ''
        for i in range(1, len(tem)):
            pair = tem[i-1]+tem[i] 

            # print(pair, i, di[pair], tem, pair in di, new_p, tem[i-1] + di[pair]+ tem[i])
            if pair in di:
                bef = new_p[:i-1]
                mid = tem[i-1]+di[pair]+tem[i]
                # te = di[pair]
                # aft = new_p[i+1:]
                if len(new_p)>0:
                    new_p += mid[1:]
                else:
                    new_p = mid
                # print(bef, mid)
                # print(new_p)
        
        tem=new_p


    count = Counter(new_p) 

    values = list(count.values())
    print(values)
    print(max(values)-min(values))
    # create a hash of instructions

def second():
    ans = 0
    inp = open('14.txt').read()

    inp = inp.split('\n')

    ind = inp.index('')
    tem, ins = inp[:ind], inp[ind+1:]

    di = defaultdict(str)

    for instruct in ins:
        left, right = instruct.split(' -> ') 
        di[left] = right
    
    # print(di, tem)
    # consider every pair in template
    tem = tem[0]
    cache = {k:k[0]+v+k[1] for k,v in di.items()}
    count_p = Counter([tem[i-1]+tem[i] for i in range(1, len(tem))])

    print(count_p)
    for a in range(40):
        new_d = {}
        for k, v in count_p.items():
            if k in cache:
                pa, pb = cache[k][:2], cache[k][1:]
                if pa in new_d:
                    new_d[pa]+=v
                else:
                    new_d[pa] = v
                
                if pb in new_d:
                    new_d[pb]+=v
                else:
                    new_d[pb] = v

                # print(f'{k} in cache', new_d)
        count_p = new_d
        # count_p = Counter([tem[i-1]+tem[i] for i in range(1, len(tem))])
        print(f'step {a} done')

    print(new_d)
    new_d1=defaultdict(int)
    for k,v in new_d.items():
        new_d1[k[0]]+=v
        new_d1[k[1]]+=v
        print(k,v, new_d1)
    # new_s = ''.join([new_d.keys())
    # print(new_d1)
    # # count = Counter(new_d1) 
    count = new_d1

    # count=nmew
    values = list(count.values())
    values = [v/2 for v in values]
    # print([v/2 for v in values])
    print(values)
    ans = max(values)-min(values)
    import math
    ans = math.ceil(ans)

    print(ans)
    # assert ans == 2188189693529


if __name__=="__main__":
    print(second())