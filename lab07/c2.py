numbers = set()
end = 'ESC'
while True:
    n = input("Nhập số: ")
    if n == end:
        break
    numbers.add(n)
print(numbers)

A = set()
A = {n for n in numbers if n.isdigit()}
A = numbers.pop()
print(A, "là các phần tử thuộc danh sách numbers")
