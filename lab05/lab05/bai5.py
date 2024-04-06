str = input("Nhập chuỗi ký tự: ")
digits = ""
for char in str:
    if char.isdigit():
        digits += char

num = int(digits)
sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

so_hoan_hao = sum_divisors == num
if so_hoan_hao:
    print("Chuỗi số này là số hoàn hảo.")
else:
    print("Chuỗi số này không phải là số hoàn hảo.")
print("Chuỗi số sau khi loại bỏ ký tự không phải số:", digits)