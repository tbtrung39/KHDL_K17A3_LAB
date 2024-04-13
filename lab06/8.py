n=int(input("Nhập số n: "))
fibonacci=[0,1]
for _ in range(n-2):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(*fibonacci[:n], sep=", ", end="")
