n = int(input("Nhập vào số n: "))
fibonacci = [0, 1] + [fibonacci[-2] + fibonacci[-1] for _ in range(n-2)]
print(", ".join(map(str, fibonacci)))
