Str = input("Nhập chuỗi ký tự:")
a = ''.join(filter(str.isdigit, Str))
print("Chuỗi số sau khi loại bỏ các ký tự không phải số là:", a)
b = int(a)
k = 0
for i in range(1, b):
    if b % i == 0:
        k += i
if k == b:
    print("Đây là số hoàn hảo")
else:
    print("Đây không phải là số hoàn hảo")
    
