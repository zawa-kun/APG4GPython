"""リスト内包表記の例"""
# # 例1 range(3)の要素それぞれに１を足す処理をする.->[1,2,3]
# l = [hoge+1 for hoge in range(3)]

# # 例2 1の要素それぞれに2倍する処理をする.-?[2,4,6]
# l2 = [2*i for i in l]

# # 例3 l2の要素それぞれに、「要素とそれからなるリストを作る」処理する. ->[[2,2],[4,4],[6,6]]
# l3 = [[val,val - 1] for val in l2]


"""組み込み関数に渡す"""
# l = [-3, -1, 1, 2]
# a = max(v*v for v in l)
# b = min(v*v for v in l)
# c = sum(v*v for v in l)
# print(a, b, c)

"""if文によるフィルタリング"""
l = [3, 1, 4, 5, 1]
l_only_even = [v for v in l if v%2 == 0]#偶数のみ
l_only_odd = [v for v in l if v%2 == 1]#奇数のみ
print(l_only_even)
print(l_only_odd)


