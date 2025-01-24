"""関数の定義"""
def print_numbers():
    print(1)
    print(2)
    print(3)

# print_numbers()

"""引数を二つ持つ関数"""
def add_and_print(a, b):
    print(a + b)

# add_and_print(10,20)

"""戻り値を持つ関数定義"""
def add_one(a):
    return a+1

# two = add_one(1)
# print(two)
# print(add_one(2)+add_one(4))

"""関数定義時のテクニック"""
"""return文の特性と複数のreturn文を持つ関数"""
def my_min(a, b):
    if a < b:
        return a
    else:
        return b
# print(my_min(10,20))

def wrong_function(a):
    return a+1
    print("この行は実行されない")
    return a+2 #この行も実行されない

# print(wrong_function(110))
"""returnの性質を利用し、my_min関数を簡潔に書く"""
def my_min_improve(a,b):
    if a < b:
        return a
    return b

# print(my_min_improve(10,20))

"""値の返さない関数でもreturnを用いて関数を早期終了する"""
def print_a_is_7(a):
    if a == 7:
        print("a is 7")
        return
    #a==7のケースではreturnで関数が終了するため、ここには到達しない
    print("a is not 7")

# print_a_is_7(7)

"""
関数内の変数のスコープ
・関数内の変数は基本敵に関数内でのみ有効
"""
def verify_scope():
    x = 1
    print("関数内:",x)

# x = 7
# verify_scope()
# print("関数外:",x)

"""関数外の変数を変更する（グローバル変数へのアクセス）"""
a =0
def increment():
    global a #globalをつけることで、関数内でグローバル変数を変更できる 
    a += 1
    return

# increment()
# print(a)

"""リストは変更できるが、代入はグローバル出ないと出来ない"""
li=[]
def func():
    print(li)
    li.append(1)
    return

func()
print(li)
