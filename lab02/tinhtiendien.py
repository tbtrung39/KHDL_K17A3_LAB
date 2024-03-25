def tinhtiendien(n):
    if n>0 and n<51:
        tiendien = n*1.678
        return tiendien
    elif n >=51  and n<101:
        tiendien1 = n*1.734
        return tiendien1
    elif n>=101 and n<201:
        tiendien2 = n*2.014
        return tiendien2
    elif n>=201 and n<300:
        tiendien3 = n*2.536
        return tiendien3

def main():
    n = float(input("Nhap so dien"))
    sotiencantra = tinhtiendien(n)
    if sotiencantra:
        print (f"Tien dien cua quy khach la",sotiencantra,"dong")
    else:
        return None
    
main()