"""多重ループ"""
A = [int(v) for v in input().split()]
B = [int(v) for v in input().split()]
result = False
finished=False

for a in range(len(A)):
    for b in range(len(B)):
        if A[a] == B[b]:
            result = True
            finished = True
            break
    if finished:
        break

if result:
    print("YES")
else:
    print("NO")