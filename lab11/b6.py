data = [
    [4],
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 253]
]
with open("data.txt", "w") as file:
    for row in data:
        file.write(" ".join(map(str, row)) + "\n")
with open("data.txt", "r") as file:
    lines = file.readlines()
    print('dong dau tien:', lines[0].strip())
    print('dong thu ba:', lines[2].strip())
print("\nNoi dung toan bo file:")
with open('data.txt', 'r') as file:
    print(file.read())
odd_matrix = [['03']*4 for _ in range(4)]
for i, row in enumerate(data):
    for j, num in enumerate(row):
        odd_matrix[i][j] = str(num).zfill(2)
with open('ODD.txt', 'w') as file:
    for row in odd_matrix:
        file.write(' '.join(row) + '\n')
with open('ODD.txt', 'r') as file:
    lines = file.readlines()
    print('\nNoi dung cua file ODD.txt:', lines[-1].strip())
