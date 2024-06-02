n = int(input("Nhập số: "))
if n <=0:
    print("Hãy nhập lại số nguyên dương")
else:
    sum = 0
    for i in range(1,n+1):
        if n % i ==0:
            sum += i 
            if sum == n:
                print(n, "là số hoàn hảo")
            else:
                a = n-1
                for j in range(a):
                    print(a, "là số hoàn hảo gần ", n , "nhất")