#いろいろなfor文.

#0以上5未満をループ.
# for i in range(5):
#     print(i)

#2以上5未満をループ.
# for i in range(2,5):
#     print(i)

#2以上10未満を2刻みでループ
# for i in range(2, 10, 2):
#     print(i)

"""リストのリスト"""
# L = [[4,5],[6,7],[8,10]]
# for a,b in L:
#     print("aは",a,"bは",b,"です")  

"""複数のリストを同時にループ処理したい場合：zip関数"""
# a = [1,2,3]
# b = [4,5,6]

# for x,y in zip(a,b):
#     print(x,y)


"""continue文 その後の処理を飛ばす"""
for i in range(5):
    if i == 2:
        continue
    print(i)
