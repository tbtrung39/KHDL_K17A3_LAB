import os

# Ensure the lab11 directory exists
os.makedirs("lab11", exist_ok=True)

# Corrected data list definition
data = [
    [4],
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 253]
]

# Writing data to 'data.txt'
with open("lab11/data.txt", "w") as file:
    for row in data:
        file.write(" ".join(map(str, row)) + "\n")

# Reading from 'data.txt' and printing specific lines
with open("lab11/data.txt", "r") as file:
    lines = file.readlines()
    print('dòng đầu tiên:', lines[0].strip())
    if len(lines) > 2:
        print('dòng thứ ba:', lines[2].strip())

print("\nNội dung của file:")
with open("lab11/data.txt", "r") as file:
    print(file.read())

# Creating the odd matrix
odd_matrix = [['03']*4 for _ in range(4)]
for i, row in enumerate(data):
    for j, num in enumerate(row):
        if num % 2 != 0:
            odd_matrix[i][j] = str(num)

# Writing the odd matrix to 'ODD.txt'
with open("lab11/ODD.txt", "w") as file:
    for row in odd_matrix:
        file.write(' '.join(row) + '\n')

# Reading from 'ODD.txt' and printing the last line
with open("lab11/ODD.txt", "r") as file:
    lines = file.readlines()
    print('\nNội dung file lab11/ODD.txt:', lines[-1].strip())
