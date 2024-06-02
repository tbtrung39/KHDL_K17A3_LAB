from datetime import datetime, timedelta 
def nhap_ngay() :
    while True:
        try:
            ngay=int(input("Nhap ngay: "))
            thang=int(input ("Nhap thang: "))
            nam=int(input ("Nhap nam: "))
            ngay_hien_tai=datetime(nam, thang, ngay)
            return ngay_hien_tai
        except ValueError:
            print ("Loi: Vui long nhap ngay hop le!")
def tim_ngay_ke_tiep(ngay_hien_tai):
    ngay_ke_tiep=ngay_hien_tai-timedelta(days=1)
    return ngay_ke_tiep
def main():
    ngay_hien_tai=nhap_ngay()
    ngay_ke_tiep=tim_ngay_ke_tiep(ngay_hien_tai)
    print ("Ngay ke tiep la:", ngay_ke_tiep.strftime ("%d/%m/%Y"))
main()