n = int(input("Nhập số hàng của tam giác: "))
for i in range(n): 
    if i == 0:  
        print(" " * (n - 1) + "*")
    elif i == n - 1:  
        print("* " * (n - 1) + "*")
    else:  
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
for i in range(1, 6):  
    print("  " * (5 - i) + " *" * (2 * i - 1))  