n=int(input("Nhập vào một số nguyên dương: "))
S=0
while n>0:
    i=n%10
    S+=i
    n//=10
print(f"Tổng các chữ số đã nhập là: {S}")
