n = int(input("Nhập số n: "))
lst = []
for i in range(1,n+1):
    lst.append(i)
even_numbers = filter(lambda x: x % 2 ==0, lst)
print(list(even_numbers), "là các số chẵn trong khoảng từ 1 tới ",n)

new_lst = []
for j in lst:
    if j % 2 ==0:
        new_lst.append(j)
import functools
print("Tổng các số chẵn trong list đã nhập là: ")
print(functools.reduce(lambda x,y : x+y , new_lst))
      