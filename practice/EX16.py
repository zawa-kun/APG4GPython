N, K = map(int,input().split())

# input().split()はその文字列を空白で区切ってリストにする.
S = input().split()
result = [word for word in S if len(word) >= K]

#空白区切りで出力.
print(*result)
