A = set()
B = set()
end = 'ESC'
while True:
    a = input("Nhập kí tự của A: ")
    b = input("Nhập kí tự của B: ")
    if a and b == end:
        break
    A.add(a)
    B.add(b)
print(A,B)
ptu_chung = A.intersection(B)
print(ptu_chung)