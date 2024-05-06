A=set()
tong = 0 
while True:
    n=input("Nhap dau vao la so thuc (Nhan N de thoat)")
    if n.isnumeric():
     A.add(n)
     tong+=int(n)
    elif n.upper()=="N":
        break
q=max(A)
r=min(A)
print(q,r,tong)