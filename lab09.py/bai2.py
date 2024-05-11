num1 = int(input("Nhập số thứ 1: "))
num2 = int(input("Nhập số thứ 2: "))
if num1 > num2:
    min = num2
    max = num1
else:
    min = num1
    max = num2

def the_gcd_of_two_numbers(max,min):
    if min == 0:
        return max
    else:
        return the_gcd_of_two_numbers(min, max % min)
result = the_gcd_of_two_numbers(max,min)
print(result, "là ước chung lớn nhất")