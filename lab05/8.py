s = input("Nhập chuỗi kí tự :")
max_len = 0
max_str = ''
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub_str = s[i:j]
        if len(set(sub_str)) == 1 and len(sub_str) > max_len:
            max_len = len(sub_str)
            max_str = sub_str

print(max_str)  
