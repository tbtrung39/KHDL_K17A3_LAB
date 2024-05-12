# câu a
def sum_recursive_1(n):
    if n ==1:
        return 1/2
    else:
        return 1 / (n*(n+1)) + sum_recursive_1(n-1)
    
n = int(input("Nhập số cho câu a: "))
print(sum_recursive_1(n), "là kết quả của pt câu a")

# câu b
def sum_recursive_2(n):
    if n ==1:
        return 1
    else:
        return 1/(n-1) + sum_recursive_2(n-1)

n = int(input("Nhập số cho câu b: "))
print(sum_recursive_2(n), "là kết quả pt câu b")

# câu c
def sum_recursive_3(n):
    if n ==1:
        return 3
    else:
        return (3*n)**(1/2) + sum_recursive_3(n-1) 
    
n = int(input("Nhập số cho câu c: "))
print(sum_recursive_3(n), "là kết quả pt câu c")