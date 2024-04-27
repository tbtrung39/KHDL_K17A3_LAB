def ucln(a, b):
    while b != 0:
        a, b = b, a%b
    return a        
def phan_so(tu_so, mau_so):
    uoc_chung = ucln(tu_so, mau_so)
    tu_so_rut_gon = tu_so//uoc_chung
    mau_so_rut_gon = mau_so//uoc_chung
    return tu_so_rut_gon, mau_so_rut_gon
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
while mau_so == 0:
    mau_so = int(input("Mẫu số phải là một số khác 0, vui lòng nhập lại: "))
        
tu_so_moi, mau_so_moi = phan_so(tu_so, mau_so)    
print("Phân số ban đầu là:",tu_so,"/",mau_so)
print("Phân số sau khi đã rút gọn là:",tu_so_moi,"/",mau_so_moi)        