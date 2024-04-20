number=[]
while True:
    n=input("nhap gia tri:")
    if n == "esc":
        break
    number.append(n)
a=set(number)
print(a)