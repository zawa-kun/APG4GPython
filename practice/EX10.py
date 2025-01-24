N = int(input())
A = list(map(int,input().split()))
total = 0 #合計点.

#合計点計算.
for x in A:
    total += x

average = total//N

#平均との差を計算.
for x in A:
    if x-average < 0:
        print(average-x)
    else:
        print(x-average)

    