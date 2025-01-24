date = [int(c) for c in input().split()]
result = "NO"

for i in range(len(date)-1):
    a_value = date[i]
    b_value = date[i+1]

    if a_value == b_value:
        result = "YES"
        break

print(result)

