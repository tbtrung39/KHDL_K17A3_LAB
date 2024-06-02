def sum_odd_numbers(file_name):
    total = 0
    with open(file_name, 'r') as file:
        for line in file:

            numbers = line.strip().split()
            for num in numbers:
                try:
                    num = int(num)
                    if num % 2 != 0:
                        total += num
                except ValueError:
                    print(f"Lỗi: '{num}' không phải là một số nguyên.")
    return total
file_name = 'dayso.dat'
odd_sum = sum_odd_numbers(file_name)
print(f'Tổng các số hạng lẻ trong dãy số là: {odd_sum}')