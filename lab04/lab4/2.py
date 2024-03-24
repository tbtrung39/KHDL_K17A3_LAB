n = int(input("Nhập một số nguyên dương: "))
while n <= 0:
    print("Vui lòng nhập một số lớn hơn 0.")
    n = int(input("Nhập một số nguyên dương: "))

Sa, Sb, Sc = 0, 0, 0
i = 1

while i <= n:
    Sa += 1/i
    Sb += 1/(i*(i+1))
    Sc += 1/(i**0.5)
    i += 1

print(f"Sa = {Sa}")
print(f"Sb = {Sb}")
print(f"Sc = {Sc}")
