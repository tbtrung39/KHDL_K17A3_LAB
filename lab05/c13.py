A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

# Chèn dấu * vào giữa các chữ số của A và B
A_new = ""
B_new = ""
for i in range(len(A)):
    A_new += A[i]
    if i < len(A) - 1:
        A_new += "*"
for i in range(len(B)):
    B_new += B[i]
    if i < len(B) - 1:
        B_new += "*"
found = False
for i in range(1, len(A_new), 2):
    for j in range(1, len(B_new), 2):
        expr1 = eval(A_new[:i] + "+" + A_new[i+1:])
        expr2 = eval(B_new[:j] + "+" + B_new[j+1:])
        if expr1 == expr2:
            print(A_new[:i] + "=" + B_new[:j])
            found = True
            break
    if found:
        break

if not found:
    print("Không tồn tại cách đặt!")