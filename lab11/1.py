def doc_day_so_tu_tap_tin(ten_tap_tin):
    day_so = []
    with open(ten_tap_tin, 'r') as file:
        for line in file:
            cac_so_trong_dong = map(int, line.split())
            day_so.extend(cac_so_trong_dong)
    return day_so
def tinh_tong_so_le(day_so):
    tong_so_le = sum(so for so in day_so if so % 2 != 0)
    return tong_so_le
def main():
    ten_tap_tin = 'dayso.dat'
    day_so = doc_day_so_tu_tap_tin(ten_tap_tin)
    print(f"Dãy số đã đọc từ tập tin: {day_so}")
    tong_so_le = tinh_tong_so_le(day_so)
    print(f"Tổng các số lẻ trong dãy: {tong_so_le}")
if __name__ == "__main__":
    main()
