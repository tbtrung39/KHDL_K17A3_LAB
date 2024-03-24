n= int(input('Nhap mot so nguyen duong: '))
print("Các số nguyên tố bé hơn hoặc bằng", n, "là:")

for j in range(2, n+1):
    nguyen_to=True
    for i in range(2, int(j**0.5)+1):
        if j % i == 0:
          nguyen_to = False
        break
    if nguyen_to:
        print(j, end= "")

