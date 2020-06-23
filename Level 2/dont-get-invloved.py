def solution(src, dest):

    count = []
    for i in range(15):
        li = []
        
        if i==0 or i==14:
            li = [6,5,4,5,4,5,4,5,4,5,4,5,4,5,6]
        
        if i==1 or i==13:
            li = [5,4,5,4,3,4,3,4,3,4,3,4,5,4,5]
                    
        if i==2 or i==12:
            li = [4,5,4,3,4,3,4,3,4,3,4,3,4,5,4]
    
        if i==3 or i==11:
            li = [5,4,3,4,3,2,3,2,3,2,3,4,3,4,5]
            
        if i==4 or i==10:
            li = [4,3,4,3,2,3,2,3,2,3,2,3,4,3,4]
            
        if i==5 or i==9:
            li = [5,4,3,2,3,4,1,2,1,4,3,2,3,4,5]
            
        if i==6 or i==8:
            li = [4,3,4,3,2,1,2,3,2,1,2,3,4,3,4]
            
        if i==7:
            li = [5,4,3,2,3,2,3,0,3,2,3,2,3,4,5]
        count.append(li)
        
    chessBoard , k = [], 0
    for i in range(8):
        li = [j for j in range(k, k+8)]
        k+=8
        chessBoard.append(li)

    cnt1 = [x for x in chessBoard if src in x][0]
    cnt2 = [y for y in chessBoard if dest in y][0]

    dist_x = 7 + (chessBoard.index(cnt2) - chessBoard.index(cnt1))
    dist_y = 7 + (cnt2.index(dest) - cnt1.index(src))

    return count[dist_x][dist_y]
    