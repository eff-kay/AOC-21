
inp = open('2.txt').read().split("\n")

def first():
    c = {'h':0, 'd':0}

    for i,j in enumerate(inp):
        act, step = j.split(' ')

        step = int(step)

        if act=='forward':
            c['h']+=step
        elif act=='up':
            c['d']-=step
        elif act=='down':
            c['d']+=step

    return c['h']*c['d']


def second():
    c = {'h':0, 'a':0, 'd':0}

    for i,j in enumerate(inp):
        act, step = j.split(' ')

        step = int(step)

        if act=='forward':
            c['h']+=step
            c['d']+= c['a']*step
        elif act=='up':
            c['a']-=step
        elif act=='down':
            c['a']+=step

    print(c)
    return c['h']*c['d']


if __name__=="__main__":
    print(second())
