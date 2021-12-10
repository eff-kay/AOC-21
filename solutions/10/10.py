
from typing import DefaultDict
from collections import defaultdict, deque
import sys
from collections import Counter
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())

def first():
    inp = open('10.txt').read()
    inp = inp.split('\n')
    
    res= []
    for l in inp:
        d = {')':'(', '}':'{', '>':'<', ']':'['}
        dup = {'(':')', '{':'}', '<':'>', '[':']'}
        stack = []
        for x in l:
            if x in list(d.keys()):
                if stack[-1]==d[x]:
                    stack.pop()
                else:
                    res.append(x)
                    print(x)
                    break
            else:
                stack.append(x)

    dup = {')':3, '}':1197, '>':25137, ']':57}
    c = [v*dup[k] for k,v in Counter(res).items()]
    print(c)
    return sum(c)


def second():
    inp = open('10.txt').read()
    inp = inp.split('\n')
    
    res= []
    for l in inp:
        d = {')':'(', '}':'{', '>':'<', ']':'['}
        dup = {'(':')', '{':'}', '<':'>', '[':']'}
        stack = []
        for i, x in enumerate(l):
            if x in list(d.keys()):
                if stack[-1]==d[x]:
                    stack.pop()
                else:
                    # res.append((l, d))
                    break
            else:
                stack.append(x)

            if i==len(l)-1:
                res.append((l, stack))

    dup = {')':3, '}':1197, '>':25137, ']':57}

    inv = {'(':')', '{':'}', '<':'>', '[':']'}
    sols = []
    for l, d in res:
        t_sol = [inv[x] for x in d][::-1]
        sols.append(t_sol)

    p = {')':1, '}':3, '>':4, ']':2}


    counts = []

    for sol in sols:
        total = 0
        for x in sol:
            total*=5
            total+=p[x]

        counts.append(total)

    import math
    ind = len(counts)//2
    print(sorted(counts)[ind])

if __name__=="__main__":
    print(second())