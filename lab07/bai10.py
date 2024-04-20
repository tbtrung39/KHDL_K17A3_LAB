n=int(input("Nhap gia tri n "))
m=int(input("Nhap gia tri m "))
q = m & n
result = 0
for i in range(len(q)):
    result = result + int(q.pop())
print(result)