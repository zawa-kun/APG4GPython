N = int(input()) #組織数

#p[i]：組織iの親組織
#[-1]:インデックスと親番号を合わせるため.p[1]から親番号を取得できるようになる.
p = [-1] + list(map(int,input().split()))

# 2次元配列 children
#childeren[i]:組織iの子組織の一覧であるような2次元配列.
children = [[]for _ in range(N)] #最大数は組織数分
for i in range(1,N):
    children[p[i]].append(i)
print(children)

# 再帰関数 complete_time
# 入力 : 組織番号 x
# 出力 : 組織 x に子組織からの報告書が揃った時刻（報告書を親組織へ送った時刻）
def complete_time(x):
    #ベースケース：子組織が存在しない場合、答えは0
    if len(p[i]) == 0:
        return 0
    
    #個組織が存在する場合、答えは「個組織から報告書が届く時刻」の最大値.
    return max(complete_time(y)+1 for y in children[x])

# 組織 0 の元に報告書が揃う時刻を出力
print(complete_time(0))