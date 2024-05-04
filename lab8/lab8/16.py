def tao_danh_sach_so_chan():
    danh_sach_so_chan = [x for x in range(1, 101) if x % 2 == 0]
    return danh_sach_so_chan

def main():
    danh_sach = tao_danh_sach_so_chan()
    print('Danh sách chứa tất cả các số chẵn từ 1 đến 100 là:')
    print(danh_sach)

if __name__ == '__main__':
    main()