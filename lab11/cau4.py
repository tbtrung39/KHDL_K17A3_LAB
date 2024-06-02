with open("f_in.dat", mode='r') as file:
    data = file.read().strip()

numbers = list(map(int, data.split()))

divisor_sum = 0

for number in numbers:
    for i in range(1, 10):
        if number % i == 0:
            divisor_sum += number

with open("f_out.dat", mode='w') as file:
    file.write(str(divisor_sum))
