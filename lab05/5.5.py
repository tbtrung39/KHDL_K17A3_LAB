input_str = input("Nhập chuỗi ký tự: ")

number_str = ''.join(filter(str.isdigit, input_str))

print("Chuỗi số sau khi loại bỏ ký tự không phải số:", number_str)

number = int(number_str)
sum_divisors = sum([i for i in range(1, number) if number % i == 0])

if sum_divisors == number:
    print("Chuỗi số", number, "là một số hoàn hảo.")
else:
    print("Chuỗi số", number, "không phải là một số hoàn hảo.")