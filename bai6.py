bang_so = [
    [4],
    [211, 133, 100, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]
with open('lab11\package_6\\bang_so.txt', mode = "w") as file:
    for row in bang_so:
        file.write(' '.join(map(str, row)) + '\n')
with open('lab11\package_6\\bang_so.txt', mode = "r") as f:
    lines = f.readlines()
    print("Dòng đầu tiên của bảng số là:")
    print(lines[0])
    print("Dòng thứ 3 của bảng số là:")
    print(lines[2])
    
print("Nội dung toàn bộ file là:")    
for row in bang_so:
    print(' '.join(map(str,row)))

with open("lab11\package_6\ODD.txt",mode = "w") as f:
    for row in bang_so:
        so_le = []
        for num in row:
            if num % 2 !=0:
                so_le.append(str(num))
            else:
                so_le.append("0")
        f.write(' '.join(so_le) + "\n")   
with open("lab11\package_6\ODD.txt", mode = "r") as f:
    print("Nội dung dòng cuối của file ODD.txt là:")
    print(f.readline()[-1])                              