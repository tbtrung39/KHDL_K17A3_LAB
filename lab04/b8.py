n = input("Nhập một ký tự: ")
if len(n) != 1:
    print("Vui lòng chỉ nhập một ký tự.")
else:
    gia_tri_ascii = ord(n)
    print("Giá trị ASCII của ký tự '{}' là: {}".format(n, gia_tri_ascii))

