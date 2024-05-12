#câu a
def s(n):
    if n == 1:
        return 1/2
    else:
        return 1 / (n*(n+1)) + s(n-1)

n = int(input('Nhập số cho câu a: '))
print(f'Kết quả của câu a là: {s(n)}')
#câu b
def s2(n):
    if n == 1:
        return 1
    else:
        return 1/(n-1) + s2(n-1)

n = int(input('Nhập số cho câu b: '))
print(f'Kết quả của câu b là: {s2(n)} ')
#câu c
def s3(n):
    if n == 1:
        return 3
    else:
        return (3*n)**(1/2) + s3(n-1) 

n = int(input('Nhập số cho câu c: '))
print(f'Kết quả của câu c là: {s3(n)}')

