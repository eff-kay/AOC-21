
import collections
from os import device_encoding
from typing import DefaultDict
from collections import Counter, defaultdict, deque
import string

import sys
sys.setrecursionlimit(15000)

def first():
    inp = open('12.txt').read().split('\n')

    g = defaultdict(set)

    for x in inp:
        s, e  = x.split('-')
        g[s].add(e)
        g[e].add(s)

    print(g)
    todo = deque([('start',)])
    paths = set()    

    while todo:
        path = todo.popleft()

        print('path', path)
        if path[-1]=='end':
            paths.add(path)
            continue
        
        print('end', path[-1])
        for ne in g[path[-1]]:
            print('ne', ne)
            if ne.isupper() or ne not in path:
                todo.append((*path, ne))
    
    # print(paths)
    return len(paths)

def second():
    inp = open('12.txt').read().split('\n')

    g = defaultdict(set)

    for x in inp:
        s, e  = x.split('-')
        g[s].add(e)
        g[e].add(s)

    todo = deque([(('start',), None)])
    paths = set()    

    def count_node(node, path):
        nu = 0

        for nod in path:
            if node==nod:
                nu+=1
        return nu

    node_with_two = None
    add=False

    while todo:
        path, twice_sm = todo.popleft()

        # print('path', path)
        if path[-1]=='end':
            paths.add(path)
            continue
        
        # print('end', path[-1])
        for ne in g[path[-1]]:
            if ne!='start':
                if ne.isupper():
                    todo.append(((*path, ne), twice_sm))
                elif twice_sm is None and path.count(ne)==1:
                    todo.append(((*path, ne), ne))
                elif twice_sm==ne and path.count(ne)==0:
                    todo.append(((*path, ne), twice_sm))
                elif twice_sm!=ne and path.count(ne)==0:
                    todo.append(((*path, ne), twice_sm))

        
    # print(paths)
    return len(paths)


if __name__=="__main__":
    print(second())