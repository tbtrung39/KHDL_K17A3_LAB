# Viết chương trình xét xem một số n có phải là số nguyên tố không. Nếu không phải hãy in ra số nguyên tố gần n nhất?
n=int(input("Nhập một số nguyên dương n: "))
for i in range(n, 0, -1):   #đảo ngược, tìm từ phải sang trái
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("so nguyen to la:", i)
        break