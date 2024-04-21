n = int(input("Nhập số thực: "))
import random
set_A = {random.randint(0,n+1) for i in range(n)}
max_A = max(set_A)
min_A = min(set_A)
sum_A = sum(set_A)
print("Giá trị max các phần tử của set A là: ", max_A)
print("Giá trị min các phần tử của set A là: ", min_A)
print("Tổng các phần tử của set A là: ", sum_A)

