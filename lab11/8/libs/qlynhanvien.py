import csv
from libs import xu_Ly_thong_tin_nhanvien


def nhap_danh_sach_nhan_vien():
    danh_sach_nhan_vien = []
    while True:
        ma_nv = input("Nhập Mã NV (nhập 'q' để kết thúc): ")
        if ma_nv == 'q':
            break
        ten_nv = input('Nhập Tên NV: ')
        chuc_vu = input('Nhập Chức vụ: ')
        he_so_luong = float(input('Nhập Hệ số lương: '))
        nhan_vien = {'NV': ma_nv, 'Tên NV': ten_nv, 'Chức vụ': chuc_vu, 'Hệ số lương': he_so_luong}
        danh_sach_nhan_vien.append(nhan_vien)
    return danh_sach_nhan_vien

def tinh_luong_va_phu_cap(danh_sach_nhan_vien):
    for nv in danh_sach_nhan_vien:
        nv['Lương'] = nv['Hệ số lương'] * 1490000
        if nv['Chức vụ'] == 'TP':
            nv['Phụ cấp chức vụ'] = 1000000
        elif nv['Chức vụ'] == 'PP':
            nv['Phụ cấp chức vụ'] = 700000
        elif nv['Chức vụ'] == 'NV':
            nv['Phụ cấp chức vụ'] = 300000
        nv['Thực lĩnh'] = nv['Lương'] + nv['Phụ cấp chức vụ']
def in_danh_sach_nhan_vien(danh_sach_nhan_vien):
    if not danh_sach_nhan_vien:
        print('Danh sách nhân viên rỗng.')
        return
    print('{:<10} {:<20} {:<15} {:<15} {:<15} {:<15}'.format('Mã NV', 'Tên NV', 'Chức vụ', 'Hệ số lương', 'Lương', 'Thực lĩnh'))
    for nv in danh_sach_nhan_vien:
        print('{:<10} {:<20} {:<15} {:<15.2f} {:<15.2f} {:<15.2f}'.format(nv['NV'], nv['Tên NV'], nv['Chức vụ'], nv['Hệ số lương'], nv['Lương'], nv['Thực lĩnh']))
def sap_xep_va_in_danh_sach_theo_thuc_linh(danh_sach_nhan_vien):
    danh_sach_nhan_vien.sort(key=lambda x: x['Thực lĩnh'], reverse=True)
    print('Danh sách nhân viên sau khi được sắp xếp theo Thực lĩnh giảm dần:')
    in_danh_sach_nhan_vien(danh_sach_nhan_vien)
def luu_vao_file_csv(danh_sach_nhan_vien):
    with open('files/ds_nhanvien.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['NV', 'Tên NV', 'Chức vụ', 'Hệ số lương', 'Lương', 'Phụ cấp chức vụ', 'Thực lĩnh']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for nv in danh_sach_nhan_vien:
            writer.writerow(nv)
def main():
    danh_sach_nhan_vien = nhap_danh_sach_nhan_vien()
    tinh_luong_va_phu_cap(danh_sach_nhan_vien)
    print('\nDanh sách nhân viên sau khi tính lương và phụ cấp:')
    in_danh_sach_nhan_vien(danh_sach_nhan_vien)
    sap_xep_va_in_danh_sach_theo_thuc_linh(danh_sach_nhan_vien)
    luu_vao_file_csv(danh_sach_nhan_vien)
if __name__ == '__main__':
    main()