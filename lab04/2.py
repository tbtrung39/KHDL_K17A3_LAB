n=int(input("Nhập vào một giá trị n: "))
S=0
i=1
while i<=n:
    if i%2==0:
        S-=1/i 
    else:
        S+=1/i 
    i+=1
print(f"Tổng của chuỗi là: {S}")

S=0
i=1
while i<n:
    S+=1/(i*(i+1))
    i+=1
print(f"Tổng của chuỗi là: {S}")

S=0
i=1
while i <= n:
    S+= 1/(i**0.5)
    i+=1
print(f"Tổng của chuỗi là: {S}")