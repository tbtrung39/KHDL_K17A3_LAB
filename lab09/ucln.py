def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a % b)

a=10
b=6
print(uscln(a, b))