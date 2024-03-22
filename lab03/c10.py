n = int(input("Nhập số nguyên tố: "))
if n <=1:
    print("Vui lòng nhập lại số có nhiều hơn 2 ước")
else:
    for i in range(1,n):
        if n % i ==0:
print("Dạng phân tích thừa số của số đó là: ", i, "*", i+1)
