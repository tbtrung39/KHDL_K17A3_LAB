
# ax^2 + bx +c = 0
# delta = b^2 - 4*a*c

# if....else // elif (else if)

a = int(input("nhập vào a:"))
b = int(input("nhập vào b:"))
c = int(input("nhập vào c:"))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + delta**0.5)/2
    x2 = (-b - delta**0.5)/2
    print("phương trình có 2 nghiệm nphaan biệt")
elif delta == 0:
    print("phương trình có 1 nghiệm kép")
else:
    print("phương trình vô nghiệm")


True
False
a > 0 : lớn hơn 0
a < 0 : nhỏ hơn 0
a == 0 : bằng 0
a >= 0 : lớn hơn hoặc = 0
a <= 0 : nhỏ hơn hoặc = 0
a != 0 : khác 0
# not True
print(1 not in [1,2,3])
# and
a < 0 and a > 10     # xét a thuộc(0,10)
# or
a < -1 or a > 3         # xét a thuộc (-vc,-1) hợp (3,+vc)
# xét a thuộc (3,5) hơp (7,10)
(a > 3 and a < 5)or(a > 7 and a < 10)


# VÍ DỤ :
if a > 0 :
     print("chạy chương trình")

#c2
if a > 0:
    print("chạy chương trình a > 0")
else:
    print("chạy trương tình a <= 0")

#c3:
if a > 0:
    print("chạy chương trình a > 0")
if a <= 0:
    print("chạy trương tình a <= 0")
#c4:
if delta > 0:
    print("chạy chương trình delta > 0")
elif delta == 0:
    print("chạy chương trình delta == 0")
elif delta == 1:
    print("chạy chương trình delta == 1")
elif delta < 10:                                     # viết elif bỏ else thì chương trình vẫn chạy
    print("chạy chương trình delta < 10")
else:
    print("chạy chương trình delta < 0")

print("chương trình khác")










# lùi dòng là 1 chương trình riêng biệt nên có thể viết thêm hàm , biến ... vào để tính toán
# ví dụ :
if a > 0:
    print("chạy chương trình a > 0")
    a = 10
    a = a + 1
    if a > 0:
        print(" chạy trương trình")
        if == 10:
            print(" chạy chương trình")
    print(" chạy chương trình")