a=set()
while True:
    n=input("Nhap gia tri")
    if n == "esc":
        break
    a.add(n)
ki_tu={"0","1","2","3","4","5","6","7","8","9"}
a-=ki_tu
print("tap hop la", a)