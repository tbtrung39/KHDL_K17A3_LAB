# Chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong khoảng [1,99999]
import random 
list_A = [random.randint(1,99999) for i in range(1000)]
print(list_A)
