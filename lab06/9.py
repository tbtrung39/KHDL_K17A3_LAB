lst=[]
while True:
    n=int(input("Nhập số tự nhiên n: "))
    if n<=0:
        break
    lst.append(n)
print("Danh sách sau khi nhập: ",lst)
try:
    assert all(i % 2 == 0 for i in lst), "Không phải tất cả các số trong danh sách là số chẵn."
    print("Tất cả các số trong danh sách là số chẵn.")
except AssertionError as e:
    print(e)
