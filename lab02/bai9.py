so_kw = int(input("nhập số điện :"))
if so_kw > 0 and so_kw <= 100 :
    don_gia = 2000
    tien_dien = so_kw * don_gia
    print("tiền điện :",tien_dien)
elif so_kw > 100 and so_kw <= 200 :
    don_gia = 2500
    tien_dien = (100 * 2000) + (so_kw - 100) * 2500
    print("tiền điện :",tien_dien)
elif so_kw > 200 and so_kw <= 300 :
    don_gia = 3000
    tien_dien = (100 * 2000) + (100 * 2500) + (so_kw - 300) * 3000
    print("tiền điện :",tien_dien)
elif so_kw > 300 and so_kw <= 400 :
    don_gia = 5000
    tien_dien = (100 * 2000) + (100 * 2500) +(100 * 3000) + (so_kw - 400) * 5000        
    print("tiền điện :",tien_dien)
        