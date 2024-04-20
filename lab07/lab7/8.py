def main():
    tap_hop_A = set(input("Nhap cac phan tu cho tap hop A, cach nhau boi dau cach: ").split())
    
    print("Tap hop A: ", tap_hop_A)
    
    so_nguyen = sum(1 for x in tap_hop_A if x.isdigit())
    so_thuc = sum(1 for x in tap_hop_A if x.replace('.', '', 1).isdigit() and '.' in x)
    chuoi_ky_tu = len(tap_hop_A) - so_nguyen - so_thuc
    
    print("So phan tu la so nguyen: ", so_nguyen)
    print("So phan tu la so thuc: ", so_thuc)
    print("So phan tu la chuoi ky tu: ", chuoi_ky_tu)

if __name__ == "__main__":
    main()
