import csv
with open ("so.txt",'r') as so:
    openfile = csv.reader(so)
    listfile = list(openfile)
#a
print("a)File so.txt sau khi in ra")
for i in (listfile):
    print(i)

#b
print("b)")
print("Dòng 1: ",listfile[0][0])
print("Dòng 3: ",listfile[2][0])

#c
# Đọc file txt và chuyển đổi nó thành một ma trận
with open('so.txt', 'r') as file:
    matrix = [list(map(int, line.split())) for line in file.readlines()]

# Tạo một ma trận mới với các số lẻ, thay thế các số chẵn bằng 0
    odd_matrix = [[num if num % 2 != 0 else 0 for num in row] for row in matrix]

# Ghi ma trận mới vào file ODD.txt
with open('ODD.txt', 'w') as file:
    for row in odd_matrix:
        file.write(' '.join(str(num) for num in row) + '\n')

#d
# Mở file ODD.txt và đọc nội dung
print("d)")
with open('ODD.txt', 'r') as file:
    lines = file.readlines()
# In ra dòng cuối cùng
    print("Dòng cuối của file ODD.txt: ",lines[-1].strip())