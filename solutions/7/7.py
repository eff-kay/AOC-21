
from statistics import median,mean

def first():
    inp = open('7.txt').read().split(',')
    inp = list(map(int, inp))
    med = median(sorted(inp))
    total=0
    for x in inp:
        diff = abs(x-med)
        total+=diff

    return total


def second():
    inp = open('7.txt').read().split(',')
    inp = list(map(int, inp))
    total=[]
    for n in range(min(inp), max(inp)):
        diffs=[]
        for j in range(len(inp)):
            diff = abs(inp[j] - n)
            diff = (diff**2+diff)/2
            diffs.append(diff)
        total.append(sum(diffs))

    total = min(total)

    return total



if __name__=="__main__":
    print(second())