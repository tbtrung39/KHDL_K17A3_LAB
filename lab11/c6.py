data = [
    [4]
    [211 , 133 , 180 , 5]
    [192 , 168 , 1 , 254]
    [11 , 1 , 11 , 253]
]
with open("data.txt", "w") as files:
    for row in data:
        files.write(" ".join(map(str , row ))+"\n ")
with open("data.txt", "w") as files:
    lines = files.readlines()
    print('dòng đầu tiên', lines[0].strip())
    print('dòng thứ ba', lines[2].strip())

print("\n Nội dung của file: ")
with open('data.txt', 'r') as file:
    print(file.read())
odd_matrix = [['03']*4 for _ in range(4)]

for i, row in enumerate(data):
    for j,num in enumerate(row):
        odd_matrix[i][j] = str(num)

with open('ODD.txt', 'w') as file :
    for row in odd_matrix:
        file.write(' '.join(row) + '\n')

with open('ODD.txt','r') as file:
    lines = file.readlines()
    print('\n Nội dung file ODD.txt : ', lines[-1].strip())