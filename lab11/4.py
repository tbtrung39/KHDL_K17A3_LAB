def doc_day_so_tu_tap_tin(ten_tap_tin):
    day_so = []
    with open(ten_tap_tin, 'r') as file:
        for line in file:
            so = int(line.strip())
            day_so.append(so)
    return day_so
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def uoc_so_nguyen_to_khac_nhau(n):
    uoc_so = set()
    for i in range(2, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            uoc_so.add(i)
    return uoc_so
def ghi_uoc_so_vao_tap_tin(ten_tap_tin, cac_uoc_so):
    with open(ten_tap_tin, 'w') as file:
        for uoc_so in cac_uoc_so:
            file.write(" ".join(map(str, uoc_so)) + "\n")
def main():
    ten_tap_tin_in = 'f_in.dat'
    ten_tap_tin_out = 'f_out.dat'
    day_so = doc_day_so_tu_tap_tin(ten_tap_tin_in)
    cac_uoc_so = [uoc_so_nguyen_to_khac_nhau(so) for so in day_so]
    ghi_uoc_so_vao_tap_tin(ten_tap_tin_out, cac_uoc_so)
    print(f"Các ước số nguyên tố đã được ghi vào tập tin {ten_tap_tin_out}.")
if __name__ == "__main__":
    main()
