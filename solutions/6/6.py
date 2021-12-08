import pandas as pd
from collections import Counter
def first():
    inp = open('6_test.txt').read().split(',')
    a = list(map(int, inp))
    for day in range(80):
        lena = len(a)
        for i in range(lena):
            if a[i]==0:
                a[i]=6
                a.append(8)
            else:
                a[i]-=1
    print(len(a))

def first_eff():
    inp = open('6.txt').read().split(',')
    a = list(map(int, inp))
    from collections import defaultdict

    ad = defaultdict(int)
    for k in a:
        ad[k] +=1

    for day in range(256):
        print('day', day)
        new_ad = defaultdict(int)
        keys = list(ad.keys())
        for k in keys:
            if k==0:
                new_ad[8]+=ad[k]
                new_ad[6]+=ad[k]
            else:
                new_ad[k-1]+=ad[k]
                # print('k', k, ad, new_ad)
        ad= new_ad

    print('ad', new_ad)
    print(sum(ad.values()))

if __name__=="__main__":
    print(first_eff())