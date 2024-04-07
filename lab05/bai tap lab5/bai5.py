
str = input("Nhập chuỗi ký tự: ")
digits = ""
for char in str:
    if char.isdigit():
        digits += char

so = int(digits)
sum_divisors = 0
for i in range(1, so):
    if so % i == 0:
        sum_divisors += i

so_hoan_hao = sum_divisors == so
if so_hoan_hao:
    print("Chuỗi số này là số hoàn hảo.")
else:
    print("Chuỗi số này không phải là số hoàn hảo.")
print("Chuỗi số sau khi loại bỏ ký tự không phải số:", digits)