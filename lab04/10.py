stp = int(input("Nhập một số thập phân: "))
if stp < 0:
    print("Vui lòng nhập một số không âm.")
else:
    ky_tu = ""
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    while stp > 0:
        don_vi = stp % 10
        ky_tu = chu_so[don_vi] + " " + ky_tu
        stp //= 10
    print("Số được chuyển thành dạng ký tự là:", ky_tu.strip())