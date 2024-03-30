# Nhập chuỗi từ bàn phím
input_str = input("Nhập chuỗi ký tự Str: ")

max_length = 0  # Độ dài cực đại của chuỗi con
max_substring = ""  # Chuỗi con có độ dài cực đại

current_char = ""  # Ký tự hiện tại đang xét
current_length = 0  # Độ dài hiện tại của chuỗi con

# Duyệt qua từng ký tự trong chuỗi
for char in input_str:
    # Nếu ký tự hiện tại trùng với ký tự trước đó
    if char == current_char:
        current_length += 1  # Tăng độ dài của chuỗi con
    else:
        current_char = char  # Cập nhật ký tự hiện tại
        current_length = 1  # Reset độ dài của chuỗi con
        
    # Nếu độ dài của chuỗi con hiện tại lớn hơn độ dài cực đại
    if current_length > max_length:
        max_length = current_length  # Cập nhật độ dài cực đại
        max_substring = current_char * max_length  # Cập nhật chuỗi con cực đại

# In ra chuỗi con cực đại
print("Chuỗi con có độ dài cực đại và chỉ chứa các ký tự giống nhau:", max_substring)
