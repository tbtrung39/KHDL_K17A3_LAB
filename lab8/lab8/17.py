from functools import reduce

def nhap_danh_sach(n):
    danh_sach = []
    while True:
        danh_sach = list(map(int, input(f'Nhập các số nguyên từ 1 đến {n}: ').split()))
        if all(1 <= x <= n for x in danh_sach):
            break
        print('Danh sách không hợp lệ. Vui lòng nhập lại.')
    return danh_sach

def tinh_tong_so_chan(danh_sach):
    tong = reduce(lambda x, y: x + y if y % 2 == 0 else x, danh_sach, 0)
    return tong

def main():
    n = int(input('Nhập số nguyên dương n: '))
    danh_sach = nhap_danh_sach(n)
    tong = tinh_tong_so_chan(danh_sach)
    if tong == 0:
        print('Danh sách không chứa số chẵn nào.')
    else:
        print(f'Tổng các số chẵn trong danh sách là: {tong}')

if __name__ == '__main__':
    main()