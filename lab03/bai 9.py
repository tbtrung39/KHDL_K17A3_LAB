
n = int(input("nhập vào số nguyên tố n: "))
suma = 0
sumb = 0
sumc= 0
for i in range(1,n+1):
    suma += i**2
    if i % 2 == 0:
        sumb += i**3
    if i % 2 != 0:
        sumc += i**4
    if n <= 0:
        break
print(suma)
print(sumb)
print(sumc)
