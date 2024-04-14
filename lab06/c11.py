lst_A = []
while True:
    n = input("Nhập phần tử số nguyên vào list A: (Nhập esc để dừng) ")
    if n.upper() == 'ESC':
        break
    lst_A.append(int(n))
lst_B = [num for num in lst_A if num % 3 ==0 and num % 5 != 0]
print(lst_B)
lst_C = [num for num in lst_A if num == num **2]
print(lst_C)
import random
lst_D = [num for num in lst_A if random.randint(num,n+1) % 3 ==0]
print(lst_D)
