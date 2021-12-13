
from typing import DefaultDict
from collections import Counter, defaultdict, deque

import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())

def first():
    inp = open('11_test.txt').read().split('\n')

    inp = [list(map(int, x)) for x in inp]
    

    rc = [1, 1,  0, -1, -1, -1, 0, 1]
    cc = [0, -1, -1, -1, 0, 1, 1, 1]

    scounts=[]
    for x in range(3):
        step_count=0
        for i, a in enumerate(inp):
            for j, b in enumerate(a):
                inp[i][j]+=1

        SEEN=set()
        for i, a in enumerate(inp):
            for j, b in enumerate(a):
                # print(i, j, inp[i][j])
                p = inp[i][j]
                if p>9 and (i,j) not in SEEN:
                    # import pdb
                    # pdb.set_trace()
                    q = deque()
                    q.append((i,j))
                    while q:
                        li,lj = q.popleft()

                        if (li, lj) in SEEN:
                            continue

                        SEEN.add((li,lj))

                        for rs, cs in zip(rc, cc):
                            r = li+rs
                            c = lj+cs

                            # if rs==1 and cs==1:
                            #     import pdb
                            #     pdb.set_trace()

                            if 0<=r<len(inp) and 0<=c<len(inp[0]):
                                inp[r][c]+=1
                                lp = inp[r][c]
                                if lp==10:
                                    if (r,c) not in q:
                                        q.append((r,c))


                                # print('  after', r, c, inp[r][c])
                # print('after', i, j, inp[i][j])

        for i, a in enumerate(inp):
            for j, b in enumerate(a):
                p = inp[i][j]
                # print(i, j, p, inp)
                if p>9:
                    inp[i][j]=0
                    step_count+=1

        scounts.append(step_count)
        print('board at the end',x+1,  inp)

    return sum(scounts)

def second():
    inp = open('11.txt').read().split('\n')

    inp = [list(map(int, x)) for x in inp]
    

    rc = [1, 1,  0, -1, -1, -1, 0, 1]
    cc = [0, -1, -1, -1, 0, 1, 1, 1]

    scounts=[]
    sim_flash=False

    for x in range(1000):
        if sim_flash:
            break
        step_count=0
        for i, a in enumerate(inp):
            if sim_flash:
                break
            for j, b in enumerate(a):
                inp[i][j]+=1

        SEEN=set()
        for i, a in enumerate(inp):
            if sim_flash:
                break

            for j, b in enumerate(a):
                # print(i, j, inp[i][j])

                def check_for_sim_flash(board):
                    for i, a in enumerate(board):
                        for j,b in enumerate(board):
                            if board[i][j]<10:
                                return False
                    return True

                sim_flash = check_for_sim_flash(inp)           
                if sim_flash:
                    break

                p = inp[i][j]
                if p>9 and (i,j) not in SEEN:
                    q = deque()
                    q.append((i,j))
                    while q:
                        li,lj = q.popleft()

                        if (li, lj) in SEEN:
                            continue

                        SEEN.add((li,lj))

                        for rs, cs in zip(rc, cc):
                            r = li+rs
                            c = lj+cs

                            # if rs==1 and cs==1:
                            #     import pdb
                            #     pdb.set_trace()

                            if 0<=r<len(inp) and 0<=c<len(inp[0]):
                                inp[r][c]+=1
                                lp = inp[r][c]
                                if lp==10:
                                    if (r,c) not in q:
                                        q.append((r,c))


                                # print('  after', r, c, inp[r][c])
                # print('after', i, j, inp[i][j])

        for i, a in enumerate(inp):
            if sim_flash:
                break
            for j, b in enumerate(a):
                p = inp[i][j]
                # print(i, j, p, inp)
                if p>9:
                    inp[i][j]=0
                    step_count+=1

        # scounts.append(step_count)
        print('board at the end',x+1)

    return x

if __name__=="__main__":
    print(second())