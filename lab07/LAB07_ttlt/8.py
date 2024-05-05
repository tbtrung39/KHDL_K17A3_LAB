a = set()
while True:
    element = input("Nhap cac phan tu (Nhap de ket thuc): ")
    if element == '':
        break
    a.add(element)
so_nguyen = sum(n.isdigit() for n in a)
so_thuc = sum('.' in n and n.replace('.','',1).isdigit() for n in a)
str = len(a) - so_nguyen - so_thuc
print(f"")
    