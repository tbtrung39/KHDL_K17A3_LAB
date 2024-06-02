Str="You are my sunshine,My only sunshine,You make me happy,When skies are gray,You'll never know, dear,How much I love you,Please don't take,My sunshine away"
n=input("Nhập từ muốn đếm: ")
if n in Str:
    print(f"Số từ có trong chuỗi là :{Str.count(n)}")
else:
    print("Không có từ bạn muốn đếm trong chuỗi")