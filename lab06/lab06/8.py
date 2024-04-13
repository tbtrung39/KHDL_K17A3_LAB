n = int(input("Nhập số lượng phần tử của dãy day_so: "))

day_so = [0, 1] if n >= 2 else [0] if n == 1 else []

[day_so.append(day_so[-1] + day_so[-2]) for _ in range(n-2)]

print("Dãy fibonacci:")
print(" , ".join(map(str, day_so)))
