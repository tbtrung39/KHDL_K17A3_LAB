A=input("Nhập chuỗi ký tự A: ")
B=input("Nhập chuỗi ký tự B: ")
for i in range(1, len(A)):
    for j in range(1, len(B)):
        C, D = A[:i]+'t'+A[i:], B[:j]+'t'+B[j:]
        if int(C[:i+1])+int(D[:j+1])==int(C[i+1:])+int(D[j+1:]):
            print(f"{c[:i+1]}+{D[:j+1]}={C[i+1:]}+{D[j+1:]}")
            exit()
print("Không tồn tại cách đặt")