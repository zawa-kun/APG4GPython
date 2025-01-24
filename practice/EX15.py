N, S = map(int, input().split())

A = list(map(int, input().split()))
P = list(map(int, input().split()))

result = 0
for a in range(len(A)):
    for p in range(len(P)):
        if A[a] + P[p] == S:
            result += 1

print(result)  