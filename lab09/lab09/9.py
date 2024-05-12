def reverse_number(number, reversed_num=0):
    if number == 0:
        return reversed_num
    else:
        last_digit = number % 10
        new_reversed_num = reversed_num * 10 + last_digit
        remaining_number = number // 10
        return reverse_number(remaining_number, new_reversed_num)

n = int(input('Nhập số: '))
reversed_n = reverse_number(n)
print(f'Số đảo ngược của {n} là: {reversed_n}')
