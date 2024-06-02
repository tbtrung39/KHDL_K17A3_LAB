def prime_num_checker(x):
    for i in range(2,x):
        if x % i !=0 and i % 2 !=0:
            print(i)
        
n = int(input("Nhập số: "))
if n <=2:
    print("Vui lòng nhập lại")
prime_num_checker(n)