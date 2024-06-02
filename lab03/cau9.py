# câu a
n = int(input("Nhập số: "))
if n <=0:
  print("Không hợp lệ")
else:
  sum1 = 0
  for i in range(1, n+1):
    sum1 += i **2
print("Tổng dãy số câu a là: ", sum1)

# câu b 
n = int(input("Nhập số: "))
if n <=0:
  print("Không hợp lệ")
for i in range(1,n+1):
  sum2 = 0
  if i % 2 !=0:
    sum2 += i**3
print("Tổng dãy số câu b là: ", sum2)
    
# câu c
n = int(input("Nhập số: "))
if n <=0:
  print("Không hợp lệ")
for i in range(1,n+1):
  sum3 = 0
  if i % 2 ==0:
    sum3 += i **4
print("Tổng dãy số câu c là: ", sum3)