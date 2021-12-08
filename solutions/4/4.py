

def first():
    inp = open('4.txt').read().split('\n')
    
    dr = inp[0].split(',')

    print(dr)
    table = [x.strip().split(' ') for x in inp[2:] if x!='']
    table = [[y for y in x if y!=''] for x in table]

    tables = [table[i:i+5] for i in range(0, len(table), 5)]

    def mark_board(board, n):
        for i,x in enumerate(board):
            for j, y in enumerate(x):
                if y==n:
                    board[i][j]='x'
        return board

    def check_win(board):
        for i,x in enumerate(board):
            countx = x.count('x')
            if countx == 5:
                return True
        
        for i,x in enumerate(zip(*board)):
            countx = x.count('x')
            if countx  == 5:
                return True

        return False

    bi= -1
    dri=-1
    status = False
    for ni, n in enumerate(dr):
        if not status:
            for i, table in enumerate(tables):
                table = mark_board(table, str(n))
                tables[i] = table
                # print(i, n)
                # print(table)
                status =check_win(table)

                if status:
                    bi=i
                    dri = ni
                    break
    
    # sum
    usum = 0
    for i, x in enumerate(tables[bi]):
        x = [int(y) for y in x if y!='x']
        usum+= sum(x)
    
    nu = int(dr[dri])
    return nu*usum

def second():
    inp = open('4.txt').read().split('\n')
    dr = inp[0].split(',')
    table = [x.strip().split(' ') for x in inp[2:] if x!='']
    table = [[y for y in x if y!=''] for x in table]

    tables = [table[i:i+5] for i in range(0, len(table), 5)]
    all_t= len(tables)

    def mark_board(board, n):
        for i,x in enumerate(board):
            for j, y in enumerate(x):
                if y==n:
                    board[i][j]='x'
        return board

    def check_win(board):
        for i,x in enumerate(board):
            countx = x.count('x')
            if countx == 5:
                return True
        
        for i,x in enumerate(zip(*board)):
            countx = x.count('x')
            if countx  == 5:
                return True

        return False

    bi= -1
    dri=-1
    status = False
    win_t = []
    for ni, n in enumerate(dr):
        if not status:
            for i, table in enumerate(tables):
                if table!='win':
                    table = mark_board(table, str(n))
                    tables[i] = table

                    # print(i, n)
                    # print(table)
                    win = check_win(table)

                    if win:
                        win_t.append(i)
                        temp_t = [x for x in tables if x!='win']
                        print(temp_t, len(tables))
                        if len(temp_t)==1:
                            status = True
                            bi=i
                            dri = ni
                            break
                        else:
                            tables[i] = 'win'
                    

    
    # sum
    usum = 0
    print(tables)
    for i, x in enumerate(tables[bi]):
        x = [int(y) for y in x if y!='x']
        usum+= sum(x)
    
    nu = int(dr[dri])
    print(bi, nu, usum)
    return nu*usum

if __name__=="__main__":
    print(second())