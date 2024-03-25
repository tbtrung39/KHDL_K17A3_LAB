n = int(input("Nhập số lần tung xúc sắc (n): "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    total_outcomes = 6 ** n
    outcomes_without_six = 5 ** n
    at_least_one_six = total_outcomes - outcomes_without_six
    probability = at_least_one_six / total_outcomes
    result = round(probability, 2)
    print("Xác suất khi tung", n, "lần 3 xúc sắc có ít nhất một lần cả ba xúc sắc đều ra 6 là:", result)
