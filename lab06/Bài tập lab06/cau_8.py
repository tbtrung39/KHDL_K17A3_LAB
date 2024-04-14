n = int(input("Nhập số phần tử của dãy Fibonacci: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
fib_string = ""
for i in range(len(fib)):
    fib_string += str(fib[i])
    if i != len(fib) - 1:
        fib_string += ", "
print(fib_string)
