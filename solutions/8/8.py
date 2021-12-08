
from typing import DefaultDict
from collections import defaultdict


def first():
    inp = open('8_test.txt').read()
    inp = inp.split('\n')
    inp = [y.split('|') for y in inp]

    count=0
    for x in inp:
        y = x[1].split(' ')
        for z in y:
            if len(z) in (2, 3,4,7):
                count+=1

    return count

def second():
    inp = open('8.txt').read()
    inp = inp.split('\n')
    # inp = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'''
    # inp = [inp]
    inp = [y.split('|') for y in inp]

    # print(inp)
    count=0
    df = {}

    def get_lights(df):
        new_df = defaultdict(str)
        for k in df:
            # these has to happen first
            if k==2:
                new_df[1] = df[k]
            elif k==3:
                new_df[7] = df[k]
            elif k==4:
                new_df[4] = df[k]
            elif k==7:
                new_df[8] = df[k]
        
        for k in df:
            if k==5:
                for v in df[k]:
                    check_2 = set(new_df[4]).union(set(v)) == set(new_df[8])# we need to calculate this last
                    if check_2:
                        new_df[2] = v
                    elif all([x in v for x in new_df[1]]):
                        new_df[3]= v
                    else:
                        new_df[5] = v 
            elif k==6:
                for v in df[k]:
                    comb  = set(new_df[4]).union(set(new_df[7]))
                    if len(set(v)-comb)==1:
                        new_df[9] = v
                    elif all([x in v for x in new_df[1]]):
                        new_df[0] = v
                    else:
                        new_df[6] = v
        return {''.join(sorted(v)):k for k,v in new_df.items()}

    totals = []
    for x in inp:
        y = x[0].split(' ')
        df={}
        for z in y:
            if len(z)==2:
                df[2] = z
            elif len(z)==3:
                df[3] = z
            elif len(z)==4:
                df[4] = z
            elif len(z)==7:
                df[7] = z
            elif len(z)==5 and len(df.get(5, []))<3:
                if 5 in df:
                    df[5].append(z)
                else:
                    df[5] = [z]
            elif len(z) == 6 and len(df.get(6, []))<3:
                if 6 in df:
                    df[6].append(z)
                else:
                    df[6] = [z]

            if sorted(list(df.keys()))==[2,3,5,6,7,8] and len(df[5])==3 and len(df[6])==3:
                break

        dec = get_lights(df)

        y = x[1].strip().split(' ')
        total=''
        for word in y:
            total+=str(dec[''.join(sorted(word))])

        totals.append(int(total))
        print(totals)

    return sum(totals)      
if __name__=="__main__":
    print(second())