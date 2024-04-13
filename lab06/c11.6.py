import random
#A
n = int(input("nhap so luong phan tu trong danh sach : "))
A=[int(input("nhap phan tu thu{} :".fomat(i+1))) for i in range(n)]

#b
B= [i for i in A if i % 3 == 0 and i % 5 !=0 ]
print("danh sach B: ",B)

#C
C = [i**2 for i in A]
print("danh sach C:", C)
#D
D = random.choices([i for i in A if i % 3 ==0], k=n)
print("Danh sach D:",D )