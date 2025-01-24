#組み込み関数.

"""
abs(x):xの絶対値を返す
"""
# abs(-1) #1

"""
pow(x,y):xのy乗を返す
※**よりも高速!!!
pow(x,y,mod):xのy乗をmodで割った余りを返す
"""
# pow(2,3) #8
# pow(2,3,5) #3

"""
min:最大値
max:最小値
"""
# min_val = min(1,2,3,4,5)
# max_val = max(1,2,3,4,5)

# print(min_val, max_val)


"""
sum:合計値
"""
# a_list = [1,2,3,4,5]
# sum_val = sum(a_list)
# # print(sum_val)



"""
sorted:ソートし、新たなリストを返す
※元のリストは変更されない
"""
# n_list = [2,6,45,7,4]
# sorted_list = sorted(n_list)
# print(sorted_list)

"""
all:全ての要素がTrueの場合Trueを返す
any:いずれかの要素がTrueの場合Trueを返す
"""
# a_list = [1,3,-5,6]
# all_res = all([v>0 for v in a_list])
# any_res = any([v<0 for v in a_list])
# print(all_res, any_res)


"""
enumrate:インデックスと要素を取得する
"""
e_list=[1,4,6,8]

for i,v in enumerate(e_list):
    print(i,"番目の要素は", v,"です")


