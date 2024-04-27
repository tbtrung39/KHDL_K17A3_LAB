user_name = input("Nhập tên của bạn: ")
print("Xin chào ", user_name)
pass_word = input("Nhập mật khẩu: ")
for char in pass_word:
    if char.isalpha() == False:
        print("Lỗi kí tự không nằm trong bảng chữ cái tiếng Anh")
    elif char.isnumeric() == False:
        print("Lỗi kí tự không có số hợp lệ")
    elif char != "$" or char != "#" or char != "@":
        print("Không có kí tự đặc biệt")
    elif len(pass_word) not in range(6,13):
        print("Độ dài mật khẩu không hợp lệ")
    else:
        print(pass_word)