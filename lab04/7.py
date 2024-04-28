
n = int(input("Nhập giá trị n: "))
while n <= 0:
    n = int(input("Giá trị không hợp lệ. Nhập lại n (n > 0): "))
S6 = 0
i = 2
while i <= 2 * n:
    S6 += i ** 4  
    i += 2  
print(f"S6 = {S6}")
