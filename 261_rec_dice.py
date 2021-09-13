# 261_rec_dice.py

N=3
M=15
a=[0]*N

def dice(round, tot):
    if round==N:
        if tot==M:
            print(a)
        return

    for i in range(1,7):
        a[round]=i
        dice(round+1, tot+i)

dice(0, 0) # 1번째 라운드, 현재까지 합은 0이다.