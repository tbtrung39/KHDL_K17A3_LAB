def read_sbd_ph(file_path):
    sbd_ph = {}
    with open(file_path, "r") as file:
        for line in file:
            sbd,phach= map(int,line.split())
            sbd_ph[phach] = sbd
            return sbd_ph

def read_sbd_ten(file_path):
    sbd_ten = {}
    with open(file_path, "r") as file:
        for line in file:
            parts= line.split()
            sbd = int(parts[0])
            ten = ''.join(parts[1:])


def read_phieu_diem(file_path):
    phieu_diem = {}
    with open(file_path, "r") as file:
        for line in file:
            phach , diem = map(int,line.split())
            phieu_diem[phach] = diem
        return phieu_diem

def merge_data(sbd_ph , sbd_ten , phieu_diem):
    resul = []
    for phach ,sbd in sbd_ph.items():
        if sbd in sbd_ten and phach in phieu_diem:
            ten = sbd_ten[sbd]
            diem = phieu_diem[phach]
            resul.append((sbd, ten, diem))
            return resul
        
def sap_xep(thong_tin):
    return sorted(thong_tin , key = lambda x : x[2] , reverse= True)

def ghi_du_lieu(file_path ,sorted_data):
    with open(file_path , "w ") as file:
        for sbd , ten ,diem in sorted_data:
            file.write(f"{sbd} {ten} {diem} \n")


def main():
    sbd_ph_file = "sbd_ph.dat"
    sbd_ten_file = "sbd_ten.txt"
    phieu_diem_file = "phieu_diem_txt"
    ket_qua_file = "ket_qua.txt"
    sbd_ph = read_sbd_ph(sbd_ph_file)
    sbd_ten = read_sbd_ten(sbd_ten_file)
    phieu_diem = read_phieu_diem(phieu_diem_file)
    thong_tin = merge_data(sbd_ph , sbd_ten , phieu_diem )
    sorted_thong_tin = sap_xep(thong_tin)
    ghi_du_lieu(ket_qua_file , sorted_thong_tin)

if __name__ == "__main__" :
    main()