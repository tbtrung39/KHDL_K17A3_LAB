def Xn_recursive(n):
    if n ==0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += (n - i)**2 * Xn_recursive(i)
        return result
    
n = int(input("Nhập số n: "))
print(Xn_recursive(n), "là kết quả của công thức truy hồi Xn")