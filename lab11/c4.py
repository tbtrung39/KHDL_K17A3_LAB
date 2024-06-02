with open("f_in.dat",mode='r') as file:
    data = file.read()

with open("f_out.dat",mode='w') as file:
    divisor = 0
    for number in int(data):
        for i in range(1,10):
            if number % i ==0:
                divisor += number
    file.write(number)
