char_to_num = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
so_container = input("Nhập số container: ")
tong_trong_so = 0
i = 0 
for char in so_container:
    if char in char_to_num:
        num = char_to_num[char]
    else:
        num = int(char)
    tong_trong_so += num * (2 ** i)
    i += 1
so_kiem_tra = tong_trong_so % 11
print("Số kiểm tra của mã container",so_container,"Là:",so_kiem_tra)