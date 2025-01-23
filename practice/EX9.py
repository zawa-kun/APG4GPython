N=int(input())
A=int(input())
result = A

for i in range(N):
    op, B = input().split()
    B = int(B)

    if op == "+":
        result += B
    elif op == "-":
        result -= B
    elif op == "*":
        result *= B
    elif op == "/" and B != 0:
        result //= B
    else:
        print("error")
        break
    
    print(i+1, result)
    