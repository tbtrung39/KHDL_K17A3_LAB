A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")
ket_qua = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        A1 = A[:i] + '+' + A[i:]
        B1 = B[:j] + '+' + B[j:]
        C, D = A1.split('+')
        E, F = B1.split('+')
        if int(C) + int(D) == int(E) + int(F):
            print(A1, '=', B1)
            ket_qua = True

if not ket_qua:
    print("Không tồn tại cách đặt!")
