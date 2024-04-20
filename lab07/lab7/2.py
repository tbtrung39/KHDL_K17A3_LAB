Numbers = []

n = int(input("Nhập số lượng phần tử: "))

for i in range(n):
    num = input("Nhập phần tử thứ {}: ".format(i+1))
    Numbers.append(num)

A = set(Numbers)

print("Tập hợp A: ", A)
