import string

def first():
    inp = open('5.txt').read().split('\n')

    a  =[x.split(' -> ') for x in inp]
    points = [[list(map(int, x.split(','))) for x in y] for y in a]


    mx = 0
    my = 0

    mx_g = max(points, key=lambda x:max(x[0][0], x[1][0]))
    mx = max(mx_g[0][0], mx_g[1][0])
    my_g = max(points, key=lambda x:max(x[0][1], x[1][1]))
    my = max(my_g[0][1], my_g[1][1])

    print(mx, my)

    def draw_board(points):
        board = [['.' for _ in range(mx+1)] for _ in range(my+1)]
        for sp, ep in points:
            def draw_line(sp, ep, board):
                x1, y1 = sp
                x2, y2 = ep

                if x1==x2 or y1==y2:
                    if board[y1][x1] == '.':
                        board[y1][x1] = 1
                    else:
                        board[y1][x1]+=1

                    if x1==x2 and y1==y2:
                        return board

                    if x1==x2:
                        x1 = x1
                    else:
                        x1= x1+1 if x1<x2 else x1-1
                    
                    if y1==y2:
                        y1=y1
                    else:
                        y1 = y1+1 if y1<y2 else y1-1

                    sp = [x1, y1] 
                    return draw_line(sp, ep, board)
                return board

            board = draw_line(sp, ep, board)

        return board
    
    board = draw_board(points)
    count=0
    for x in board:
        for y in x:
            try:
                if int(y)>=2:
                    count+=1
            except ValueError:
                continue

    return count



def second():
    inp = open('5.txt').read().split('\n')

    a  =[x.split(' -> ') for x in inp]
    points = [[list(map(int, x.split(','))) for x in y] for y in a]


    mx = 0
    my = 0

    mx_g = max(points, key=lambda x:max(x[0][0], x[1][0]))
    mx = max(mx_g[0][0], mx_g[1][0])
    my_g = max(points, key=lambda x:max(x[0][1], x[1][1]))
    my = max(my_g[0][1], my_g[1][1])

    print(mx, my)

    def draw_board(points):
        board = [['.' for _ in range(mx+1)] for _ in range(my+1)]
        for sp, ep in points:
            def draw_line(sp, ep, board):
                x1, y1 = sp
                x2, y2 = ep

                if board[y1][x1] == '.':
                    board[y1][x1] = 1
                else:
                    board[y1][x1]+=1

                if x1==x2 and y1==y2:
                    return board

                if x1==x2:
                    x1 = x1
                else:
                    x1= x1+1 if x1<x2 else x1-1
                
                if y1==y2:
                    y1=y1
                else:
                    y1 = y1+1 if y1<y2 else y1-1

                sp = [x1, y1] 
                return draw_line(sp, ep, board)

            board = draw_line(sp, ep, board)

        return board
    
    board = draw_board(points)
    count=0
    for x in board:
        for y in x:
            try:
                if int(y)>=2:
                    count+=1
            except ValueError:
                continue

    return count

if __name__=="__main__":
    print(second())