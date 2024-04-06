a = input("Nhập một ký tự: ")
while len(a) != 1:
    print("Vui lòng chỉ nhập một ký tự.")
    a = input("Nhập lại một ký tự: ")
ascii = ord(a)
print("Giá trị ASCII của ký tự", a, "là:", ascii)
