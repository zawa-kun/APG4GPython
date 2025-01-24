S = input()
total = 1

for i in range(len(S)):
    if S[i] == "1":
        int(S[i])
    
    if S[i] == "+":
        total += 1
    elif S[i] == "-":
        total -= 1
print(total)
