def find_solutions(n,x1,x2,x3):
    if x1 + x2 + x3 == n:
        return x1,x2,x3
    elif x1 + x2 + x3 < n:
        find_solutions(n, x1+1, x2, 3)
        find_solutions(n, x1, x2+1 ,x3)
        find_solutions(n, x1, x2, x3+1)

N = int(input("Nhập số N: "))
print("Các nghiệm của pt là: ", find_solutions(N, 2, 2, 1))
