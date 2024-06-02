try:
    with open("lab11/dayso.dat", mode='r') as file:
        nums = [int(line.strip()) for line in file if line.strip().isdigit()]
except FileNotFoundError:
    print("The file 'lab11/dayso.dat' was not found.")
    nums = []

odd_sum = sum(num for num in nums if num % 2 != 0)

print(f"{odd_sum} là tổng số lẻ trong file")
