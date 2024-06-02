# def kiemtraa(a):
#     for i in a:
#         count=0
#         for j in a:
#             if i !=j :
#                 break
#             else :
#                 count= count + 1
#         if count==4:
#             break
#         return count
# a=input("nhap day ki tu ")

# print(kiemtraa(a))


def kiem_tra_chuoi(chuoi):
    for c in chuoi:
        if not c.isalpha():
            raise ValueError("Lỗi ký tự !!!")
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")
def kiem_tra_tu_trung_lap(tu_danh_sach):
    for i in range(len(tu_danh_sach) - 4):
        if tu_danh_sach[i] == tu_danh_sach[i + 1] == tu_danh_sach[i + 2] == tu_danh_sach[i + 3] == tu_danh_sach[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")
def main():
    while True:
        try:
            chuoi = input("Nhập một chuỗi ký tự: ")
            kiem_tra_chuoi(chuoi)
            tu_danh_sach = chuoi.split()
            kiem_tra_tu_trung_lap(tu_danh_sach)
            print(f"Chuỗi hợp lệ: {chuoi}")
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()