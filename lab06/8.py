n = int(input("Nhập số lượng phần tử của dãy Fibonacci: "))
fib_dtien = [0, 1]
for i in range(2, n):
    fib_dtien.append(fib_dtien[-1] + fib_dtien[-2])
fib_tuple = tuple(fib_dtien)
print(",".join(map(str, fib_tuple)))