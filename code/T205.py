"""
再帰関数
再帰関数は３つの部分に分けられる
1.ベースケース ex) if n==0 によるフィルタリング
2.再帰呼び出し ex) s = func(n-1)
3.答えの計算
"""
#0からnまでの総和を求める.
def sum_triangle(n):
    #0から0までの総和は0.
    if n == 0:
        return 0

    s = sum_triangle(n - 1) #自信を呼び出して0からnまでのn-1までの総和を求める.
    return(s + n) # nを足して0からnまでの総和を求める.

"""再帰呼び出しの例"""
#入力：０以上の整数ｎ
#出力: nの階上
def factorial(n):
    if n==0:
        return 0
    s = factorial(n-1)
    return(n*s)

#入力：０以上の整数ｎ
#出力：fib(0) = 1, fib(1) = 1, fib (n) = (n-1) + (n-2)で定められた数列のn項目を返す.
def fib(n):
    #ベースケース：fib(0) = 1, fib(1) = 1
    if n == 0 or n == 1:
        return 1
    #再帰呼び出し:(n-1)と(n-2)を計算.
    f1 = fib(n-1)
    f2 = fib(n-2)

    #答えの計算:fib(n)を計算.
    return f1 + f2


