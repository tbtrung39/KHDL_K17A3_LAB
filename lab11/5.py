# Đọc dữ liệu từ các tập tin
def doc_du_lieu(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.strip().split() for line in file]

def lap_rap_thong_tin(sbd_phach, sbd_ten, phieu_diem):
    sbd_to_phach = {sbd: phach for sbd, phach in sbd_phach}
    phach_to_diem = {phach: diem for phach, diem in phieu_diem}
    sbd_to_ten = {sbd: ' '.join(ten) for sbd, *ten in sbd_ten}

    thong_tin_thi_sinh = []
    for sbd, ten in sbd_to_ten.items():
        phach = sbd_to_phach.get(sbd)
        diem = phach_to_diem.get(phach)
        if phach is not None and diem is not None:
            thong_tin_thi_sinh.append((sbd, ten, diem))
    return thong_tin_thi_sinh


# Sắp xếp và ghi kết quả ra tập tin
def sap_xep_va_ghi_ket_qua(thong_tin_thi_sinh):
    thong_tin_thi_sinh.sort(key=lambda x: -float(x[2]))  # Sắp xếp theo điểm giảm dần
    with open('Ketqua.txt', 'w', encoding='utf-8') as file:
        for sbd, ten, diem in thong_tin_thi_sinh:
            file.write(f'{sbd} {ten} {diem}\n')

# Chính
if __name__ == '__main__':
    sbd_phach = doc_du_lieu('Sbd_Ph.dat')
    sbd_ten = doc_du_lieu('SBD_Ten.txt')
    phieu_diem = doc_du_lieu('Phieu_Diem.txt')

    thong_tin_thi_sinh = lap_rap_thong_tin(sbd_phach, sbd_ten, phieu_diem)
    sap_xep_va_ghi_ket_qua(thong_tin_thi_sinh)
