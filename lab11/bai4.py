# Ensure the required modules are imported
import os

# Read the data from the input file
with open("lab11/f_in.dat", mode='r') as file:
    data = file.read().strip()

# Split the data into individual numbers and convert them to integers
try:
    numbers = list(map(int, data.split()))
except ValueError:
    print("The file contains non-integer values.")
    numbers = []

# Calculate the sum of divisors
divisor_sum = 0
for number in numbers:
    for i in range(1, 10):
        if number % i == 0:
            divisor_sum += number

# Write the result to the output file
with open("lab11/f_out.dat", mode='w') as file:
    file.write(str(divisor_sum))

print(f"The sum of numbers divisible by any integer from 1 to 9 is: {divisor_sum}")
