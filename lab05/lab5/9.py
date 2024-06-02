str1 = input('Nhập chuỗi ký tự Str1: ')
str2 = input('Nhập chuỗi ký tự Str2: ')

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

max_length = 0 
max_substring = ''

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]  
                max_substring = str1[i - max_length:i] 
        else:
            dp[i][j] = 0 

print(f'Chuỗi con chung có độ dài cực đại của Str1 và Str2: {max_substring}')