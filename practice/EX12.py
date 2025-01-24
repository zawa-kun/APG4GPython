N = int(input())#生徒数.
T = list(map(int,input().split())) #各生徒のゴール時間

min_value = min(T) #最小値を求める.
fastest_student_index = 0

for i,v in enumerate(T):
    if v == min_value:
        fastest_student_index = i+1

print(fastest_student_index)