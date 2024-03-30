# Nhập hai chuỗi từ bàn phím
str1 = input("Nhập chuỗi ký tự Str1: ")
str2 = input("Nhập chuỗi ký tự Str2: ")

# Khởi tạo ma trận để lưu độ dài của chuỗi con chung
# Độ dài của dãy con chung tại vị trí (i, j) sẽ được lưu tại dp[i][j]
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

max_length = 0  # Độ dài cực đại của chuỗi con chung
max_substring = ""  # Chuỗi con chung có độ dài cực đại

# Duyệt qua từng ký tự trong chuỗi Str1
for i in range(1, len(str1) + 1):
    # Duyệt qua từng ký tự trong chuỗi Str2
    for j in range(1, len(str2) + 1):
        # Nếu ký tự tại vị trí i trong Str1 giống ký tự tại vị trí j trong Str2
        if str1[i - 1] == str2[j - 1]:
            # Tăng độ dài của chuỗi con chung lên 1
            dp[i][j] = dp[i - 1][j - 1] + 1
            # Nếu độ dài của chuỗi con chung lớn hơn độ dài cực đại hiện tại
            if dp[i][j] > max_length:
                max_length = dp[i][j]  # Cập nhật độ dài cực đại
                max_substring = str1[i - max_length:i]  # Cập nhật chuỗi con chung cực đại
        else:
            dp[i][j] = 0  # Đặt độ dài của chuỗi con chung tại vị trí (i, j) bằng 0

# In ra chuỗi con chung cực đại
print("Chuỗi con chung có độ dài cực đại của Str1 và Str2:", max_substring)
