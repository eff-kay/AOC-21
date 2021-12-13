
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string

import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())

def first():
    inp = open('12_t2.txt').read().split('\n')

    g = {}

    for x in inp:
        s, e  = x.split('-')
        if s not in g:
            g[s] = [e]
        else:
            g[s].append(e)

        if e not in g:
            g[e] = [s]
        else:
            g[e].append(s)

    Q = deque()
    st = 'start'
    Q.append(st)

    paths = defaultdict(list)
    paths[st] = [[st]]
    old_paths = paths

    print(g)
    i=0
    c=0
    while Q:
        sou = Q.popleft()
        for ne in g[sou]:
            # print(sou, ne, paths, Q)
            if ne!='start' and ne!='end':
                Q.append(ne)
                for path in paths[sou]:
                    new_path = path+[ne]
                    # check if the existing path persists
                    exists=False
                    for x in paths[ne]:
                        exists |= all([(a==b) and len(x)==len(new_path) for a,b in zip(x, new_path)])

                    # print('sinle path', sou, ne, path, exists,  new_path, paths[ne])
                    if not exists:
                        print('not exists')
                        if ne.startswith(string.ascii_lowercase) and ne not in path and path[0]=='start':
                            paths[ne].append(path+[ne])
                        elif ne in string.ascii_uppercase:
                            paths[ne].append(path+[ne])

            elif ne=='end':
                for path in paths[sou]:
                    new_path = path+[ne]
                    # check if the existing path persists
                    exists=False
                    for x in paths[ne]:
                        exists |= all([a==b and len(x)==len(new_path) for a,b in zip(x, new_path)])
                        # print('x ', x, 'new path', new_path, exists)

                    if not exists:
                        if ne not in path and path[0]=='start':
                            paths[ne].append(path+[ne])
                            # print('appending end', sou, ne, Q, paths)
                
            # print('paths', i, sou, ne, paths.get('end'), Q)
        i+=1
        if i==50:
            break
    
        def check_for_changes(old_g, new_g):
            if old_g!=[] and new_g!=[]:
                if len(old_g)==len(new_g):
                    for x,y in zip(old_g, new_g):
                        if len(x)==len(y):
                            if not all([i==j for i,j in zip(x,y)]):
                                return False
                        else:
                            return False
                        return True
                    return True
                else:
                    return False
            else:
                return False

        old_end = old_paths.get('end', [])
        n_end = paths.get('end', [])
        same = check_for_changes(old_end, n_end)
        print(old_end, n_end)
        print('same ', same, c)
        if same:
            if c==30:
                break
            else:
                c+=1
        else:
            old_paths = {k:list(v) for k, v in paths.items()}
            c=0



            
    # print(paths)
    # create a graph
    # get the pathts
        # when you reach the end
        # check if the number of 'lower' characters in the paths is more than 1
        # store if the answer is yes
    # stop when all of the combinations have been tried
    # make sure you don't visit start

def second():
    pass

if __name__=="__main__":
    print(first())