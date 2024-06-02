with open("lab11/Inp.txt",mode='r') as file:
    data = file.readline()

numbers = list(data.split())
numbers.sort(reverse=False)

with open("lab11/out.dat",mode='w') as file:
    for num in numbers:
        file.write(num)