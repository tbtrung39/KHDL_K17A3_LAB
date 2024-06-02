def doc_day_so_tu_tap_tin(ten_tap_tin):
    with open(ten_tap_tin, 'r') as file:
        noi_dung = file.read()
    day_so = list(map(int, noi_dung.split()))
    return day_so
def ghi_day_so_vao_tap_tin(ten_tap_tin, day_so):
    with open(ten_tap_tin, 'w') as file:
        file.write(" ".join(map(str, day_so)))
def main():
    ten_tap_tin_in = 'Inp.txt'
    ten_tap_tin_out = 'out.dat'
    day_so = doc_day_so_tu_tap_tin(ten_tap_tin_in)
    day_so.sort()
    ghi_day_so_vao_tap_tin(ten_tap_tin_out, day_so)
    print(f"Dãy số đã được sắp xếp và ghi vào tập tin {ten_tap_tin_out}.")
if __name__ == "__main__":
    main()
