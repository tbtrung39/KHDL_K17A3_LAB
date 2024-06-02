import csv

def nhap_danh_sach_sinh_vien():
    danh_sach_sinh_vien = []
    while True:
        ma_sv = input("Nhập mã sinh viên (nhập 'enter' để kết thúc): ")
        if ma_sv == '':
            break
        ho_ten = input('Nhập họ và tên: ')
        diem_tb = float(input('Nhập điểm trung bình: '))
        diem_rl = float(input('Nhập điểm rèn luyện: '))
        sinh_vien = {'Mã SV': ma_sv, 'Họ và tên': ho_ten, 'Điểm TB': diem_tb, 'Điểm RL': diem_rl}
        danh_sach_sinh_vien.append(sinh_vien)
    return danh_sach_sinh_vien

def tinh_diem_tl(danh_sach_sinh_vien):
    for sinh_vien in danh_sach_sinh_vien:
        sinh_vien['Điểm TL'] = (sinh_vien['Điểm TB'] + sinh_vien['Điểm RL']) / 2

def in_danh_sach_sinh_vien(danh_sach_sinh_vien):
    if not danh_sach_sinh_vien:
        print('Danh sách sinh viên rỗng.')
        return
    print('{:<10} {:<30} {:<10} {:<10} {:<10}'.format('Mã SV', 'Họ và tên', 'Điểm TB', 'Điểm RL', 'Điểm TL'))
    for sinh_vien in danh_sach_sinh_vien:
        print('{:<10} {:<30} {:<10.2f} {:<10.2f} {:<10.2f}'.format(sinh_vien['Mã SV'], sinh_vien['Họ và tên'], sinh_vien['Điểm TB'], sinh_vien['Điểm RL'], sinh_vien['Điểm TL']))

def sap_xep_theo_diem_rl(danh_sach_sinh_vien):
    danh_sach_sinh_vien.sort(key=lambda x: x['Điểm RL'])

def sinh_vien_co_diem_tl_cao_nhat(danh_sach_sinh_vien):
    sinh_vien = max(danh_sach_sinh_vien, key=lambda x: x['Điểm TL'])
    return sinh_vien

def luu_vao_file_csv(danh_sach_sinh_vien):
    with open('files/ds_sinhvien.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Mã SV', 'Họ và tên', 'Điểm TB', 'Điểm RL', 'Điểm TL']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for sinh_vien in danh_sach_sinh_vien:
            writer.writerow(sinh_vien)

def main():
    danh_sach_sinh_vien = nhap_danh_sach_sinh_vien()
    tinh_diem_tl(danh_sach_sinh_vien)
    sap_xep_theo_diem_rl(danh_sach_sinh_vien)
    in_danh_sach_sinh_vien(danh_sach_sinh_vien)
    
    sinh_vien_max_diem_tl = sinh_vien_co_diem_tl_cao_nhat(danh_sach_sinh_vien)
    print(f'\nSinh viên có điểm TL cao nhất:\nMã SV: {sinh_vien_max_diem_tl['Mã SV']}\nHọ và tên: {sinh_vien_max_diem_tl['Họ và tên']}\nĐiểm TL: {sinh_vien_max_diem_tl['Điểm TL']}')

    luu_vao_file_csv(danh_sach_sinh_vien)

if __name__ == '__main__':
    main()
