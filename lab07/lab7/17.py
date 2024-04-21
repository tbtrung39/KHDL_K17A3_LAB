a = [1, 2, 3, 2, 4]
pairs = [(i, j) for i in range(len(a)) for j in range(i+1, len(a)) if a[i] + 1 == a[j]]
print(pairs)