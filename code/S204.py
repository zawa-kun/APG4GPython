"""
多次元配列
数値を要素に持つリストを持つリストのこと.
a[x][y]で出力できる
"""
# a = [[1, 3, 5],[2, 4, 6]]

# print(a[1])
# print(a[1][2])

# #２重ループで取り出してみる.
# for i in range(len(a)):
#     print(f"リストの第{i}成分は{a[i]}です")
#     for j in range(len(a[i])):
#         print(f"リストの第({i},{j})成分は{a[i][j]}です")

# #同じことをする、違う書き方.
# for item in a:
#     print(item)
#     for val in item:
#         print(val)


"""二次元配列を入力から取得する１"""
# N, M = list(map(int, input().split()))
# a = []
# for i in range(N):
#     a.append(list(map(int,input().split())))


"""二次元配列を入力から取得する2"""
# N, M = list(map(int, input().split()))
# a = [None]*N
# for i in range(N):
#     a[i] = list(map(int, input().split()))

"""二次元配列を入力から取得する3"""
# N, M = list(map(int, input().split()))
# a = [list(map(int, input().split())) for _ in range(N)]


"""要素が全て0の二次元配列を作る"""
N = 2 #行
M = 3 #列
a = [[0 for _ in range(M)] for _ in range(N)]
# a = [[0]*M for _ in range(N)] でも可.
print(a)

"""N×0の二次元配列を作る"""
N = 10
a = [[0] for _ in range(N)]
print(a)

"""
二次元配列の作成時の注意
・行数と列数をしないように注意.サイズN×Mを作る時、Nを最後.
"""
