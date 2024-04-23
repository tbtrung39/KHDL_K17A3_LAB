A = input("Nhập các kí tự:")
gia_tri_A = A.split(",")
set_A = set(A)
B = input("Nhập các kí tự:")
gia_tri_B = B.split(",")
set_B = set(B)
phan_tu_chung = set_A.intersection(set_B)

print(phan_tu_chung)