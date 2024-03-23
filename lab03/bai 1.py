
n=int(input("Nhập vào n: "))
result=1
term=0
for i in range(1,n+1):
    term*=(2*i)/(2*i+1)
    result+=term
print("Kết quả của phép toán là:", round(result, 3))
