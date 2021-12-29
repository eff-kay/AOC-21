import re,ast
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
    def check_for_explode(expr, new_l, depth, explosion, lc, rc):
        if depth==3 and not explosion:
            new_expr = [0]*len(expr)
            expl_ind = len(expr)
            for i in range(len(expr)):
                if isinstance(expr[i], list):
                    if not explosion:
                        lc, rc = expr[i]
                        expl_ind = i
                        explosion = True
                    else:
                        left_val, right_val = expr[i]
                        left_val+=rc
                        rc = 0
                        new_expr[i] = [left_val, right_val]
                else: 
                    new_expr[i] = expr[i]+rc
                    rc = 0


            if lc!=0:
                # print('outer lc remaining', lc, new_expr)
                def update_lc(new_expr, expl_ind, lc):
                    temp_expr = new_expr[:expl_ind]
                    for i in range(len(temp_expr)-1, -1, -1):
                        if not isinstance(temp_expr[i], list):
                            new_expr[i] = new_expr[i]+lc
                            lc = 0
                            return new_expr, lc
                        else:
                            ret_expr, lc = update_lc(temp_expr[i], len(temp_expr[i]), lc)
                            new_expr[i] = ret_expr
                    
                    # print('update loc ret_expr', new_expr)
                    return new_expr, lc
                new_expr, lc = update_lc(new_expr, expl_ind, lc)

                # print('lc', i, 'depth 3', 'expr', expr, 'new_expr', new_expr, lc, rc)
            return new_expr, lc, rc, explosion
        
        new_expr=['i']*len(expr)
        expl_ind = len(expr)
        for i, x in enumerate(expr):
            if isinstance(x, list):
                ret_expr = check_for_explode(x, [], depth+1, explosion, lc, rc)
                # print('ret expr', ret_expr)
                new_expr[i], lc, rc, explosion = ret_expr
                expl_ind = i
            else:
                new_expr[i] = expr[i]+rc
                rc = 0

        # print('new expr', new_expr)

        if lc!=0:
            # print('outer lc remaining', lc, new_expr)
            def update_lc(new_expr, expl_ind, lc):
                temp_expr = new_expr[:expl_ind]
                for i in range(len(temp_expr)-1, -1, -1):
                    if not isinstance(temp_expr[i], list):
                        new_expr[i] = new_expr[i]+lc
                        lc = 0
                        return new_expr, lc
                    else:
                        ret_expr, lc = update_lc(temp_expr[i], len(temp_expr[i]), lc)
                        new_expr[i] = ret_expr
                
                # print('update loc ret_expr', new_expr)
                return new_expr, lc
            new_expr, lc = update_lc(new_expr, expl_ind, lc)

        # print('final expr', expr, 'new_expr', new_expr, lc, rc)
        return new_expr, lc, rc, explosion


    exprs = [ 
        # [[[[[9,8],1],2],3],4],
        # [7,[6,[5,[4,[3,2]]]]],
        # [[6,[5,[4,[3,2]]]],1], 
        # [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],
        # [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],
        # [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]],
        # [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
        # [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]],
        # [[[[0, [3,2]],[3,3]],[4,4]],[5,5]],
        # [[[[12, 0], [[12, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]], [2, 9]]
        # [[[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]], [2, 9]]
    ]
        
    res_exprs = [
        # [[[[0,9],2],3],4],
        # [7,[6,[5,[7,0]]]],
        # [[6,[5,[7,0]]],3],
        # [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],
        # [[3,[2,[8,0]]],[9,[5,[7,0]]]],
        # [[[[0,7],4],[15,[0,13]]],[1,1]],
        # [[[[0,7],4],[7,[[8,4],9]]],[1,1]],
        # [[[[3, 0],[5,3]],[4,4]],[5,5]],
        # [[[[12, 12], [0, [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]], [2, 9]]
        # []
    ]

    for exp, res_exp in zip(exprs, res_exprs):
        print(exp)
        new_expr, lc, rc, explosion = check_for_explode(exp, [], 0, False, 0, 0)
        print(new_expr, lc, rc, explosion)
        assert new_expr == res_exp, f'{new_expr} != {res_exp}'


    def check_for_split(expr, split):
        # print(expr)
        new_expr = ['i']*len(expr)
        for i, x in enumerate(expr):
            if isinstance(x, list):
                ret_exp, split = check_for_split(x, split)
                new_expr[i] = ret_exp
            else:
                if x>=10 and not split:
                    import math
                    l, r = math.floor(x/2), math.ceil(x/2)
                    new_expr[i] = [l, r]
                    split=True
                else:
                    new_expr[i] = x

        # print(expr, new_expr)
        return new_expr, split

    # exprs = [
    #     [[[[0,7],4],[15,[0,13]]],[1,1]],
    #     [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    # ]
    # res_exprs = [
    #     [[[[0,7],4],[[7,8],[0,13]]],[1,1]],
    #     [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    # ]

    # for exp, res_exp in zip(exprs, res_exprs):
    #     r_exp, split = check_for_split(exp, False)
    #     print(r_exp)
    #     assert r_exp==res_exp

    # simple addition

    def add(first, second):
        add_res = [first, second]
        in_progress = True
        new_res = add_res

        def reduce(new_res):
            print('starting', new_res)
            new_res, lc, rc, explosion = check_for_explode(new_res, [], 0, False, 0, 0)
            if explosion:
                return reduce(new_res)
            else:
                new_res, split = check_for_split(new_res, False)
                if split:
                    return reduce(new_res)
                else:
                    return new_res


        return reduce(new_res)



    def explode(n):
        ns = str(n)
        nums = re.findall('\d+', ns)
        parts = []
        i = 0
        while i < len(ns):
            if ns[i] == '[':
                parts.append('[')
                i += 1
            elif ns[i] == ',':
                parts.append(',')
                i += 1
            elif ns[i] == ']':
                parts.append(']')
                i += 1
            elif ns[i] == ' ':
                i += 1
            else:
                assert ns[i].isdigit()
                j = i
                while j < len(ns) and ns[j].isdigit():
                    j += 1
                parts.append(int(ns[i:j]))
                i = j

        depth = 0
        for i,c in enumerate(parts):
            if c=='[':
                depth += 1
                if depth == 5:
                    old_ns = ns
                    left = parts[i+1]
                    assert isinstance(left, int)
                    assert parts[i+2] == ','
                    right = parts[i+3]
                    assert isinstance(right, int)
                    left_i = None
                    right_i = None
                    for j in range(len(parts)):
                        if isinstance(parts[j], int) and j < i:
                            left_i = j
                        elif isinstance(parts[j], int) and j>i+3 and right_i is None:
                            right_i = j
                    if right_i is not None:
                        assert right_i > i
                        parts[right_i] += right
                    parts = parts[:i] + [0] + parts[i+5:]
                    if left_i is not None:
                        parts[left_i] += left
                    return True, ast.literal_eval(''.join([str(x) for x in parts]))
            elif c==']':
                depth -= 1
            else:
                pass

        return False, n

    def add_1(first, second):
        add_res = [first, second]
        in_progress = True
        new_res = add_res

        def reduce(new_res):
            # print('starting', new_res)
            th, res = explode(new_res)
            if th:
                return reduce(res)
            else:
                new_res, split = check_for_split(new_res, False)
                if split:
                    return reduce(new_res)
                else:
                    return new_res
                
        return reduce(new_res)
    expr_l = [[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]
    # res = add(expr[0], expr[1])
    # assert res == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

    # print(res)

#     expr_l = [[1,1],
# [2,2],
# [3,3],
# [4,4],
# [5,5],
# [6,6]]
    
    # expr_l = [[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]] ,[2,9]]

    def mag(res):
        if isinstance(res, list):
            left = 3*mag(res[0])
            right = 2*mag(res[1])
            return left+right
        else:
            return res

    assert mag([9,1])==29
    assert mag([[9,1],[1,9]]) == 129
    assert mag([[1,2],[[3,4],5]]) == 143
    assert mag([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    assert mag([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
    assert mag([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
    assert mag([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
    assert mag([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

    expr_l = open('18.txt').read().split('\n')
    expr_l = [eval(x) for x in expr_l]
    # print('adding', expr_l[0], expr_l[1])
    res = add_1(expr_l[0],expr_l[1])
    # print('add res', res)
    
    # raise Exception()
    for i, x in enumerate(expr_l[2:], 2):
        # print('adding', res, x)
        res = add_1(res, x)
        # print('add res', res)

    mag_n = mag(res)
    print('res', mag_n)

def second():
    def check_for_split(expr, split):
        # print(expr)
        new_expr = ['i']*len(expr)
        for i, x in enumerate(expr):
            if isinstance(x, list):
                ret_exp, split = check_for_split(x, split)
                new_expr[i] = ret_exp
            else:
                if x>=10 and not split:
                    import math
                    l, r = math.floor(x/2), math.ceil(x/2)
                    new_expr[i] = [l, r]
                    split=True
                else:
                    new_expr[i] = x

        # print(expr, new_expr)
        return new_expr, split


    def explode(n):
        ns = str(n)
        nums = re.findall('\d+', ns)
        parts = []
        i = 0
        while i < len(ns):
            if ns[i] == '[':
                parts.append('[')
                i += 1
            elif ns[i] == ',':
                parts.append(',')
                i += 1
            elif ns[i] == ']':
                parts.append(']')
                i += 1
            elif ns[i] == ' ':
                i += 1
            else:
                assert ns[i].isdigit()
                j = i
                while j < len(ns) and ns[j].isdigit():
                    j += 1
                parts.append(int(ns[i:j]))
                i = j

        depth = 0
        for i,c in enumerate(parts):
            if c=='[':
                depth += 1
                if depth == 5:
                    old_ns = ns
                    left = parts[i+1]
                    assert isinstance(left, int)
                    assert parts[i+2] == ','
                    right = parts[i+3]
                    assert isinstance(right, int)
                    left_i = None
                    right_i = None
                    for j in range(len(parts)):
                        if isinstance(parts[j], int) and j < i:
                            left_i = j
                        elif isinstance(parts[j], int) and j>i+3 and right_i is None:
                            right_i = j
                    if right_i is not None:
                        assert right_i > i
                        parts[right_i] += right
                    parts = parts[:i] + [0] + parts[i+5:]
                    if left_i is not None:
                        parts[left_i] += left
                    return True, ast.literal_eval(''.join([str(x) for x in parts]))
            elif c==']':
                depth -= 1
            else:
                pass

        return False, n

    def add_1(first, second):
        add_res = [first, second]
        in_progress = True
        new_res = add_res

        def reduce(new_res):
            # print('starting', new_res)
            th, res = explode(new_res)
            if th:
                return reduce(res)
            else:
                new_res, split = check_for_split(new_res, False)
                if split:
                    return reduce(new_res)
                else:
                    return new_res
                
        return reduce(new_res)
    expr_l = [[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]

    def mag(res):
        if isinstance(res, list):
            left = 3*mag(res[0])
            right = 2*mag(res[1])
            return left+right
        else:
            return res

    expr_l = open('18.txt').read().split('\n')
    expr_l = [eval(x) for x in expr_l]

    from itertools import permutations
    
    resul = list(permutations(expr_l, 2))
    # print(len(resul), resul[0])
    # print('adding', expr_l[0], expr_l[1])

    max_mag = 0
    mags = []
    for x,y in resul:
        res = add_1(x,y)
        mag_n = mag(res)
        mags.append(mag_n)

    print('res', max(mags))

if __name__=="__main__":
    print(second())