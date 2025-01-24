S = input().strip()

result = 1
calculation = list(S[1::2])
print(calculation)
for i in range(len(calculation)):
    x = calculation.pop(0)
    if x == "+":
        result += 1
    elif x == "-":
        result -= 1

print(result)

"""
なぜ下記のロジックだと動かないのか？

原因: 
for x in calculation:
    処理
    calculation.pop(0)

for文のループが元のリストの長さで動くのに対し、pop()でリストが短くなるため、
一部の要素がスキップされるから。
"""

# for x in calculation:
#     if x == "+":
#         result += 1
#     elif x == "-":
#         result -= 1
#     calculation.pop(0)

# print(result)e
