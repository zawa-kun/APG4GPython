"""5個の0が入ったリストの作成"""
# N = 5
# list_a = [0]*N

"""配列の要素を順番に出力"""
# a = [3, 1, 4, 5]
# print(a[0])
# print(a[1])
# a[2]=7

# for x in a:
#     print(x)

"""リストを作成する"""
# a = [] # 空のリスト作成.
# a = [3,1,4,1,5]

# a = ["Hello","Atcoder", 123, 4.5, []] #様々な型を持つデータを人るのリストに入れられる.

"""リスト[0, 1, 2, 3, 4]を作る"""
# a = list(range(5))

"""リストを作る"""
# a = list(range(5))

# #aの長さを出力
# print(len(a))

# #aの２番目の要素を7に変更する.
# a[2] = 7

# #len(a)とすると,配列aの添え字順に列挙できる.
# for i in range(len(a)):
#     #a[i]でaのi番目の要素を取得する.
#     print(i, ":", a[i])


"""リストの内容列挙"""
# a = list(range(5))

# for x in a:
#     print(x)

"""入力からリストを作る"""
# a = list(map(int, input().split()))

# for x in a:
#     print(a)

"""リストの出力別バージョン"""
# a = [9,9,7,3]
# #aの値を空白区切りを出力する.
# print(*a)

# #aの要素を改行区切りで出力する.
# for x in a:
#     print(x)

"""例題 数学と英語の点数の各生徒と合計を求める"""
# N = int(input()) #生徒数
# M=list(map(int,input().split()))
# E=list(map(int,input().split()))

# for i in range(N):
#     total = M[i] + E[i]
#     print(total)

"""負の添え字 範囲外アクセス"""
# a = [3, 1, 4, 1, 5]

# print(a[-1])
# print(a[-2])
# print(a[-3])
# #aの5番目存在しないので、実行時エラーが発生する.
# print(a[5])

"""リストの末尾に要素を追加・削除"""
# a = []
# #[1,2,3]の作成.
# a.append(1)
# a.append(2)
# a.append(3)

# #末尾を出力し、削除.
# print(a.pop())

# #a配列の1の位置に10を入れる.
# a.insert(1,10)
# print(a)

#xが配列の中にあるかを判定する.
# x = 2
# print(x in [1,2,3])


# a = [3, 1, 4, 1,5]
# #aの中に存在する１の数を数える.
# print(a.count(1))
# #aの中に存在する最初の1の位置を調べる.
# print(a.index(1))

# #aを昇順で並び替える.
# a.sort()
# print(a)
# #リストの反転.
# a.reverse()
# print(a)

"""リストを複製する よくある間違いバージョン"""
# a = [3,1,4,1,5]
# #aがさしているリストをbに代入する.
# b = a

# #aの指しているリストとbの指すリストは同一のため,aを変更するとbも変わる.
# a[2] = 7
# print(b)
# #逆に、bを変更するトaも変わる
# b.append(9)
# print(a)


"""リストの複製 正答"""
a = [3,1,4,1,5]
b = []

for i in range(len(a)):
    b.append(a[i])

print(b)

"""ちなみにfor文を使って1個ずつ挿入しなくてもcopy()で複製できる"""
a = [3,1,4,1,5]
b = a.copy()
print(b)