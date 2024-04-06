n = int(input("Nhập một số nguyên dương: "))
if n < 2:
    print("Số bạn nhập không phải là số nguyên dương lớn hơn 1.")
else:
    pt = []
    for i in range(2, n + 1):
        while n % i == 0:
            pt.append(i)
            n //= i
        if n == 1:
            break

    print(f"Dạng phân tích thừa số nguyên tố của {n} là:", end=" ")
    for i, pt in enumerate(pt):
        if i < len(pt) - 1:
            print(pt, end=" x ")
        else:
            print(pt)