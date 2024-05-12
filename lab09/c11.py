def double_factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        result = 0
        for i in range(n):
            result += double_factorial(i-2) * i
        return result

n = int(input("Nhập số n: "))
print(double_factorial(n), "là kết quả của tổng giai thừa kép")