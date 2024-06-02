with open("f_in.dat",mode='r') as file:
    data = file.readline().strip()

numbers = list(map(int, data.split()))
extreme = []
n = len(numbers)

for i in range(1,n-1):
    if numbers[i-1] < numbers[i] > numbers[i+1] or numbers[i-1] > numbers[i] < numbers[i+1]:
        extreme.append(numbers[i])

with open("f_out.dat",mode='w') as file:
    file.write(",".join(map(str, extreme)))

