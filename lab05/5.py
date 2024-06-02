input_str = input("Nhập chuỗi: ")

# Xóa hết những kí tự không phải số
num_str = ''.join(ch for ch in input_str if ch.isdigit())

# Kiểm tra số thu được có phải là số hoàn hảo không
num = int(num_str)
sum = 1
i = 2
while i * i <= num:
    if num % i:
        i += 1
    else:
        if i * (num // i) == num:
            sum = sum + i + num//i
        else:
            sum = sum + i
        i += 1

if sum == num and num!=1:
    print(num_str, "là số hoàn hảo.")
else:
    print(num_str, "không phải là số hoàn hảo.")
