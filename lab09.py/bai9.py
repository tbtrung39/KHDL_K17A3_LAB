digit = 0
ten_power = 1
def reverse_number(number):
    global digit
    global ten_power
    if number >10:
        reverse_number(number // 10)
    digit = (number % 10) * ten_power + digit
    ten_power = ten_power * 10

n = int(input("Nhập số: "))
reverse_number(n)
print(digit, "là số đảo ngược của", n)