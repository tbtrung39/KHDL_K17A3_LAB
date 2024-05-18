numbers = set()
A=set()
while True:
 n = input("Nhap dau vao (Nhan N de thoat)")
 if n.isnumeric():
     numbers.add(n)
 elif n.upper()=="N":
       break
print(numbers)
print(A.union(numbers))