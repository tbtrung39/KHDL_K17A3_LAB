def permutation(n):
    if len(n) ==1:
        return [n]
    perms = permutation(n[1:])
    char = n[0]
    result = []
    for perm in perms:
        for i in range(len(perm) +1):
            result.append(perm[:i] + char + perm[i:])
    return result

n = input("Nhập số: ")
print(permutation(n))