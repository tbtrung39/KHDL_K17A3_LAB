list=set()
while True:
    n=input("Nhap dau vao ( Nhap ESC de thoat) ")
    if not n.isnumeric():
        list.add(n)
    else:
        list.remove(n)
    if n.upper()=="ESC":
        break
list.remove("ESC")
print(list)