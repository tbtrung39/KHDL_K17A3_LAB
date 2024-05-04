def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
def so_ngay_trong_thang(thang, nam):
    if thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31
def main():
    nam = int(input("Nhập năm: "))
    thang = int(input("Nhập tháng: "))
    if la_nam_nhuan(nam):
        print("Năm", nam, "là năm nhuận.")
    else:
        print("Năm", nam, "không phải là năm nhuận.")
    print("Số ngày tối đa của tháng", thang, "trong năm", nam, "là:", so_ngay_trong_thang(thang, nam))
if __name__ == "__main__":
    main()
