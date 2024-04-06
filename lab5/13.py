A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")
n = len(A)
m = len(B)
f = False
for i in range(1, n):
    for j in range(1, m):
        C, D = A[:i], A[i:]
        E, F = B[:j], B[j:]
        if int(C) + int(D) == int(E) + int(F):
            print(C + '+' + D + '=' + E + '+' + F)
            f= True
            break
    if f:
        break
if not f:
    print("Không tồn tại cách đặt!")
