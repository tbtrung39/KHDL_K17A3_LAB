input_str = input("Nhập chuỗi ký tự: ")
n = ''.join(c for c in input_str if c.isdigit())
print("Chuỗi số sau khi loại bỏ các ký tự không phải số:", n)
so = int(n)
a = sum(int(digit) for digit in str(so))
so_hoan_hao = a == so
if so_hoan_hao:
    print(f"{so} là một số hoàn hảo.")
else:
    print(f"{so} không phải là số hoàn hảo.")
