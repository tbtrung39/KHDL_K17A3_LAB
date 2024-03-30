Str1 = "Khoa, khoa hoc ung dung"

# Phân tách chuỗi thành các từ
words = Str1.split(' ')  # Phân tách dựa trên khoảng trắng
words = [word.strip(',') for word in words]  # Loại bỏ dấu phẩy ở đầu và cuối từ

# In ra các từ
for word in words:
    print(word)