#入力：リストa
#出力：aを昇順にしたリスト

def quick_sort(a):
    #ベースケース
    if len(a) == 0:
        return []
    # aから要素を１つ取り出してpとする
    p = a.pop()

    #aからp未満の要素を集めたリストをlo,p以上を集めたリストをhiとする　
    lo = []
    hi = []
    for x in a:
        if x < p:
            lo.append(x)
        else:
            hi.append(x)
    
    #再帰呼び出し：loとhiをソートする
    lo = quick_sort(lo)
    hi = quick_sort(hi)

    #答えの計算：loとpとhiをこの順に並べたものがaの昇順ソートである。
    return lo + [p] + hi


a = list(map(int,input().split()))
print(quick_sort(a))