

def first():
    a = open('1.txt').read()

    a = list(map(int, a.split('\n')))
    count=0
    for i,j in enumerate(a[1:],1):
        if a[i]>a[i-1]:
            count+=1
    print(count)


def second():
    a = open('1_test.txt').read()

    a = list(map(int, a.split('\n')))
    count=0
    for i, j in enumerate(a[1:-2], 1):
        fa = sum(a[i:i+3])
        fb = sum(a[i-1:(i-1)+3])
        print(fa, fb, i, a[i:i+3], a[i-1:(i-1)+3])
        if fa>fb:
            count+=1
    
    return count


if __name__=="__main__":
    print(second())
